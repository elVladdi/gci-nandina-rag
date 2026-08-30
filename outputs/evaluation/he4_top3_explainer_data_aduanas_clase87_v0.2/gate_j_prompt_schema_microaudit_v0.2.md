# Gate J microcierre: compatibilidad prompt-schema-validador HE4 v0.2

## Dictamen

- Clasificacion: `PROMPT-SCHEMA SPECIFICATION MISMATCH`.
- El prompt v0.2 no solicita `advertencias_globales`; el schema v0.2 si lo exige.
- El campo aparece en el prompt v0.3, no en la estructura exacta usada por Fase I.
- `0/50` se preserva como cumplimiento contra schema congelado y queda confounded por el mismatch.
- Solo por ese campo: `50/50`; otros schema errors: `0/50`.

## Advertencias

- `warnings_field_valid`: `50/50`.
- `generic_normative_warning_when_required`: `41/50`.
- Fallos del control generico: `9`; solapamiento: `0`.
- `INVALID_WARNING_FIELD` se conserva como etiqueta original; su interpretacion derivada para esos fallos es `MISSING_GENERIC_NORMATIVE_WARNING`.

## Fase K

- La rubrica no contiene `advertencias_globales` como dimension ni hard constraint; no se aplico.
- Gate J permanece `APPROVED WITH PROTOCOL/SPECIFICATION LIMITATION`; Fase K no se inicio.
