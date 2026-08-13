# Informe Final — Electrotecnia Industrial

**Repositorio:** https://github.com/KyonX1/Electro (rama `main`)
**Fecha:** 2026-08-13

## Resumen del proyecto

Libro de texto de **electrotecnia industrial** en español, nivel intermedio-avanzado (C/D), con estilo profesional tipo Boylestad/Alexander-Sadiku: fórmulas limpias, tablas elegantes y diagramas ASCII.

**Resultado final: `electrotecnia.pdf` — 89 páginas A4, verificado y aprobado.**

## Contenido del libro

| Capítulo | Archivo | Contenido |
|---|---|---|
| 1 | `01-fundamentos.md` | Fundamentos de electrotecnia (carga, campo, potencial, Ohm, Kirchhoff, transitorios, fasores, potencia, Fourier) |
| 2 | `02-corriente-directa.md` | Corriente directa (series/paralelo, Thévenin, Norton, mallas, nodos, capacitores, inductores, instrumentación) |
| 3 | `03-corriente-alterna.md` | Corriente alterna (fasores, impedancia, potencia, resonancia, trifásica, filtros, Fourier) |
| 4 | `04-maquinas.md` | Máquinas eléctricas (transformadores, CC, síncronas, inducción) |
| 5 | `05-instalaciones.md` | Instalaciones eléctricas (normativa IEC 60364 y RETIE, protecciones, puesta a tierra, locales especiales) |
| 6 | `06-ejercicios.md` | **31 ejercicios resueltos** (E1.1–E6.4) y propuestos, con código Python verificable |
| 7 | `07-apendice.md` | Apéndice: tablas maestras (resistividades, secciones IEC, colores, símbolos, constantes, fórmulas) |

## Características de calidad

- **8 diagramas ASCII** (graph-easy) en `diagrams/`: serie-paralelo, divisor de voltaje, fasor RLC, triángulo de potencias, estrella-delta, transformador, motor CC, puesta a tierra
- **63 bloques de código Python** ejecutables y autocontenidos (todos verificados con `exec()`)
- **Tablas validadas** automáticamente (`validate_md.py`)
- **Bibliografía IEEE** global (`[1]`–`[5]`) al final del PDF
- **0 caracteres faltantes**, **0 errores de LaTeX**, numeración de capítulos correcta (1–7)

## Proceso de desarrollo

Desarrollo dirigido por subagentes (plan de 11 tareas) con revisión por pares en cada tarea:

1. Scaffold del repositorio
2. Capítulo 1: Fundamentos
3. Capítulo 2: Corriente directa
4. Capítulo 3: Corriente alterna
5. Capítulo 4: Máquinas eléctricas
6. Capítulo 5: Instalaciones eléctricas
7. Capítulo 6: Ejercicios resueltos (ampliado a 31 tras revisión)
8. Capítulo 7: Apéndice (fórmula de tensión de fase corregida tras revisión)
9. Diagramas ASCII + bloques Python autocontenidos
10. Compilación del PDF (pandoc 2.9 + xelatex + pandoc-citeproc) y verificación
11. Publicación en GitHub

## Cómo generar el PDF

```bash
./build.sh
```

Requisitos: pandoc + pandoc-citeproc, xelatex, fuentes DejaVu.

## Verificación

```bash
python3 validate_md.py   # valida estructura de capítulos
python3 verify_pdf.py electrotecnia.pdf   # valida el PDF generado
```

## Historial de git

- Rama `main`: libro final (último commit `6e10081`)
- Rama `legacy-pre-plan`: versión anterior del proyecto preservada
