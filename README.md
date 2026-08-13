# Electrotecnia Industrial

Libro de texto de electrotecnia industrial (nivel intermedio-avanzado, C/D) en español: fundamentos, corriente directa y alterna, máquinas eléctricas, instalaciones, 31 ejercicios resueltos y apéndice de tablas.

## Estructura

| Archivo | Contenido |
|---|---|
| `00-portada.md` | Portada |
| `01-fundamentos.md` | Fundamentos de electrotecnia |
| `02-corriente-directa.md` | Corriente directa |
| `03-corriente-alterna.md` | Corriente alterna |
| `04-maquinas.md` | Máquinas eléctricas |
| `05-instalaciones.md` | Instalaciones eléctricas |
| `06-ejercicios.md` | Ejercicios resueltos y propuestos (31) |
| `07-apendice.md` | Apéndice: tablas, constantes y fórmulas |
| `diagrams/` | Diagramas ASCII (graph-easy) |
| `build.sh` | Genera `electrotecnia.pdf` |
| `electrotecnia.pdf` | PDF generado (89 páginas A4) |

## Generar el PDF

```bash
./build.sh
```

Requiere: pandoc (con pandoc-citeproc), xelatex, DejaVu fonts.

## Validación

- `validate_md.py`: valida estructura de tablas y bloques de código de los capítulos
- `verify_pdf.py`: verifica el PDF generado

## Licencia

CC BY-SA 4.0
