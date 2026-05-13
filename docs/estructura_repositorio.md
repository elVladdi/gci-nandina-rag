# Estructura del repositorio

El repositorio se organiza para separar datos, código, documentación y resultados del piloto experimental offline.

```text
.
├── data/
│   ├── raw/          # Datos fuente locales; no subir datos sensibles
│   ├── interim/      # Datos intermedios generados durante procesamiento
│   ├── processed/    # Datos procesados listos para evaluación
│   └── external/     # Recursos externos permitidos o referencias públicas
├── docs/             # Documentación metodológica y técnica
├── indexes/          # Índices de recuperación generados localmente
├── models/           # Modelos o artefactos locales no versionados
├── notebooks/        # Cuadernos de exploración y validación
├── outputs/          # Salidas experimentales, métricas y reportes
└── src/              # Código fuente del pipeline
```

## Criterios de organización

- Los datos sensibles, confidenciales o no autorizados no deben subirse al repositorio.
- Las carpetas `data/`, `outputs/`, `models/` e `indexes/` deben contener solo archivos `.gitkeep` o documentación, salvo que los artefactos sean públicos, livianos y autorizados.
- Cada corrida experimental debe registrar configuración, versión del corpus, parámetros, prompts y salidas.
- Los notebooks deben ser usados para validación y exploración; el código reutilizable debe migrarse a `src/`.
