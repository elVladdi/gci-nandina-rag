"""
Generador del corpus documental NANDINA-Arancel v0.1.

Este módulo construye una versión procesada del corpus documental del proyecto
"Gestión de información documental para la recomendación auditable de subpartidas
NANDINA mediante recuperación documental y LLM+RAG".

El script realiza las siguientes operaciones:

1. Localiza los documentos fuente en data/external.
2. Extrae texto página por página desde archivos PDF.
3. Normaliza el texto extraído sin modificar el contenido normativo esencial.
4. Segmenta el contenido en fragmentos recuperables.
5. Asigna metadatos mínimos de trazabilidad por documento y por fragmento.
6. Exporta el corpus en JSONL y un inventario documental en CSV.
7. Genera un reporte Markdown de la corrida.

La implementación evita convertir la salida del sistema en una clasificación oficial.
El corpus generado se usa únicamente como artefacto experimental para recuperación,
reordenamiento y explicación auditable en condiciones offline.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator, Optional


# -----------------------------------------------------------------------------
# Configuración general del corpus
# -----------------------------------------------------------------------------

CORPUS_VERSION = "v0.1"
DEFAULT_EXTERNAL_DIR = Path("data/external")
DEFAULT_OUTPUT_DIR = Path("data/processed/corpus")

# El script usa patrones flexibles porque los nombres de archivo pueden contener
# tildes, espacios, variantes Unicode o errores menores de escritura.
DEFAULT_SOURCE_PATTERNS = {
    "arancel_2022": ["*Arancel*2022*.pdf", "*arancel*2022*.pdf"],
    "nandina_decision_885": ["*885*NANDINA*.pdf", "*885*Nandina*.pdf", "*885*Nanadina*.pdf", "*885*.pdf"],
}


@dataclass(frozen=True)
class DocumentRecord:
    """Representa los metadatos mínimos de un documento fuente."""

    doc_id: str
    titulo_documento: str
    ruta_archivo_origen: str
    nombre_archivo: str
    extension: str
    hash_sha256: str
    tamano_bytes: int
    version_corpus: str
    fecha_procesamiento_utc: str
    paginas_extraidas: int
    caracteres_extraidos: int
    observaciones: str


@dataclass(frozen=True)
class CorpusChunk:
    """Representa un fragmento documental recuperable del corpus."""

    chunk_id: str
    version_corpus: str
    doc_id: str
    titulo_documento: str
    ruta_archivo_origen: str
    nombre_archivo: str
    pagina: int
    bloque_en_pagina: int
    tipo_fragmento: str
    seccion: Optional[str]
    capitulo: Optional[str]
    partida: Optional[str]
    subpartida: Optional[str]
    codigo_detectado: Optional[str]
    texto_fragmento: str
    longitud_caracteres: int
    hash_texto_sha256: str


# -----------------------------------------------------------------------------
# Utilidades de ruta, hash y normalización
# -----------------------------------------------------------------------------


def utc_now_iso() -> str:
    """Devuelve la fecha de procesamiento en formato ISO 8601 UTC."""

    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()



def calculate_file_sha256(path: Path) -> str:
    """Calcula el hash SHA-256 de un archivo fuente para trazabilidad."""

    digest = hashlib.sha256()
    with path.open("rb") as file_obj:
        for block in iter(lambda: file_obj.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()



def calculate_text_sha256(text: str) -> str:
    """Calcula el hash SHA-256 de un fragmento textual normalizado."""

    return hashlib.sha256(text.encode("utf-8")).hexdigest()



def normalize_text(text: str) -> str:
    """
    Normaliza texto extraído desde PDF.

    La normalización elimina espacios redundantes, caracteres de control y saltos
    de línea excesivos. No elimina tildes ni cambia el contenido normativo.
    """

    text = text.replace("\x00", " ")
    text = text.replace("\u00ad", "")  # guion blando
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" +\n", "\n", text)
    text = re.sub(r"\n +", "\n", text)
    return text.strip()



def clean_pdf_header_footer(text: str) -> str:
    """
    Reduce encabezados y pies de página frecuentes.

    La limpieza es conservadora. El script evita reglas agresivas porque los PDF
    normativos pueden contener información relevante en encabezados de sección.
    """

    lines = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            lines.append("")
            continue

        # Se descartan marcadores repetitivos de paginación cuando aparecen solos.
        if re.fullmatch(r"GACETA OFICIAL\s+\d{1,2}/\d{1,2}/\d{4}\s+\d+\s+de\s+\d+", line, flags=re.IGNORECASE):
            continue
        if re.fullmatch(r"\d+\s+de\s+\d+", line, flags=re.IGNORECASE):
            continue

        lines.append(line)

    return normalize_text("\n".join(lines))


# -----------------------------------------------------------------------------
# Extracción de texto desde PDF
# -----------------------------------------------------------------------------


def extract_pdf_pages(path: Path) -> list[str]:
    """
    Extrae texto por página desde un PDF.

    El script intenta primero con pypdf por ser una dependencia liviana. Si pypdf
    no está disponible o falla, intenta con PyMuPDF. Si ninguna biblioteca está
    instalada, se emite un error operativo con instrucciones claras.
    """

    try:
        from pypdf import PdfReader  # type: ignore

        reader = PdfReader(str(path))
        pages = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")
        return pages
    except Exception as first_error:
        try:
            import fitz  # type: ignore

            document = fitz.open(str(path))
            pages = [page.get_text("text") or "" for page in document]
            document.close()
            return pages
        except Exception as second_error:
            raise RuntimeError(
                "No se pudo extraer texto del PDF. Se requiere instalar pypdf "
                "o PyMuPDF. Comandos sugeridos: pip install pypdf o pip install pymupdf. "
                f"Primer error: {first_error}. Segundo error: {second_error}."
            ) from second_error


# -----------------------------------------------------------------------------
# Localización de documentos fuente
# -----------------------------------------------------------------------------


def find_source_documents(external_dir: Path) -> dict[str, Path]:
    """
    Localiza documentos fuente esperados dentro del directorio externo.

    La búsqueda se basa en patrones flexibles. Si un documento no se encuentra,
    el script continúa con los documentos disponibles y registra la advertencia.
    """

    found: dict[str, Path] = {}
    for doc_id, patterns in DEFAULT_SOURCE_PATTERNS.items():
        matches: list[Path] = []
        for pattern in patterns:
            matches.extend(sorted(external_dir.glob(pattern)))

        unique_matches = []
        seen = set()
        for match in matches:
            resolved = match.resolve()
            if resolved not in seen and match.is_file():
                unique_matches.append(match)
                seen.add(resolved)

        if unique_matches:
            found[doc_id] = unique_matches[0]

    return found



def infer_document_title(doc_id: str, path: Path) -> str:
    """Asigna un título documental normalizado a partir del identificador."""

    if doc_id == "arancel_2022":
        return "Arancel de Aduanas 2022"
    if doc_id == "nandina_decision_885":
        return "CAN Decisión 885 - Nomenclatura Común NANDINA"
    return path.stem


# -----------------------------------------------------------------------------
# Segmentación y enriquecimiento de metadatos
# -----------------------------------------------------------------------------


def split_page_into_blocks(text: str, min_chars: int = 80, max_chars: int = 1800) -> list[str]:
    """
    Segmenta una página en bloques recuperables.

    La estrategia inicial usa separación por párrafos y acumulación controlada.
    Esta decisión privilegia fragmentos suficientemente informativos para BM25,
    recuperación vectorial y RAG, sin perder trazabilidad por página.
    """

    cleaned = clean_pdf_header_footer(text)
    if not cleaned:
        return []

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", cleaned) if p.strip()]

    # Cuando el PDF no contiene saltos de párrafo confiables, se usa una división
    # por líneas con acumulación posterior.
    if len(paragraphs) <= 1:
        paragraphs = [p.strip() for p in cleaned.splitlines() if p.strip()]

    blocks: list[str] = []
    current: list[str] = []
    current_len = 0

    for paragraph in paragraphs:
        paragraph_len = len(paragraph)

        if current and current_len + paragraph_len > max_chars:
            blocks.append(normalize_text("\n".join(current)))
            current = []
            current_len = 0

        current.append(paragraph)
        current_len += paragraph_len

        if current_len >= min_chars and paragraph.endswith((".", ":", ";")):
            blocks.append(normalize_text("\n".join(current)))
            current = []
            current_len = 0

    if current:
        final_block = normalize_text("\n".join(current))
        if final_block:
            blocks.append(final_block)

    # Los bloques demasiado breves se conservan solo cuando contienen códigos o
    # encabezados normativos útiles.
    filtered_blocks = []
    for block in blocks:
        if len(block) >= min_chars or detect_code(block) or detect_fragment_type(block) in {
            "titulo_seccion",
            "titulo_capitulo",
            "regla_general",
        }:
            filtered_blocks.append(block)

    return filtered_blocks



def detect_code(text: str) -> Optional[str]:
    """
    Detecta el primer código arancelario visible en un fragmento.

    La detección cubre patrones de 2, 4, 6, 8 y 10 dígitos escritos con o sin
    puntos. El valor devuelto conserva la forma encontrada en el texto.
    """

    patterns = [
        r"\b\d{4}\.\d{2}\.\d{2}\.\d{2}\b",  # 10 dígitos con puntos
        r"\b\d{4}\.\d{2}\.\d{2}\b",  # 8 dígitos con puntos
        r"\b\d{4}\.\d{2}\b",  # 6 dígitos con punto
        r"\b\d{8}\b",
        r"\b\d{6}\b",
        r"\b\d{4}\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(0)
    return None



def normalize_code_digits(code: Optional[str]) -> Optional[str]:
    """Convierte un código detectado a solo dígitos."""

    if not code:
        return None
    digits = re.sub(r"\D", "", code)
    return digits or None



def infer_hierarchy_from_text(text: str) -> tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
    """
    Infere sección, capítulo, partida y subpartida desde el texto del fragmento.

    Esta inferencia es preliminar. La versión v0.1 no reemplaza una segmentación
    normativa experta; solo agrega metadatos útiles para inspección e indexación.
    """

    seccion = None
    capitulo = None
    partida = None
    subpartida = None

    section_match = re.search(r"\bSECCI[ÓO]N\s+([IVXLCDM]+|\d+)\b", text, flags=re.IGNORECASE)
    if section_match:
        seccion = section_match.group(0).strip()

    chapter_match = re.search(r"\bCap[íi]tulo\s+(\d{1,2})\b", text, flags=re.IGNORECASE)
    if chapter_match:
        capitulo = chapter_match.group(1).zfill(2)

    code = normalize_code_digits(detect_code(text))
    if code:
        if len(code) >= 4:
            partida = code[:4]
        if len(code) >= 8:
            subpartida = code[:8]

    # También se detectan encabezados de partida con punto: 01.01, 84.71, etc.
    heading_match = re.search(r"\b(\d{2})\.(\d{2})\b", text)
    if heading_match and not partida:
        partida = f"{heading_match.group(1)}{heading_match.group(2)}"
        if not capitulo:
            capitulo = heading_match.group(1)

    if partida and not capitulo:
        capitulo = partida[:2]

    return seccion, capitulo, partida, subpartida



def detect_fragment_type(text: str) -> str:
    """
    Clasifica de manera heurística el tipo de fragmento documental.

    Los tipos permiten filtrar y evaluar el comportamiento del recuperador por
    clase de evidencia normativa.
    """

    normalized = text.strip().upper()

    if re.search(r"REGLAS GENERALES PARA LA INTERPRETACI[ÓO]N", normalized):
        return "regla_general_titulo"
    if re.match(r"^[1-6]\.?\s+", normalized) and "CLASIFIC" in normalized:
        return "regla_general"
    if "CONSIDERACIONES GENERALES" in normalized:
        return "consideracion_general"
    if "CONSIDERACIONES SOBRE EL ARANCEL" in normalized:
        return "consideracion_arancel"
    if re.search(r"^SECCI[ÓO]N\s+", normalized):
        return "titulo_seccion"
    if re.search(r"CAP[ÍI]TULO\s+\d+", normalized):
        return "titulo_capitulo"
    if "NOTA COMPLEMENTARIA" in normalized:
        return "nota_complementaria"
    if re.search(r"\bNOTAS?\b", normalized):
        return "nota"
    if detect_code(text):
        return "descripcion_arancelaria"
    return "texto_normativo"



def build_chunks_for_document(doc_id: str, title: str, path: Path, pages: list[str]) -> list[CorpusChunk]:
    """Construye fragmentos recuperables para un documento fuente."""

    chunks: list[CorpusChunk] = []
    for page_index, raw_page_text in enumerate(pages, start=1):
        blocks = split_page_into_blocks(raw_page_text)
        for block_index, block in enumerate(blocks, start=1):
            seccion, capitulo, partida, subpartida = infer_hierarchy_from_text(block)
            code = detect_code(block)
            chunk_id = f"{doc_id}_{CORPUS_VERSION.replace('.', '')}_p{page_index:04d}_b{block_index:03d}"
            chunks.append(
                CorpusChunk(
                    chunk_id=chunk_id,
                    version_corpus=CORPUS_VERSION,
                    doc_id=doc_id,
                    titulo_documento=title,
                    ruta_archivo_origen=str(path.as_posix()),
                    nombre_archivo=path.name,
                    pagina=page_index,
                    bloque_en_pagina=block_index,
                    tipo_fragmento=detect_fragment_type(block),
                    seccion=seccion,
                    capitulo=capitulo,
                    partida=partida,
                    subpartida=subpartida,
                    codigo_detectado=code,
                    texto_fragmento=block,
                    longitud_caracteres=len(block),
                    hash_texto_sha256=calculate_text_sha256(block),
                )
            )
    return chunks


# -----------------------------------------------------------------------------
# Exportación de artefactos
# -----------------------------------------------------------------------------


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    """Escribe una colección de diccionarios en formato JSONL UTF-8."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file_obj:
        for row in rows:
            file_obj.write(json.dumps(row, ensure_ascii=False) + "\n")



def write_csv(path: Path, rows: list[DocumentRecord]) -> None:
    """Escribe el inventario documental en formato CSV."""

    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(asdict(rows[0]).keys()) if rows else [
        "doc_id",
        "titulo_documento",
        "ruta_archivo_origen",
        "nombre_archivo",
        "extension",
        "hash_sha256",
        "tamano_bytes",
        "version_corpus",
        "fecha_procesamiento_utc",
        "paginas_extraidas",
        "caracteres_extraidos",
        "observaciones",
    ]
    with path.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))



def generate_report(
    output_path: Path,
    document_records: list[DocumentRecord],
    chunks: list[CorpusChunk],
    missing_doc_ids: list[str],
    generated_at: str,
) -> None:
    """Genera un reporte Markdown de la corrida de construcción del corpus."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    chunks_by_doc: dict[str, int] = {}
    chunks_by_type: dict[str, int] = {}
    for chunk in chunks:
        chunks_by_doc[chunk.doc_id] = chunks_by_doc.get(chunk.doc_id, 0) + 1
        chunks_by_type[chunk.tipo_fragmento] = chunks_by_type.get(chunk.tipo_fragmento, 0) + 1

    lines = [
        f"# Reporte de generación del corpus {CORPUS_VERSION}",
        "",
        f"- **Fecha de generación UTC:** {generated_at}",
        f"- **Documentos procesados:** {len(document_records)}",
        f"- **Fragmentos generados:** {len(chunks)}",
        f"- **Documentos esperados no localizados:** {', '.join(missing_doc_ids) if missing_doc_ids else 'Ninguno'}",
        "",
        "## Documentos procesados",
        "",
        "| doc_id | Archivo | Páginas | Caracteres | SHA-256 | Observaciones |",
        "|---|---|---:|---:|---|---|",
    ]

    for record in document_records:
        lines.append(
            f"| `{record.doc_id}` | `{record.nombre_archivo}` | {record.paginas_extraidas} | "
            f"{record.caracteres_extraidos} | `{record.hash_sha256[:12]}...` | {record.observaciones} |"
        )

    lines.extend([
        "",
        "## Fragmentos por documento",
        "",
        "| doc_id | Fragmentos |",
        "|---|---:|",
    ])

    for doc_id, count in sorted(chunks_by_doc.items()):
        lines.append(f"| `{doc_id}` | {count} |")

    lines.extend([
        "",
        "## Fragmentos por tipo",
        "",
        "| tipo_fragmento | Fragmentos |",
        "|---|---:|",
    ])

    for fragment_type, count in sorted(chunks_by_type.items()):
        lines.append(f"| `{fragment_type}` | {count} |")

    lines.extend([
        "",
        "## Archivos generados",
        "",
        f"- `corpus_chunks_{CORPUS_VERSION}.jsonl`",
        f"- `corpus_documents_{CORPUS_VERSION}.csv`",
        f"- `corpus_generation_report_{CORPUS_VERSION}.md`",
        "",
        "## Observaciones metodológicas",
        "",
        "La segmentación de esta versión es heurística y debe validarse mediante inspección manual de una muestra de fragmentos. "
        "La versión v0.1 prioriza trazabilidad, reproducibilidad y disponibilidad de una primera base recuperable. "
        "No constituye una interpretación oficial de la NANDINA ni del Arancel de Aduanas.",
        "",
        "## Próximos controles recomendados",
        "",
        "- Verificar manualmente fragmentos de reglas generales, notas y subpartidas.",
        "- Confirmar que los códigos NANDINA de ocho dígitos se preserven correctamente.",
        "- Revisar errores de extracción en tablas extensas del PDF.",
        "- Ajustar reglas de segmentación antes de construir índices BM25 o vectoriales definitivos.",
    ])

    output_path.write_text("\n".join(lines), encoding="utf-8")


# -----------------------------------------------------------------------------
# Orquestación principal
# -----------------------------------------------------------------------------


def build_corpus(external_dir: Path, output_dir: Path) -> tuple[list[DocumentRecord], list[CorpusChunk], list[str]]:
    """Ejecuta el proceso completo de construcción del corpus documental."""

    if not external_dir.exists():
        raise FileNotFoundError(f"No existe el directorio de documentos fuente: {external_dir}")

    generated_at = utc_now_iso()
    source_documents = find_source_documents(external_dir)
    missing_doc_ids = [doc_id for doc_id in DEFAULT_SOURCE_PATTERNS if doc_id not in source_documents]

    document_records: list[DocumentRecord] = []
    all_chunks: list[CorpusChunk] = []

    for doc_id, path in source_documents.items():
        title = infer_document_title(doc_id, path)
        pages = extract_pdf_pages(path)
        normalized_pages = [normalize_text(page) for page in pages]
        characters = sum(len(page) for page in normalized_pages)
        chunks = build_chunks_for_document(doc_id, title, path, normalized_pages)

        document_records.append(
            DocumentRecord(
                doc_id=doc_id,
                titulo_documento=title,
                ruta_archivo_origen=str(path.as_posix()),
                nombre_archivo=path.name,
                extension=path.suffix.lower(),
                hash_sha256=calculate_file_sha256(path),
                tamano_bytes=path.stat().st_size,
                version_corpus=CORPUS_VERSION,
                fecha_procesamiento_utc=generated_at,
                paginas_extraidas=len(pages),
                caracteres_extraidos=characters,
                observaciones="procesado correctamente" if chunks else "procesado sin fragmentos útiles",
            )
        )
        all_chunks.extend(chunks)

    output_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(output_dir / f"corpus_chunks_{CORPUS_VERSION}.jsonl", (asdict(chunk) for chunk in all_chunks))
    write_csv(output_dir / f"corpus_documents_{CORPUS_VERSION}.csv", document_records)
    generate_report(
        output_path=output_dir / f"corpus_generation_report_{CORPUS_VERSION}.md",
        document_records=document_records,
        chunks=all_chunks,
        missing_doc_ids=missing_doc_ids,
        generated_at=generated_at,
    )

    return document_records, all_chunks, missing_doc_ids



def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    """Procesa argumentos de línea de comandos."""

    parser = argparse.ArgumentParser(
        description="Genera el corpus documental NANDINA-Arancel v0.1 desde PDFs ubicados en data/external."
    )
    parser.add_argument(
        "--external-dir",
        type=Path,
        default=DEFAULT_EXTERNAL_DIR,
        help="Directorio donde se encuentran los documentos PDF fuente.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directorio donde se guardarán los artefactos procesados del corpus.",
    )
    return parser.parse_args(argv)



def main(argv: Optional[list[str]] = None) -> int:
    """Punto de entrada del script."""

    args = parse_args(argv)
    try:
        document_records, chunks, missing_doc_ids = build_corpus(args.external_dir, args.output_dir)
    except Exception as error:
        print(f"[ERROR] No se pudo generar el corpus: {error}", file=sys.stderr)
        return 1

    print("[OK] Corpus generado correctamente.")
    print(f"[OK] Documentos procesados: {len(document_records)}")
    print(f"[OK] Fragmentos generados: {len(chunks)}")
    if missing_doc_ids:
        print(f"[WARN] Documentos esperados no localizados: {', '.join(missing_doc_ids)}")
    print(f"[OK] Salidas en: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
