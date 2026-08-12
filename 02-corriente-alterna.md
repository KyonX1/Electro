# 02 — Corriente Alterna (CA / AC)

> Todo sobre circuitos de corriente alterna: desde la onda sinusoidal hasta transformadores trifásicos.
> 39 temas, cada uno con definición, fórmula, ejemplo y verificación.

---

## Índice

1. [¿Qué es la corriente alterna?](#1--qué-es-la-corriente-alterna)
2. [Forma de onda sinusoidal](#2--forma-de-onda-sinusoidal)
3. [Frecuencia, periodo y longitud de onda](#3--frecuencia-periodo-y-longitud-de-onda)
4. [Voltajes: pico, RMS, medio](#4--voltajes-pico-rms-medio)
5. [Fasores](#5--fasores-y-representación-rotatoria)
6. [Reactancia inductiva X_L](#6--reactancia-inductiva-x_l)
7. [Reactancia capacitiva X_C](#7--reactancia-capacitiva-x_c)
8. [Impedancia Z](#8--impedancia-z)
9. [Circuito serie R-L](#9--circuito-serie-r-l)
10. [Circuito serie R-C](#10--circuito-serie-r-c)
11. [Circuito serie R-L-C](#11--circuito-serie-r-l-c)
12. [Circuito paralelo R-L](#12--circuito-paralelo-r-l)
13. [Circuito paralelo R-C](#13--circuito-paralelo-r-c)
14. [Circuito paralelo R-L-C](#14--circuito-paralelo-r-l-c)
15. [Serie-paralelo en CA](#15--circuits-serie-paralelo-en-ca)
16. [Potencia: activa, reactiva, aparente](#16--potencia-en-ca-activa-reactiva-aparente)
17. [Factor de potencia](#17--factor-de-potencia)
18. [Corrección del FP](#18--corrección-del-factor-de-potencia)
19. [Resonancia en serie](#19--resonancia-en-serie)
20. [Resonancia en paralelo](#20--resonancia-en-paralelo)
21. [Factor de calidad Q](#21--factor-de-calidad-q)
22. [Mallas en CA](#22--análisis-de-mallas-en-ca)
23. [Nodos en CA](#23--análisis-de-nodos-en-ca)
24. [Thevenin/Norton en CA](#24--thevenin-y-norton-en-ca)
25. [Sistemas trifásicos](#25--sistemas-trifásicos-equilibrados)
26. [Conexión estrella Y](#26--conexión-estrella-y)
27. [Conexión triángulo Δ](#27--conexión-triángulo-δ)
28. [Relación línea-fase](#28--relación-línea-fase)
29. [Potencia trifásica](#29--potencia-en-sistemas-trifásicos)
30. [Secuencia de fases](#30--secuencia-de-fases)
31. [Trifásico desequilibrado](#31--circuitos-trifásicos-desequilibrados)
32. [Transformadores: principio](#32--transformadores-principio)
33. [Ideal vs real](#33--transformador-ideal-vs-real)
34. [Ensayos OC y CC](#34--ensayos-de-circuito-abierto-y-cortocircuito)
35. [Eficiencia y regulación](#35--eficiencia-y-regulación)
36. [Transformadores trifásicos](#36--transformadores-trifásicos)
37. [Autotransformadores](#37--autotransformadores)
38. [Armónicos](#38--armónicos-y-distorsión)
39. [Filtros](#39--filtros-eléctricos)

---

## 1. ¿Qué es la corriente alterna?

La corriente alterna (CA) es aquella cuya **magnitud y dirección cambian periódicamente**. A diferencia de la CD (dirección constante), la CA oscila entre valores positivos y negativos.

### ¿Por qué se usa?

- **Transporte eficiente**: se transforma a altos voltajes para largas distancias con mínimas pérdidas
- **Motores simples**: los motores de inducción (los más usados en la industria) solo funcionan con CA
- **Generación natural**: los generadores rotativos producen CA naturalmente
- **Red mundial**: toda la infraestructura eléctrica está basada en CA

### Diferencia con CD

| **Característica** | **CD** | **CA** |
|----------------|----|----|
| Dirección | Constante | Cambia periódicamente |
| Magnitud | Puede ser constante | Varía con el tiempo |
| Transformación | No se transforma directamente | Se transforma con transformadores |
| Distribución | Ineficiente a larga distancia | Muy eficiente |
| Motores | Escobillas (DC) | Inducción, sin escobillas |
---

## 2. Forma de onda sinusoidal

La forma de onda sinusoidal es la forma natural de la CA generada por un alternador.

### Fórmula general

```
v(t) = V_max × sin(ωt + φ)

  v(t) = voltaje instantáneo (V)
  V_max = amplitud o valor pico (V)
  ω = frecuencia angular (rad/s)
  t = tiempo (s)
  φ = ángulo de fase inicial
```

### Anatomía de la onda

```
      V_max
       ↑
| ╭──╮ 
| ╱    ╲ 
  ─────┼──╱──────╲────────→ t
| ╱        ╲    ╱ 
| ╱          ╲  ╱ 
       ↓            ╲╱
                    -V_max
| ←── Un ciclo ──→ |
```

- **Cresta**: punto máximo = +V_max
- **Valle**: punto mínimo = -V_max
- **Cruce por cero**: v(t) = 0

### Analogía

Una rueda girando a velocidad constante. La altura de un punto en la rueda, proyectada contra una pared, traza una onda seno. La sinusoidal es la **proyección de un movimiento circular**.

---

## 3. Frecuencia, periodo y longitud de onda

### Frecuencia (f)

Número de ciclos completos por segundo. Se mide en Hertz (Hz).

```
f = 1/T    [Hz]
```

### Periodo (T)

Tiempo que tarda un ciclo completo.

```
T = 1/f    [s]
```

### Frecuencia angular (ω)

```
ω = 2π × f    [rad/s]
```

### Longitud de onda (λ)

Distancia espacial que recorre la onda en un ciclo:

```
λ = v / f    [m]
```

En cables eléctricos, v ≈ 2 × 10⁸ m/s (2/3 de la velocidad de la luz).

### Frecuencias estándar

| **País/Región** | **Frecuencia** | **Uso** |
|-------------|------------|-----|
| América | 60 Hz | Iluminación, motores |
| Europa, África | 50 Hz | Iluminación, motores |
| Aviación | 400 Hz | Sistemas aeronáuticos |
| Audio | 20-20,000 Hz | Sonido |
### Ejemplo

*Red eléctrica a 60 Hz:*

```
T = 1/60 = 0.01667 s = 16.67 ms
ω = 2π × 60 = 377 rad/s
```

---

## 4. Voltajes: pico, RMS, medio

### Valor pico (V_max)

El valor máximo absoluto de la onda. Es la amplitud.

### Valor RMS (V_rms) — EL MÁS IMPORTANTE

El valor efectivo. Es el voltaje de CD que produciría la **misma potencia** en una resistencia.

```
V_rms = V_max / √2 ≈ 0.7071 × V_max
V_max = V_rms × √2 ≈ 1.4142 × V_rms
```

> **Este es el valor que mide un multímetro y el que aparece en las especificaciones.**

### Valor medio (V_medio)

Promedio en medio ciclo (para rectificadores):

```
V_medio = (2/π) × V_max ≈ 0.637 × V_max
```

### Valor pico a pico (V_pp)

```
V_pp = 2 × V_max
```

### Tabla resumen

| **Valor** | **Fórmula** | **Factor con V_max** |
|-------|---------|-------------------|
| V_max (pico) | V_max | ×1 |
| V_rms (efectivo) | V_max/√2 | ×0.707 |
| V_medio | 2V_max/π | ×0.637 |
| V_pp (pico a pico) | 2×V_max | ×2 |
### Ejemplo

*Toma doméstica 120V RMS a 60 Hz:*

```
V_max = 120 × 1.414 = 169.7 V
V_medio = 0.637 × 169.7 = 108.1 V
V_pp = 2 × 169.7 = 339.4 V
```

### ⚠️ Error común

Confundir RMS con pico. Un multímetro muestra RMS. Si ves "310V" en un multímetro, el pico es 310 × √2 ≈ 438V.

---

## 5. Fasores y representación rotatoria

### ¿Qué es un fasor?

Representación vectorial de una magnitud sinusoidal. Convierte ecuaciones diferenciales en **álgebra con números complejos**.

```
Forma rectangular:  V̂ = a + jb
Forma polar:        V̂ = |V| ∠ φ
Forma exponencial:  V̂ = |V| × e^(jφ)
```

### Conversión

```
Polar → Rectangular:
  a = |V| × cos(φ)
  b = |V| × sin(φ)

Rectangular → Polar:
| V | = √(a² + b²) 
  φ = arctan(b/a)
```

### Operaciones

```
Suma/resta:     Se suman componente a componente (rectangular)
Multiplicación: Se multiplican magnitudes, se suman ángulos (polar)
División:       Se dividen magnitudes, se restan ángulos (polar)
```

### Regla ELI-ICE

- **ELI**: En un inductor (L), el voltaje (E) **adelanta** a la corriente (I)
- **ICE**: En un capacitor (C), la corriente (I) **adelanta** al voltaje (E)

### Ejemplo

*V₁ = 100∠30° + V₂ = 80∠-20°:*

```
V₁ = 100(cos30° + j sin30°) = 86.6 + j50
V₂ = 80(cos(-20°) + j sin(-20°)) = 75.18 - j27.36

V₁ + V₂ = (86.6 + 75.18) + j(50 - 27.36)
         = 161.78 + j22.64

En polar: |V| = √(161.78² + 22.64²) = 163.36 V
          φ = arctan(22.64/161.78) = 7.95°

Resultado: V₁ + V₂ = 163.36 ∠ 7.95° V
```

---

## 6. Reactancia inductiva (X_L)

La **oposición** que un inductor presenta al paso de CA. No disipa energía (la almacena y devuelve).

```
X_L = ω × L = 2π × f × L    [Ω]
```

| **Frecuencia** | **X_L** | **Efecto** |
|------------|-----|--------|
| f = 0 (CD) | 0 | Cortocircuito |
| f baja | Pequeña | Poca oposición |
| f alta | Grande | Mucha oposición |
> Un inductor **pasa CD** y **bloquea CA de alta frecuencia**.

### Ejemplo

*L = 0.5H a 60Hz:*

```
X_L = 2π × 60 × 0.5 = 188.5 Ω
```

---

## 7. Reactancia capacitiva (X_C)

La **oposición** que un capacitor presenta al paso de CA.

```
X_C = 1 / (ω × C) = 1 / (2π × f × C)    [Ω]
```

| **Frecuencia** | **X_C** | **Efecto** |
|------------|-----|--------|
| f = 0 (CD) | ∞ | Circuito abierto |
| f baja | Grande | Mucha oposición |
| f alta | Pequeña | Poca oposición |
> Un capacitor **bloquea CD** y **pasa CA de alta frecuencia**.

### Ejemplo

*C = 10μF a 60Hz:*

```
X_C = 1/(2π × 60 × 10×10⁻⁶) = 265.3 Ω
```

---

## 8. Impedancia (Z)

La **oposición total** al paso de CA. Generalización de la resistencia para CA.

```
Z = R + jX    donde X = X_L - X_C

| Z | = √(R² + X²)    (magnitud) 
φ = arctan(X/R)       (ángulo)
```

### La Ohm Generalizada

```
V̂ = Î × Z
| V | = | I | × | Z |
```

### Ejemplo

*R = 30Ω, X_L = 40Ω, X_C = 10Ω:*

```
X = 40 - 10 = 30Ω
Z = 30 + j30 = 42.43 ∠ 45° Ω

Si V = 120∠0°:
I = V/Z = 120∠0° / 42.43∠45° = 2.828 ∠ -45° A
```

La corriente **retrasa** 45° respecto al voltaje (circuito inductivo).

---

## 9. Circuito serie R-L

```
Z = R + jX_L
| Z | = √(R² + X_L²) 
φ = arctan(X_L / R)

V_total = √(V_R² + V_L²)  ← NUNCA es la suma aritmética
```

### Ejemplo

*R = 100Ω, L = 0.2H, f = 60Hz, V = 120V:*

```
X_L = 2π × 60 × 0.2 = 75.4Ω
| Z | = √(100² + 75.4²) = 125.2Ω 
I = 120/125.2 = 0.958A

V_R = 0.958 × 100 = 95.8V
V_L = 0.958 × 75.4 = 72.3V

Verificación: √(95.8² + 72.3²) = √(9178+5227) = 120V ✓
φ = arctan(75.4/100) = 37° (V adelanta a I)
```

---

## 10. Circuito serie R-C

```python
Z = R - jX_C
φ = -arctan(X_C / R)  (negativo: corriente adelanta)
```

### Ejemplo

*R = 200Ω, C = 10μF, f = 60Hz, V = 100V:*

```
X_C = 265.3Ω
| Z | = √(200² + 265.3²) = 332.2Ω 
I = 100/332.2 = 0.301A
φ = -53.1° (I adelanta a V)
```

---

## 11. Circuito serie R-L-C

```
Z = R + j(X_L - X_C)
| Z | = √(R² + (X_L - X_C)²) 
```

### Tres casos

| **Condición** | **φ** | **Comportamiento** |
|-----------|---|----------------|
| X_L > X_C | φ > 0 | Inductivo (V adelanta a I) |
| X_L < X_C | φ < 0 | Capacitivo (I adelanta a V) |
| X_L = X_C | φ = 0 | **Resonancia** (solo R) |
### En resonancia (X_L = X_C)

```python
Z = R (mínima)
I_max = V/R (máxima)
V_L = V_C >> V (pueden ser MUCHO mayores que la fuente)
```

### Ejemplo

*R = 50Ω, L = 0.1H, C = 100μF, f = 60Hz, V = 120V:*

```
X_L = 2π × 60 × 0.1 = 37.7Ω
X_C = 1/(2π × 60 × 100×10⁻⁶) = 26.5Ω
X = 37.7 - 26.5 = 11.2Ω (inductivo)

| Z | = √(50² + 11.2²) = 51.2Ω 
I = 120/51.2 = 2.344A
V_R = 117.2V, V_L = 88.4V, V_C = 62.1V
```

---

## 12. Circuito Paralelo R-L

En un circuito paralelo R-L, la resistencia y el inductor están conectados en **paralelo** sobre la misma fuente de voltaje. A diferencia del circuito serie, aquí cada componente recibe el **mismo voltaje**, pero las corrientes son diferentes.

### Fórmulas

```
I_R = V / R           (corriente por la resistencia, en fase con V)
I_L = V / X_L         (corriente por el inductor, retrasa 90° respecto a V)

I_total = √(I_R² + I_L²)    (suma fasorial, no aritmética)

φ = arctan(I_R / I_L)        (ángulo del circuito total)
```

> **Nota:** En paralelo, las corrientes se suman fasorialmente (como vectores perpendiculares), no directamente.

### Ejemplo

**Datos:** R = 30Ω, X_L = 40Ω, V = 120V

**Paso 1:** Calcular cada corriente

```
I_R = V / R = 120 / 30 = 4.00 A  (en fase con V)
I_L = V / X_L = 120 / 40 = 3.00 A  (retrasa 90° respecto a V)
```

**Paso 2:** Corriente total

```
I_total = √(I_R² + I_L²) = √(4² + 3²) = √(16 + 9) = √25 = 5.00 A
```

**Paso 3:** Ángulo de fase

```
φ = arctan(I_R / I_L) = arctan(4/3) = 53.13°
```

El ángulo φ representa cuánto **retrasa la corriente total** respecto al voltaje. Como el circuito es inductivo, la corriente total retrasa.

### Verificación

```
| Z | _equivalente = V / I_total = 120 / 5 = 24 Ω 
```

Verificación por impedancia equivalente en paralelo:
```
1/|Z| = √(1/R² + 1/X_L²) = √(1/900 + 1/1600) = √(0.001111 + 0.000625)
       = √(0.001736) = 0.04167 S  →  |Z| = 1/0.04167 = 24 Ω  ✓
```

---

## 13. Circuito Paralelo R-C

En un circuito paralelo R-C, la resistencia y el capacitor están en paralelo. La corriente por el capacitor **adelanta** 90° respecto al voltaje.

### Fórmulas

```
I_R = V / R           (en fase con V)
I_C = V / X_C         (adelanta 90° respecto a V)

I_total = √(I_R² + I_C²)

φ = arctan(I_C / I_R)   (adelantado: I total adelanta a V)
```

### Ejemplo

**Datos:** R = 150Ω, X_C = 200Ω, V = 120V

**Paso 1:** Corrientes individuales

```
I_R = 120 / 150 = 0.800 A  (en fase con V)
I_C = 120 / 200 = 0.600 A  (adelanta 90°)
```

**Paso 2:** Corriente total

```
I_total = √(I_R² + I_C²) = √(0.8² + 0.6²) = √(0.64 + 0.36) = √1.0 = 1.00 A
```

**Paso 3:** Ángulo de fase

```
φ = arctan(I_C / I_R) = arctan(0.6/0.8) = arctan(0.75) = 36.87°
```

La corriente total **adelanta** 36.87° al voltaje (circuito capacitivo).

### Verificación

```
| Z | = V / I_total = 120 / 1.0 = 120 Ω 
```

Por impedancia equivalente:
```
1/|Z| = √(1/R² + 1/X_C²) = √(1/22500 + 1/40000) = √(0.00004444 + 0.000025)
       = √(0.00006944) = 0.008333 S  →  |Z| = 120 Ω  ✓
```

---

## 14. Circuito Paralelo R-L-C

En un circuito paralelo R-L-C, los tres componentes están en paralelo. Las corrientes por L y C son opuestas (desfasadas 180° entre sí), por lo que se **restan** antes de combinarse con I_R.

### Fórmulas

```
I_R = V / R
I_L = V / X_L
I_C = V / X_C

I_total = √(I_R² + (I_C - I_L)²)
```

### Resonancia en paralelo

Cuando X_L = X_C → I_C = I_L, entonces:

```
I_C - I_L = 0  →  I_total = I_R (solo queda la resistiva)
```

En resonancia, la corriente total es **mínima** (igual a I_R) y la impedancia es **máxima**.

### Ejemplo

**Datos:** R = 100Ω, X_L = 50Ω, X_C = 80Ω, V = 200V

**Paso 1:** Corrientes individuales

```
I_R = 200 / 100 = 2.00 A
I_L = 200 / 50  = 4.00 A  (retrasa 90°)
I_C = 200 / 80  = 2.50 A  (adelanta 90°)
```

**Paso 2:** Diferencia I_C - I_L

```
I_C - I_L = 2.50 - 4.00 = -1.50 A
```

El signo negativo indica que el efecto inductivo domina (I_L > I_C).

**Paso 3:** Corriente total

```
I_total = √(I_R² + (I_C - I_L)²) = √(2² + (-1.5)²) = √(4 + 2.25) = √6.25 = 2.50 A
```

**Paso 4:** Ángulo de fase

```
φ = arctan((I_C - I_L) / I_R) = arctan(-1.5/2) = arctan(-0.75) = -36.87°
```

Negativo significa que el circuito es **inductivo** (la corriente total retrasa respecto al voltaje).

### Verificación

```
| Z | = V / I_total = 200 / 2.50 = 80 Ω 

Componentes de Z:
Z_R = 100Ω, Z_L = j50Ω, Z_C = -j80Ω

Admitancias:
Y_R = 1/100 = 0.01 S
Y_L = 1/(j50) = -j0.02 S
Y_C = 1/(-j80) = j0.0125 S

Y_total = 0.01 + j(0.0125 - 0.02) = 0.01 - j0.0075 S
| Y | = √(0.01² + 0.0075²) = √(0.0001 + 0.00005625) = 0.0125 S 
| Z | = 1/ | Y | = 80 Ω  ✓ 
```

---

## 15. Circuito Serie-Paralelo en CA

Los circuitos serie-paralelo combinan ambos tipos de conexión. La estrategia es **reducir subcircuitos paso a paso** usando números complejos.

### Estrategia de resolución

1. Identificar los subcircuitos en paralelo
2. Calcular la impedancia equivalente de cada subcircuito
3. Sumar en serie las impedancias que queden
4. Calcular corrientes y voltajes con la Ohm generalizada

### Ejemplo

**Datos:** Z₁ = 3 + j4Ω (serie), Z₂ = 6 - j8Ω (paralelo con Z₃), Z₃ = j5Ω

La configuración es: Z₁ en serie con (Z₂ ∥ Z₃)

**Paso 1:** Impedancia equivalente del paralelo Z₂ ∥ Z₃

```
Z₂ ∥ Z₃ = (Z₂ × Z₃) / (Z₂ + Z₃)

Z₂ × Z₃ = (6 - j8)(j5) = j30 - j²40 = 40 + j30

Z₂ + Z₃ = (6 - j8) + (j5) = 6 - j3

Z₂ ∥ Z₃ = (40 + j30) / (6 - j3)
```

Multiplicar por conjugado:
```
= (40 + j30)(6 + j3) / ((6 - j3)(6 + j3))
= (240 + j120 + j180 + j²90) / (36 + 9)
= (240 - 90 + j300) / 45
= (150 + j300) / 45
= 3.333 + j6.667 Ω
```

**Paso 2:** Impedancia total

```
Z_total = Z₁ + (Z₂ ∥ Z₃)
        = (3 + j4) + (3.333 + j6.667)
        = 6.333 + j10.667 Ω

| Z_total | = √(6.333² + 10.667²) = √(40.11 + 113.78) = √153.89 = 12.40 Ω 
φ = arctan(10.667/6.333) = 59.21°
```

**Paso 3:** Si V = 100∠0° V, corriente total

```
I_total = V / Z_total = 100∠0° / 12.40∠59.21° = 8.065 ∠ -59.21° A
```

### Verificación

```
V_Z₁ = I × Z₁ = 8.065∠-59.21° × 5∠53.13° = 40.33 ∠ -6.08° V
V_paralelo = I × Z_paralelo = 8.065∠-59.21° × 7.454∠63.43° = 60.12 ∠ 4.22° V

V_total = V_Z₁ + V_paralelo ≈ 100∠0° V  ✓
```

---

## 16. Potencia en Corriente Alterna

En CA existen **tres tipos de potencia**. La distinción es fundamental para el diseño y análisis de circuitos.

### Potencia Activa (P) — Watts

La potencia real que **consume** el circuito y se convierte en calor, movimiento, luz, etc.

```
P = V × I × cos(φ)    [Watts]
  = V × I × FP

donde cos(φ) = factor de potencia (FP)
```

### Potencia Reactiva (Q) — VAR

Potencia que **oscila** entre la fuente y los componentes reactivos (L y C). No se consume, pero necesita conductores más gruesos.

```
Q = V × I × sin(φ)    [VAR]
```

- Q > 0 → circuito inductivo
- Q < 0 → circuito capacitivo

### Potencia Aparente (S) — VA

El producto simple de voltaje y corriente RMS. Es la capacidad total que debe tener la infraestructura.

```
S = V × I    [VA]
```

### Triángulo de Potencia

```
        S (hipotenusa)
       /|
      / |
     /  | Q (vertical)
    /   |
   / φ  |
  /_____|
     P (horizontal)

S² = P² + Q²
FP = cos(φ) = P / S
```

### Ejemplo

**Datos:** Motor conectado a 120V, consume 5A, FP = 0.8 (atrasado)

**Paso 1:** Potencia aparente

```
S = V × I = 120 × 5 = 600 VA
```

**Paso 2:** Potencia activa

```
P = S × cos(φ) = 600 × 0.8 = 480 W
```

**Paso 3:** Potencia reactiva

```
cos(φ) = 0.8  →  φ = arccos(0.8) = 36.87°
sin(φ) = sin(36.87°) = 0.6

Q = S × sin(φ) = 600 × 0.6 = 360 VAR (inductivo)
```

**Paso 4:** Verificación

```
S = √(P² + Q²) = √(480² + 360²) = √(230400 + 129600) = √360000 = 600 VA  ✓
```

---

## 17. Factor de Potencia

El factor de potencia (FP) indica qué fracción de la potencia aparente se convierte en **potencia útil**.

### Definición

```
FP = cos(φ) = P / S
```

### Interpretación

```python
FP = 1.0  →  óptimo: toda la energía se usa productivamente
FP = 0.8  →  bueno: 80% se usa, 20% se pierde en oscilación
FP = 0.5  →  muy malo: solo 50% se usa
```

### Tabla de referencia

| **FP** | **Calificación** | **Acción requerida** |
|----|-------------|-----------------|
| > 0.95 | Excelente | Ninguna |
| 0.90 – 0.95 | Bueno | Monitorear |
| 0.80 – 0.90 | Aceptable | Considerar corrección |
| 0.70 – 0.80 | Regular | Corrección recomendada |
| 0.60 – 0.70 | Malo | Corrección urgente |
| < 0.60 | Crítico | Corrección inmediata |
### Causas de FP bajo

- **Motores de inducción** (el mayor causante): consumen mucha Q reactiva
- **Transformadores**: similares efectos
- **Arcos de soldadica**: alta distorsión + componente reactiva
- **Iluminación fluorescente** (sin compensar): condensadores internos

### Consecuencias de FP bajo

- **Multas** de las compañías eléctricas
- **Conductores sobrecalentados**: necesitan llevar más corriente
- **Transformadores sobredimensionados**
- **Caída de voltaje** mayor en líneas de transmisión

### Ejemplo de impacto

```python
Dos motores consumen P = 10 kW cada uno:

Motor A: FP = 0.95
  S_A = 10,000 / 0.95 = 10,526 VA → I_A = 10,526 / 230 = 45.8 A

Motor B: FP = 0.65
  S_B = 10,000 / 0.65 = 15,385 VA → I_B = 15,385 / 230 = 66.9 A

Motor B necesita un conductor 46% más grueso por la misma potencia útil.
```

---

## 18. Corrección del Factor de Potencia

La corrección más común es instalar un **banco de capacitores en paralelo** con el equipo de FP bajo. Los capacitores suministran la corriente reactiva que los motores consumen, reduciendo la carga sobre la fuente.

### Fórmula

```
C = P × (tan(φ₁) - tan(φ₂)) / (ω × V²)

donde:
  φ₁ = ángulo original (FP₁ = cos(φ₁))
  φ₂ = ángulo deseado (FP₂ = cos(φ₂))
  P = potencia activa (W)
  ω = 2πf (rad/s)
  V = voltaje de la fuente (V)
```

### Ejemplo

**Datos:** Motor de 10 kW, FP = 0.70 (atrasado), corregir a FP = 0.95. Fuente: 230V, 60Hz.

**Paso 1:** Ángulos

```
φ₁ = arccos(0.70) = 45.57°  →  tan(φ₁) = tan(45.57°) = 1.0202
φ₂ = arccos(0.95) = 18.19°  →  tan(φ₂) = tan(18.19°) = 0.3287
```

**Paso 2:** Frecuencia angular

```
ω = 2π × 60 = 377 rad/s
```

**Paso 3:** Capacitancia necesaria

```
C = 10,000 × (1.0202 - 0.3287) / (377 × 230²)
  = 10,000 × 0.6915 / (377 × 52,900)
  = 6915 / 19,943,300
  = 0.0003467 F
  = 346.7 μF
```

**Paso 4:** Verificación — corriente reactiva antes y después

```
Q_antes = P × tan(φ₁) = 10,000 × 1.0202 = 10,202 VAR
Q_después = P × tan(φ₂) = 10,000 × 0.3287 = 3,287 VAR
Q_C = Q_antes - Q_después = 10,202 - 3,287 = 6,915 VAR

I_C = Q_C / V = 6,915 / 230 = 30.07 A (corriente del banco)
X_C = V / I_C = 230 / 30.07 = 7.65 Ω
C = 1/(ω × X_C) = 1/(377 × 7.65) = 346.7 μF  ✓
```

---

## 19. Resonancia en Serie

La resonancia en serie ocurre cuando la **reactancia inductiva iguala a la capacitiva** (X_L = X_C). En este punto, las reacciones se cancelan y el circuito se comporta como puramente resistivo.

### Condición de resonancia

```
X_L = X_C
2πfL = 1/(2πfC)
```

### Frecuencia de resonancia

```
f₀ = 1 / (2π√(LC))    [Hz]
```

### En resonancia

```
Z = R (mínima)
I = V / R (máxima)
V_L = I × X_L  (puede ser MUCHO mayor que V)
V_C = I × X_C  (puede ser MUCHO mayor que V)
V_L + V_C = 0  (se cancelanfasorialmente)
```

### Ejemplo

**Datos:** L = 100 mH, C = 10 μF, R = 10Ω, V = 10V

**Paso 1:** Frecuencia de resonancia

```
f₀ = 1 / (2π√(0.1 × 10×10⁻⁶))
   = 1 / (2π√(10⁻⁶))
   = 1 / (2π × 10⁻³)
   = 1 / (6.283 × 10⁻³)
   = 159.15 Hz
```

**Paso 2:** Reactancias en resonancia

```
X_L = 2π × 159.15 × 0.1 = 100 Ω
X_C = 1/(2π × 159.15 × 10×10⁻⁶) = 100 Ω  ✓ (iguales)
```

**Paso 3:** Corriente y voltajes

```
Z = R = 10Ω (solo resistiva)
I = V / R = 10 / 10 = 1.0 A

V_R = I × R = 1.0 × 10 = 10 V (igual a la fuente)
V_L = I × X_L = 1.0 × 100 = 100 V (¡10 veces V!)
V_C = I × X_C = 1.0 × 100 = 100 V (¡10 veces V!)
```

### Verificación

```
V_L y V_C están desfasados 180°, por lo tanto:
V_L + V_C (fasorial) = 100∠90° + 100∠-90° = j100 - j100 = 0  ✓

Voltaje total: V_R + V_L + V_C = 10∠0° + 0 = 10∠0° V = V_fuente  ✓
```

> **Advertencia:** En resonancia serie, los voltajes en L y C pueden ser **muy superiores** al voltaje de la fuente. Esto puede dañar componentes si no se diseña adecuadamente.

---

## 20. Resonancia en Paralelo

La resonancia en paralelo ocurre cuando **I_L = I_C** cuando ambas ramas comparten el mismo voltaje.

### Condición

```
I_L = I_C  →  V/X_L = V/X_C  →  X_L = X_C
```

Esto es la misma condición que en serie, pero el efecto es diferente.

### En resonancia paralelo

```
I_C = I_L (pero ambas pueden ser MUY mayores que I_total)
I_total = I_R (solo fluye por la rama resistiva)
Z_total = R × Q (máxima)
```

### Ejemplo

**Datos:** R = 1kΩ, L = 10mH, C = 0.1μF, V = 10V, f = f₀ = 5033 Hz

**Paso 1:** Verificar resonancia

```
X_L = 2π × 5033 × 0.01 = 316.2 Ω
X_C = 1/(2π × 5033 × 0.1×10⁻⁶) = 316.2 Ω  ✓
```

**Paso 2:** Corrientes

```python
I_R = V / R = 10 / 1000 = 0.01 A = 10 mA
I_L = V / X_L = 10 / 316.2 = 0.0316 A = 31.6 mA
I_C = V / X_C = 10 / 316.2 = 0.0316 A = 31.6 mA
```

**Paso 3:** Corriente total

```
I_total = I_R = 10 mA  (las reactivas se cancelan)
```

**Paso 4:** Impedancia equivalente

```
| Z | = V / I_total = 10 / 0.01 = 1000 Ω = R 
```

### Verificación

```
I_L y I_C están desfasadas 180°:
I_L + I_C (fasorial) = 31.6∠-90° + 31.6∠90° = -j31.6 + j31.6 = 0  ✓

I_total = I_R + I_L + I_C = 10 mA + 0 = 10 mA  ✓
```

### Aplicación

La resonancia paralelo se usa en **filtros selectivos**: solo pasan señales cercanas a f₀. Las señales fuera de resonancia ven una impedancia baja y se atenúan.

---

## 21. Factor de Calidad Q

El factor de calidad Q mide la **selectividad** de un circuito resonante. Indica cuánta energía se almacena comparada con la que se disipa por ciclo.

### Definición

```python
Q = X_L / R = (2πf₀L) / R     (en serie)
Q = R / X_L = R / (2πf₀L)     (en paralelo)
```

En términos de L y C:

```
Q = (1/R) × √(L/C)    (serie)
Q = R × √(C/L)        (paralelo)
```

### Ancho de banda

```
BW = f₀ / Q    [Hz]

BW = f₂ - f₁  (frecuencias a -3dB)
```

### Interpretación de Q

| **Q** | **Tipo de circuito** | **Aplicación** |
|---|-----------------|-----------|
| Q > 10 | Muy selectivo | Filtros de radio, osciladores |
| Q = 5 – 10 | Selectivo | Filtros de audio, sintonía |
| Q = 1 – 5 | Moderado | Circuitos de carga general |
| Q < 1 | Amplio | Amortiguación, supresión |
### Ejemplo

**Datos:** f₀ = 1000 Hz, Q = 20

**Paso 1:** Ancho de banda

```
BW = f₀ / Q = 1000 / 20 = 50 Hz
```

**Paso 2:** Frecuencias de corte

```python
f₁ = f₀ - BW/2 = 1000 - 25 = 975 Hz
f₂ = f₀ + BW/2 = 1000 + 25 = 1025 Hz
```

**Paso 3:** Verificación de Q con valores de L y R

```
Si L = 10 mH, R = 3.14 Ω:

X_L = 2π × 1000 × 0.01 = 62.83 Ω
Q = X_L / R = 62.83 / 3.14 = 20.0  ✓
```

---

## 22. Análisis de Mallas en CA

El análisis de mallas funciona igual que en CD, pero usando **impedancias complejas** en lugar de resistencias.

### Procedimiento

1. Asignar corrientes de malla (I₁, I₂, ...) en sentido horario
2. Escribir KVL para cada malla con impedancias complejas
3. Resolver el sistema de ecuaciones complejas

### Ejemplo

**Datos:** Dos mallas con:
- Malla 1: V = 100∠0°, Z₁ = 4 + j3Ω, Z_compartida = 2 - j2Ω
- Malla 2: Z₂ = 3 + j1Ω, Z_compartida = 2 - j2Ω

**Ecuaciones de malla:**

```
Malla 1: (Z₁ + Z_c) × I₁ - Z_c × I₂ = V
         (4 + j3 + 2 - j2) × I₁ - (2 - j2) × I₂ = 100∠0°
         (6 + j1) × I₁ - (2 - j2) × I₂ = 100  ... (1)

Malla 2: -Z_c × I₁ + (Z₂ + Z_c) × I₂ = 0
         -(2 - j2) × I₁ + (3 + j1 + 2 - j2) × I₂ = 0
         -(2 - j2) × I₁ + (5 - j1) × I₂ = 0  ... (2)
```

**Resolviendo (2) para I₁:**

```
I₁ = (5 - j1)/(2 - j2) × I₂
   = (5 - j1)(2 + j2) / ((2 - j2)(2 + j2)) × I₂
   = (10 + j10 - j2 - j²2) / (4 + 4) × I₂
   = (12 + j8) / 8 × I₂
   = (1.5 + j1) × I₂
```

**Sustituyendo en (1):**

```
(6 + j1)(1.5 + j1) × I₂ - (2 - j2) × I₂ = 100
(9 + j6 + j1.5 + j²) × I₂ - (2 - j2) × I₂ = 100
(8 + j7.5) × I₂ - (2 - j2) × I₂ = 100
(6 + j9.5) × I₂ = 100

I₂ = 100 / (6 + j9.5)
   = 100(6 - j9.5) / (36 + 90.25)
   = (600 - j950) / 126.25
   = 4.752 - j7.525 A
   = 8.89 ∠ -57.8° A
```

**I₁:**

```
I₁ = (1.5 + j1) × I₂ = (1.5 + j1)(4.752 - j7.525)
   = (7.128 - j11.288 + j4.752 - j²7.525)
   = 14.653 - j6.536
   = 16.04 ∠ -24.0° A
```

---

## 23. Análisis de Nodos en CA

El análisis de nodos usa **admitancias** (Y = 1/Z) y es dual al análisis de mallas.

### Procedimiento

1. Seleccionar nodo de referencia (tierra)
2. Asignar voltajes de nodo (V₁, V₂, ...)
3. Escribir KCL: suma de corrientes que salen = 0
4. Usar admitancias: I = Y × V

### Ejemplo

**Datos:** Tres ramas conectadas a un nodo V₁:
- Rama 1: fuente V_s = 50∠30° con Z₁ = 2 + j1Ω
- Rama 2: Z₂ = 3 - j2Ω (a tierra)
- Rama 3: Z₃ = 1 + j3Ω (a tierra)

**Admitancias:**

```python
Y₁ = 1/(2 + j1) = (2 - j1)/5 = 0.4 - j0.2 S
Y₂ = 1/(3 - j2) = (3 + j2)/13 = 0.2308 + j0.1538 S
Y₃ = 1/(1 + j3) = (1 - j3)/10 = 0.1 - j0.3 S
```

**KCL en el nodo V₁:**

```
Y₁(V₁ - V_s) + Y₂V₁ + Y₃V₁ = 0
V₁(Y₁ + Y₂ + Y₃) = Y₁ × V_s

Y_total = Y₁ + Y₂ + Y₃
        = (0.4 + 0.2308 + 0.1) + j(-0.2 + 0.1538 - 0.3)
        = 0.7308 - j0.3462 S
```

**Resolviendo:**

```
V₁ = Y₁ × V_s / Y_total
   = (0.4 - j0.2) × 50∠30° / (0.7308 - j0.3462)
```

Convirtiendo a polar:
```
Y₁ = 0.4472 ∠ -26.57°
Y_total = 0.8091 ∠ -25.45°
V_s = 50∠30°

V₁ = (0.4472 × 50 / 0.8091) ∠ (-26.57° + 30° - (-25.45°))
   = 27.64 ∠ 28.88° V
```

### Verificación

```
I₁ = Y₁(V₁ - V_s) = (0.4472∠-26.57°)(27.64∠28.88° - 50∠30°)
I₂ = Y₂ × V₁ = (0.2774∠33.69°)(27.64∠28.88°)
I₃ = Y₃ × V₁ = (0.3162∠-71.57°)(27.64∠28.88°)

I₁ + I₂ + I₃ ≈ 0  ✓ (KCL satisfecha)
```

---

## 24. Thevenin y Norton en CA

Los teoremas de Thevenin y Norton se aplican directamente en CA usando **números complejos**.

### Thevenin

```
V_Th = voltaje de circuito abierto (fasor)
Z_Th = impedancia equivalente (fuentes de voltaje → cortocircuito, fuentes de corriente → abierto)
```

### Norton

```
I_N = V_Th / Z_Th
Z_N = Z_Th
```

### Ejemplo

**Circuito:** Fuente V = 100∠0° con impedancia interna Z₁ = 2 + j1Ω, conectada a una carga a través de Z₂ = 3 - j2Ω y Z₃ = 1 + j4Ω.

**Paso 1:** Voltaje de Thevenin (abierto entre terminales A-B, sin carga)

```
Divisor de voltaje:
V_Th = V × Z₃ / (Z₁ + Z₂ + Z₃)
     = 100∠0° × (1 + j4) / ((2+j1) + (3-j2) + (1+j4))
     = 100 × (1 + j4) / (6 + j3)
```

En polar:
```
1 + j4 = 4.123∠75.96°
6 + j3 = 6.708∠26.57°

V_Th = 100 × 4.123/6.708 ∠(75.96° - 26.57°)
     = 61.47 ∠ 49.39° V
```

**Paso 2:** Impedancia de Thevenin (apagar fuente → cortocircuitar V)

```python
Z_Th = (Z₁ + Z₂) ∥ Z₃
     = ((2+j1) + (3-j2)) ∥ (1+j4)
     = (5 - j1) ∥ (1 + j4)
```

```
Z_Th = (5-j1)(1+j4) / ((5-j1) + (1+j4))
     = (5 + j20 - j1 - j²4) / (6 + j3)
     = (9 + j19) / (6 + j3)
```

Multiplicando por conjugado:
```
= (9 + j19)(6 - j3) / (36 + 9)
= (54 - j27 + j114 - j²57) / 45
= (111 + j87) / 45
= 2.467 + j1.933 Ω
= 3.135∠38.05° Ω
```

**Paso 3:** Norton

```
I_N = V_Th / Z_Th = 61.47∠49.39° / 3.135∠38.05°
    = 19.61 ∠ 11.34° A

Z_N = Z_Th = 2.467 + j1.933 Ω
```

### Verificación

```
Si conectamos una carga Z_L = 5Ω:

V_L = V_Th × Z_L / (Z_Th + Z_L)
    = 61.47∠49.39° × 5 / (7.467 + j1.933)
    = 61.47∠49.39° × 5 / 7.717∠14.55°
    = 39.83 ∠ 34.84° V

I_L = V_L / Z_L = 39.83 / 5 = 7.966 A
```

Verificación por Norton:
```
I_L = I_N × Z_N / (Z_N + Z_L) = 19.61∠11.34° × 3.135∠38.05° / 7.717∠14.55°
    = 7.966 ∠ 34.84° A  ✓
```

---

## 25. Sistemas Trifásicos Equilibrados

Un sistema trifásico usa **tres fuentes** sinusoidales de igual magnitud y frecuencia, desfasadas 120° entre sí.

### Fuentes trifásicas

```
Secuencia ABC (positiva):
  V_a = V∠0°
  V_b = V∠-120°
  V_c = V∠+120° = V∠-240°

Secuencia ACB (negativa):
  V_a = V∠0°
  V_b = V∠+120°
  V_c = V∠-120°
```

### Verificación fundamental

```
V_a + V_b + V_c = 0  (siempre, en cualquier instante)

Demostración:
V_a = V∠0° = V + j0
V_b = V∠-120° = V(cos(-120°) + j sin(-120°)) = V(-0.5 - j0.866)
V_c = V∠+120° = V(cos(120°) + j sin(120°)) = V(-0.5 + j0.866)

Suma: V(1 - 0.5 - 0.5) + jV(0 - 0.866 + 0.866) = 0  ✓
```

### Ventajas del sistema trifásico

1. **Potencia constante**: la suma de potencias de las tres fases es constante (no oscila como en monofásico)
2. **Equilibrado natural**: con cargas equilibradas, la corriente por el neutro es cero
3. **Conductor neutro**: puede ser más delgado (o eliminarse en cargas equilibradas)
4. **Campo magnético rotatorio**: permite construir motores simples y eficientes
5. **Distribución eficiente**: 3 conductores transmiten el triple de potencia con solo 1.5× el cobre

### Ejemplo

**Datos:** Sistema trifásico equilibrado, V_fase = 220V, carga por fase Z = 30 + j40Ω

**Paso 1:** Corriente por fase

```
| Z | = √(30² + 40²) = 50 Ω 
I_a = V_a / Z = 220∠0° / 50∠53.13° = 4.4 ∠ -53.13° A
I_b = V_b / Z = 220∠-120° / 50∠53.13° = 4.4 ∠ -173.13° A
I_c = V_c / Z = 220∠+120° / 50∠53.13° = 4.4 ∠ 66.87° A
```

**Paso 2:** Verificación — suma de corrientes

```
I_a + I_b + I_c = 4.4(∠-53.13° + ∠-173.13° + ∠66.87°)
= 4.4[(0.6 - j0.8) + (-0.993 - j0.122) + (0.393 + j0.920)]
= 4.4[(0.6 - 0.993 + 0.393) + j(-0.8 - 0.122 + 0.920)]
= 4.4[0.0 + j0.0] = 0  ✓
```

**Paso 3:** Potencia por fase

```
P_fase = V × I × cos(φ) = 220 × 4.4 × cos(53.13°) = 220 × 4.4 × 0.6 = 580.8 W
Q_fase = V × I × sin(φ) = 220 × 4.4 × sin(53.13°) = 220 × 4.4 × 0.8 = 774.4 VAR
S_fase = V × I = 220 × 4.4 = 968 VA

P_total = 3 × 580.8 = 1742.4 W
S_total = 3 × 968 = 2904 VA
```

---


---

## 26. Conexión Estrella (Y)

En conexión estrella, tres impedancias comparten un punto común llamado **neutro** o estrella.

### Relaciones fundamentales

```
V_L = √3 × V_F    [V]
I_L = I_F          [A]
```

- **V_L**: voltaje entre líneas (dos fases distintas)
- **V_F**: voltaje fase (entre una línea y el neutro)
- **I_L**: corriente que circula por la línea
- **I_F**: corriente que circula por la fase (impedancia)

### Neutro

El neutro es el punto común donde se unen las tres fases. En un sistema **equilibrado**, la corriente en el neutro es **cero** porque las tres corrientes de fase se cancelan vectorialmente.

Si hay **desequilibrio** (cargas desiguales en cada fase), el neutro porta la diferencia. Por eso se recomienda cable de sección adecuada en el neutro.

### Ejemplo práctico

```
Dado: V_F = 220V (voltaje fase-neutro)

V_L = √3 × 220 = 1.732 × 220 = 381 V

Verificación: 381 / 220 = 1.732 ≈ √3 ✓
```

> En America Latina, la toma doméstica es V_F = 120V → V_L = 208V. En Europa, V_F = 230V → V_L = 400V.

---

## 27. Conexión Triángulo (Δ)

En conexión triángulo, las tres impedancias forman un lazo cerrado sin punto neutro.

### Relaciones fundamentales

```
V_L = V_F           [V]
I_L = √3 × I_F      [A]
```

- **V_L = V_F**: cada impedancia recibe directamente el voltaje entre líneas
- **I_L = √3 × I_F**: la corriente de línea se reparte entre dos fases

### Características

- **Sin neutro**: no hay punto común, es un circuito cerrado
- **Autoequilibrado**: tiende a balancear cargas por sí mismo
- **Mayor corriente en línea**: cada línea alimenta dos fases

### Ejemplo práctico

```
Dado: I_F = 10A (corriente por cada impedancia)

I_L = √3 × 10 = 1.732 × 10 = 17.32 A

Verificación: 17.32 / 10 = 1.732 ≈ √3 ✓
```

---

## 28. Tabla Comparativa Y vs Δ

| **Parámetro** | **Estrella (Y)** | **Triángulo (Δ)** |
|-----------|--------------|----------------|
| **Voltaje línea-fase** | V_L = √3 × V_F | V_L = V_F |
| **Corriente línea-fase** | I_L = I_F | I_L = √3 × I_F |
| **Voltaje fase** | V_F = V_L / √3 | V_F = V_L |
| **Corriente fase** | I_F = I_L | I_F = I_L / √3 |
| **Neutro** | Sí (punto común) | No |
| **Potencia** | P = √3 × V_L × I_L × cosφ | P = √3 × V_L × I_L × cosφ |
| **Arranque de motor** | Menor voltaje en devanados | Mayor torque de arranque |
| **Aplicación típica** | Arranque Y-Δ, alta tensión | Cargas equilibradas, motores |
### Cuándo usar cada una

```
Estrella (Y):
  → Arranque de motores (reducir corriente inicial)
  → Sistemas con neutro (distribución doméstica)
  → Alta tensión (reducir aislamiento)

Triángulo (Δ):
  → Operación normal de motores
  → Cargas pesadas equilibradas
  → Cuando se necesita mayor torque
```

### Arranque Y-Δ (método clásico)

1. **Arranque en Y**: voltaje por fase = V_L/√3 → corriente reducida a 1/3
2. **Operación en Δ**: voltaje por fase = V_L → potencia nominal

```
I_arranque_Y / I_arranque_Δ = 1/3
Torque_Y / Torque_Δ = 1/3
```

---

## 29. Potencia Trifásica

En un sistema trifásico equilibrado, la potencia total es **3 veces** la potencia de una fase, pero se expresa en función de valores de línea.

### Potencia activa (P)

```
P = √3 × V_L × I_L × cosφ    [W]
```

Es la potencia real que realiza trabajo útil.

### Potencia reactiva (Q)

```
Q = √3 × V_L × I_L × sinφ    [VAR]
```

Es la potencia que oscila entre fuente y carga (almacenada/devuelta por L y C).

### Potencia aparente (S)

```
S = √3 × V_L × I_L            [VA]
```

Es la combinación vectorial de P y Q.

### Relación entre potencias

```
S² = P² + Q²
cosφ = P / S    (factor de potencia)
sinφ = Q / S
tanφ = Q / P
φ = arccos(P/S)
```

### Ejemplo completo

```
Motor trifásico: V_L = 400V, I_L = 20A, FP = cosφ = 0.85

P = √3 × 400 × 20 × 0.85
P = 1.732 × 400 × 20 × 0.85
P = 11,777 W = 11.78 kW

S = √3 × 400 × 20 = 13,856 VA = 13.86 kVA

Q = √3 × 400 × 20 × sin(arccos(0.85))
φ = arccos(0.85) = 31.79°
sin(31.79°) = 0.527
Q = 1.732 × 400 × 20 × 0.527 = 7,318 VAR = 7.32 kVAR

Verificación:
S² = P² + Q²
13.86² = 11.78² + 7.32²
192.1 = 138.8 + 53.6 = 192.4 ✓ (diferencia por redondeo)
```

---

## 30. Secuencia de Fases

La secuencia indica el orden en que los voltajes alcanzan su valor máximo.

### Secuencia positiva (ABC)

```
V_a = V_m × sin(ωt)
V_b = V_m × sin(ωt - 120°)
V_c = V_m × sin(ωt - 240°) = V_m × sin(ωt + 120°)
```

Los voltajes alcanzan su pico en orden: A → B → C

### Secuencia negativa (ACB)

```
V_a = V_m × sin(ωt)
V_c = V_m × sin(ωt - 120°)
V_b = V_m × sin(ωt - 240°) = V_m × sin(ωt + 120°)
```

Los voltajes alcanzan su pico en orden: A → C → B

### Invertir el giro de un motor

Para invertir el sentido de giro de un motor trifásico de inducción, **se intercambian cualquier dos fases**:

```
Original (ABC):    L1→A, L2→B, L3→C  →  giro horario
Invertido (ACB):   L1→A, L2→C, L3→B  →  giro antihorario

(Intercambiar L2 y L3)
```

### Método de las dos bombillas y voltímetro

Para detectar la secuencia de fases:

```
1. Conectar dos bombillas incandescentes en serie entre L1-L2 y L2-L3
2. Conectar un voltímetro entre L1 y L3
3. La bombilla que se enciende MÁS es la de mayor voltaje
4. Si bombilla L1-L2 brilla más → secuencia ABC
5. Si bombilla L2-L3 brilla más → secuencia ACB
```

### Método del capacitor (simple)

```
1. Conectar un capacitor entre dos fases
2. Conectar una bombilla en serie con el capacitor
3. Conectar entre la tercera fase y el punto medio
4. Bombilla brilla → secuencia correcta
5. Bombilla no brilla → secuencia invertida
```

---

## 31. Trifásico Desequilibrado

Cuando las cargas en las tres fases no son iguales, el sistema se desequilibra.

### Componentes simétricas de Fortescue

Cualquier sistema desequilibrado se descompone en **tres sistemas equilibrados**:

```
V₀ = (V_a + V_b + V_c) / 3          → Componente CERO
V₁ = (V_a + a×V_b + a²×V_c) / 3     → Componente POSITIVA
V₂ = (V_a + a²×V_b + a×V_c) / 3     → Componente NEGATIVA

Donde: a = 1∠120° = -0.5 + j0.866
       a² = 1∠240° = -0.5 - j0.866
```

### Significado físico

| **Componente** | **Descripción** | **Efecto** |
|-----------|-------------|--------|
| **Positiva** | Sistema equilibrado con secuencia ABC | Funcionamiento normal |
| **Negativa** | Sistema equilibrado con secuencia ACB | Calentamiento en motores, fallas |
| **Cero** | Tres fasores iguales en fase | Corriente por neutro |
### Aplicación: análisis de fallas

```
Cortocircuito fase-fase:
  → Aparece componente negativa
  → El motor se calienta excesivamente

Cortocircuito fase-tierra:
  → Aparece componente cero
  → La corriente fluye por el neutro/tierra

Cortocircuito trifásico:
  → Solo componente positiva (simétrico)
```

### Neutro en sistema desequilibrado

```
I_neutro = I_a + I_b + I_c

Si las cargas son iguales: I_neutro = 0
Si hay desequilibrio: I_neutro ≠ 0 (porta la diferencia)
```

> El neutro debe tener suficiente sección para soportar la corriente de desequilibrio. En distribución doméstica, el neutro se dimensiona igual que las fases.

---

## 32. Transformadores: Principio de Funcionamiento

Un transformador convierte voltajes de CA de un nivel a otro **sin cambiar la frecuencia**, basándose en la **inducción electromagnética**.

### Ley de Faraday

```
e = -N × dΦ/dt    [V]

  e = fuerza electromotriz inducida (V)
  N = número de espiras del devanado
  dΦ/dt = tasa de cambio del flujo magnético (Wb/s)
```

El signo negativo indica que la fem inducida se opone al cambio (ley de Lenz).

### Relación de transformación

```python
a = N₁/N₂ = V₁/V₂ = I₂/I₁

  a = relación de transformación
  N₁, N₂ = espiras primario y secundario
  V₁, V₂ = voltajes primario y secundario
  I₁, I₂ = corrientes primario y secundario
```

### Propiedades fundamentales

```
1. Transforma voltaje y corriente
   → Si a > 1: reductor (V₂ < V₁)
   → Si a < 1: elevador (V₂ > V₁)

2. NO transforma potencia (transformador ideal)
   → P₁ = P₂ → V₁×I₁ = V₂×I₂

3. Transforma impedancia
   → Z₁/Z₂ = a²
   → Z_ref primario = a² × Z_secundario
```

### Polaridad de bornes (puntos)

Los **puntos de polaridad** indican la relación de fase entre primario y secundario:

```
  ·₁ ───┐           ┌─── ·₂
        │  Núcleo   │
  ──────┘           └──────
  
Si ·₁ y ·₂ están en el mismo lado:
  V₁ y V₂ están en fase (polaridad aditiva)

Si ·₁ y ·₂ están en lados opuestos:
  V₁ y V₂ están desfasados 180° (polaridad sustractiva)
```

### Ejemplo

```
Transformador reductor: N₁ = 1000 espiras, N₂ = 200 espiras, V₁ = 220V

a = 1000/200 = 5
V₂ = V₁/a = 220/5 = 44V

Si I₁ = 2A:
I₂ = a × I₁ = 5 × 2 = 10A

Verificación de potencia:
P₁ = 220 × 2 = 440W
P₂ = 44 × 10 = 440W ✓
```

---

## 33. Transformador Ideal vs Real

### Transformador ideal

El transformador ideal tiene las siguientes características simplificadas:

```python
1. Sin pérdidas en el cobre (R = 0 en ambos devanados)
2. Sin pérdidas en el núcleo (permeabilidad μ = ∞)
3. Acoplamiento magnético perfecto (k = 1, fuga = 0)
4. Relación V₁/V₂ = N₁/N₂ exacta
5. P₁ = P₂ siempre
```

### Transformador real: pérdidas

En la práctica, existen pérdidas que hacen que P₂ < P₁.

#### Pérdidas en el núcleo (hierro)

```
P_núcleo = P_histeresis + P_corrientes_parásitas

P_histeresis: Energía perdida al magnetizar/desmagnetizar el núcleo
  → Proporcional al volumen del núcleo y al material
  → Se reduce con acero al silicio

P_corrientes_parásitas: Corrientes de Foucault en el núcleo
  → Proporcional al grosor de láminas
  → Se reduce con núcleo laminado
```

#### Pérdidas en el cobre (devanados)

```
P_cobre = I₁² × R₁ + I₂² × R₂

  R₁ = resistencia del devanado primario
  R₂ = resistencia del devanado secundario
  → Se reduce con cable de mayor sección
```

### Modelo equivalente

```
        R₁      jX₁         R₂'     jX₂'
  ─────┤├───┤├─────┤───────┤├───┤├─────
  V₁       X_Lm    R_c            V₂'
           │   │
          ─┴─ ─┴─   (rama magnetizante)
           │   │
  ─────────┴───┴────────────────────────

R₁, X₁: Resistencia y reactancia del primario
R₂', X₂': Resistencia y reactancia del secundario (referidos al primario)
R_c: Resistencia que modela pérdidas en núcleo
X_Lm: Reactancia magnetizante (ramal de magnetización)
```

### Ejemplo

```python
Transformador 10kVA, 2200/220V:

Pérdidas en núcleo (medidas en ensayo abierto): P₀ = 80W
Pérdidas en cobre a plena carga: P_cc = 200W

P_total pérdidas = 80 + 200 = 280W
P_entrada = 10,000 + 280 = 10,280W
η = 10,000 / 10,280 = 97.3%
```

---

## 34. Ensayos: Circuitos Abierto y Cortocircuito

Los ensayos permiten determinar los parámetros del transformador sin abrirlo.

### Ensayo de circuito abierto (OC)

Se aplica voltaje nominal al primario con el **secundario abierto** (sin carga).

```
Procedimiento:
  1. Conectar V₁ nominal al primario
  2. Dejar secundario abierto
  3. Medir: I₀ (corriente de vacío) y P₀ (potencia)

Resultado:
  I₀ es muy pequeña (2-5% de I_nominal)
  P₀ = pérdidas en núcleo (conste, independiente de carga)
```

#### Cálculo de parámetros

```
R_c = V₁² / P₀           (resistencia del núcleo)
Y₀ = I₀ / V₁             (admitancia de vacío)
G_c = P₀ / V₁²           (conductancia del núcleo)
B_m = √(Y₀² - G_c²)      (susceptancia magnetizante)
X_Lm = 1/B_m              (reactancia magnetizante)
```

### Ensayo de cortocircuito (CC)

Se reduce el voltaje en el primario hasta que la corriente secundaria sea **nominal**, con el **secundario cortocircuitado**.

```
Procedimiento:
  1. Cortocircuitar el secundario
  2. Reducir V₁ lentamente hasta que I₂ = I_nominal
  3. Medir: V_cc (voltaje de cortocircuito) y P_cc

Resultado:
  V_cc es pequeña (5-10% de V_nominal)
  P_cc = pérdidas en cobre a plena carga
```

#### Cálculo de parámetros

```
Z_eq = V_cc / I₁          (impedancia equivalente)
R_eq = P_cc / I₁²         (resistencia equivalente)
X_eq = √(Z_eq² - R_eq²)   (reactancia equivalente)
```

### Resumen de ensayos

| **Ensayo** | **Conexión** | **Mide** | **Parámetros** |
|--------|----------|------|------------|
| **Abierto** | V₁ nominal, sec. abierto | I₀, P₀ | R_c, X_Lm (núcleo) |
| **Cortocircuito** | I₂ nominal, sec. corto | V_cc, P_cc | R_eq, X_eq (cobre) |
---

## 35. Eficiencia y Regulación

### Eficiencia (η)

```
η = P_salida / P_entrada × 100%

P_entrada = P_salida + P_núcleo + P_cobre

η = P_out / (P_out + P₀ + P_cc) × 100%
```

Donde:
- P₀ = pérdidas en núcleo (constantes, independientes de carga)
- P_cc = pérdidas en cobre (varían con el cuadrado de la carga)

### Condición de eficiencia máxima

La eficiencia es máxima cuando las **pérdidas variables = pérdidas constantes**:

```
P_cubre = P_núcleo
I² × R_eq = P₀
I_máx_eficiencia = √(P₀ / R_eq)
```

### Curva de eficiencia

```
η (%)
  │        ╭──────────────╮
  │       ╱                ╲
  │      ╱                  ╲
  │     ╱                    ╲
  │    ╱                      ╲
  │   ╱                        ╲
  │──╱──────────────────────────╲──
  └──────────────────────────────→ Carga
  0%    25%   50%  75%  100%  125%
         ↑
    Máx. eficiencia
    (P_cobre = P_núcleo)
```

### Regulación de voltaje

Mide la variación del voltaje de salida entre vacío y plena carga.

```
Reg = (V_vacío - V_plena_carga) / V_plena_carga × 100%
```

O en función de impedancia:

```
Reg ≈ (I × R_eq × cosφ + I × X_eq × sinφ) / V₂ × 100%
```

### Ejemplo

```
Transformador 50kVA, 2300/230V:
P₀ = 200W, P_cc = 600W

A plena carga (S = 50kVA):
P_salida = 50,000W
P_cobre = 600W
P_núcleo = 200W

η = 50,000 / (50,000 + 600 + 200) × 100%
η = 50,000 / 50,800 × 100% = 98.4%

Carga de máxima eficiencia:
I = √(200/R_eq) = √(P₀/P_cc) × I_nominal
I = √(200/600) × I_nominal = 0.577 × I_nominal → 57.7% de carga
```

---

## 36. Transformadores Trifásicos

Se usan tres transformadores monofásicos (o un solo cuerpo trifásico) para transformar sistemas trifásicos.

### Conexiones principales

#### Y-Y (Estrella-Estrella)

```
V_L2/V_L1 = N₂/N₁ = a (igual que monofásico)
Ventajas: Neutro disponible, aislamiento simple
Riesgo: Desequilibrio de carga distorsiona el voltaje
```

#### Δ-Δ (Triángulo-Triángulo)

```
V_L2/V_L1 = a
Ventajas: Autoequilibrado, sin problema de distorsión
Riesgo: Sin neutro
```

#### Y-Δ (Estrella-Triángulo)

```
V_L2/V_L1 = a/√3 (reductor)
Ventajas: Neutro en primario, buena para distribución
Uso: Transformador de distribución
```

#### Δ-Y (Triángulo-Estrella)

```
V_L2/V_L1 = √3 × a (elevador)
Ventajas: Neutro en secundario, buena para generación
Uso: Transformador de generación (alternador → red)
```

### Grupo de conexiones (reloj)

La notación indica el desfase entre voltajes de línea primario y secundario.

```
Formato: Dyn11
  D = Primario en triángulo (Delta)
  y = Secundario en estrella (Wye)
  n = Neutro disponible
  11 = Posición del voltaje secundario en el reloj (11:00 → +30°)

Ejemplos comunes:
  Dyn11: El secundario ADELA al primario 30° (el más común)
  YNd5:  El secundario RETRASA al primario 150°
  Dyn1:  El secundario ADELA 30° en sentido horario
```

### Cuándo usar cada conexión

```
Dyn11 (Δ-Y): Transformador de distribución (el más usado en el mundo)
  → Neutro para cargas monofásicas
  → Triángulo en primario filtra armónicos

YNd1 (Y-Δ): Generación eléctrica
  → Neutro en generador
  → Triángulo en secundario para cargas industriales

Y-Y: Sistemas de alta tensión (>100kV)
  → Neutro aterrizado
  → Requiere cargas equilibradas

Δ-Δ: Sistemas industriales de media tensión
  → Opera con un transformador dañado (V-V)
```

---

## 37. Autotransformadores

Un autotransformador utiliza **un solo devanado** con una toma intermedia, en lugar de dos devanados separados.

### Principio de funcionamiento

```
        ┌─── Toma intermedia (secundario)
        │
  N₁ ───┤
        │
  ──────┴──────

  V₁ se aplica en todo el devanado
  V₂ se toma desde la toma intermedia
```

### Relación de transformación

```
a = N₁/N₂ = V₁/V₂

Pero N₂ < N₁, siempre a ≥ 1
El devanado compartido N₂ - N₁ porta la diferencia de potencia
```

### Ventajas sobre transformador convencional

```
1. Más compacto: solo un devanado
2. Más eficiente: menor pérdida en cobre
3. Más barato: menos material
4. Menor peso y tamaño
```

### Desventaja crítica

```
⚠️  PELIGRO: No hay aislamiento galvánico entre primario y secundario

Si el primario está conectado a la red de alta tensión,
el secundario queda potencialmente a alta tensión respecto a tierra.

Nunca usar cuando:
  → Se necesita aislamiento de seguridad
  → Cargas con personas en contacto
  → Normativas lo prohíban
```

### Aplicaciones típicas

```
1. Arranque de motores (reductor de voltaje)
   → Arranque con 50-80% del voltaje nominal
   → Reduce corriente de arranque

2. Variadores de voltaje (variac)
   → Toa móvil continua
   → Control de iluminación, calentadores

3. Laboratorios
   → Fuente variable de voltaje

4. Reducción de pérdidas en distribución
   → Cuando a es pequeño (1.1 a 3)
```

### Ejemplo

```python
Autotransformador reductor: 220V → 110V

a = 220/110 = 2
El devanado compartido porta I₂ - I₁

Si P = 2kW:
I₂ = 2000/110 = 18.18A
I₁ = 2000/220 = 9.09A

Corriente en devanado compartido = I₂ - I₁ = 9.09A
(vs. 18.18A en transformador convencional → ahorro del 50%)
```

---

## 38. Armónicos y Distorsión

Los armónicos son componentes de frecuencia **múltiplo entero** de la fundamental, generados por cargas no lineales.

### Definición de THD (Distorsión Armónica Total)

```
THD = √(I₂² + I₃² + I₄² + ... + Iₙ²) / I₁ × 100%

  I₁ = corriente fundamental (50/60 Hz)
  I₂, I₃... = corrientes armónicas (100/120 Hz, 150/180 Hz...)
  THD = porcentaje de distorsión
```

### Origen de los armónicos

```
Cargas no lineales (electrónica de potencia):
  → Fuentes conmutadas (computadoras, LED)
  → Rectificadores (cargadores, variadores)
  → Arcos (soldadura, hornos)
  → Motores con saturación del núcleo

Frecuencias armónicas:
  Fundamental: 60 Hz (1er armónico)
  3er armónico: 180 Hz
  5to armónico: 300 Hz
  7mo armónico: 420 Hz
  ... y así sucesivamente
```

### Efectos negativos

```
1. Calentamiento
   → Pérdidas adicionales en transformadores y motores
   → Derating (reducción de capacidad)

2. Interferencia
   → Perturba telecomunicaciones
   → Causa malfunction de equipos electrónicos

3. Fallos
   → Vibraciones en motores
   → Daño en capacitores de corrección de FP
   → Disparo intempestivo de protecciones

4. Pérdidas
   → Corriente de neutro elevada (armónicos triple)
   → Pérdidas adicionales en conductores
```

### Norma IEEE 519

```
Límite de THD en voltaje: < 5% (en punto de común acoplamiento)
Límite de THD en corriente: varía según relación I_SC/I_L

| **I_SC/I_L** | **Límite THD corriente** |
|----------|----------------------|
| < 20 | 5.0% |
| 20-50 | 3.0% |
| 50-100 | 1.5% |
| 100-1000 | 0.7% |
| > 1000 | 0.35% | ``` 

### Ejemplo de cálculo

```
Corriente fundamental I₁ = 100A
I₃ = 30A, I₅ = 20A, I₇ = 10A

THD = √(30² + 20² + 10²) / 100 × 100%
THD = √(900 + 400 + 100) / 100 × 100%
THD = √1400 / 100 × 100%
THD = 37.42 / 100 × 100% = 37.42%

⚠️ Este THD es muy alto, excede el límite IEEE 519
Se requieren filtros armónicos
```

---

## 39. Filtros Eléctricos

Los filtros permiten **pasar ciertas frecuencias** y **bloquear otras**, esenciales para eliminar armónicos y proteger equipos.

### Filtro paso-bajo (low-pass)

```
Permite: frecuencias bajas (hasta f_c)
Bloquea: frecuencias altas

Circuito RC:
  ──┤├────┤├──
     R     C (a tierra)

f_c = 1 / (2π × R × C)    [Hz]

  R en ohmios (Ω)
  C en faradios (F)
```

### Filtro paso-alto (high-pass)

```
Permite: frecuencias altas (desde f_c)
Bloquea: frecuencias bajas

Circuito RC:
  ──┤├────┤├──
     C     R (a tierra)

f_c = 1 / (2π × R × C)    [Hz]
```

### Filtro paso-banda (band-pass)

```
Permite: solo frecuencias entre f₁ y f₂
Bloquea: todo lo demás

Circuito RLC serie:
  ──┤R├──┤L├──┤C├──

f₀ = 1 / (2π × √(L × C))    [Hz] (frecuencia central)

Ancho de banda:
  BW = R / (2π × L)    [Hz]
  Q = f₀ / BW (factor de calidad)
```

### Filtro rechaza-banda (band-stop/notch)

```
Bloquea: solo frecuencias entre f₁ y f₂
Permite: todo lo demás

Útil para eliminar una frecuencia específica (ej: 60Hz)

Circuito RLC paralelo en serie con la línea:
  ──┤R├──┤L├──┤C├── (en paralelo)
         │
        ─┴─  (a tierra)
```

### Ejemplo: filtro paso-bajo

```
Diseñar un filtro paso-bajo para eliminar armónicos ≥ 300Hz
(fundamental = 60Hz, queremos pasar solo hasta ~150Hz)

Usar f_c = 150Hz:

Elegir C = 0.1μF = 0.1 × 10⁻⁶ F

R = 1 / (2π × f_c × C)
R = 1 / (2π × 150 × 0.1×10⁻⁶)
R = 1 / (9.42 × 10⁻⁵)
R = 10,610 Ω ≈ 10.6 kΩ

Verificación:
f_c = 1 / (2π × 10,610 × 0.1×10⁻⁶) = 150 Hz ✓

A 60Hz:  X_C = 26.5 kΩ → paso casi libre
A 300Hz: X_C = 5.3 kΩ  → atenuación significativa
A 420Hz: X_C = 3.78 kΩ → alta atenuación
```

---

# 📊 Resumen de Corriente Alterna

> Tabla comprehensive de todas las fórmulas y conceptos clave, agrupados por tema.

---

## Onda Sinusoidal

| **Concepto** | **Fórmula** | **Unidades** |
|----------|---------|----------|
| Voltaje instantáneo | v(t) = V_max × sin(ωt + φ) | V |
| Frecuencia angular | ω = 2π × f | rad/s |
| Periodo | T = 1/f | s |
| Relación ω-f | ω = 2π/T | rad/s |
---

## Valores de Voltaje/Corriente

| **Valor** | **Fórmula** | **Factor** |
|-------|---------|--------|
| V_max (pico) | V_max | ×1 |
| V_rms (efectivo) | V_max / √2 | ×0.707 |
| V_medio | 2 × V_max / π | ×0.637 |
| V_pp (pico a pico) | 2 × V_max | ×2 |
---

## Componentes Pasivos

| **Componente** | **Reactancia** | **Frecuencia** | **Comportamiento** |
|-----------|-----------|-----------|----------------|
| Resistencia (R) | R (constante) | Cualquiera | Disipa energía |
| Inductor (L) | X_L = 2πfL | f ↑ → X_L ↑ | Pasa DC, bloquea HF |
| Capacitor (C) | X_C = 1/(2πfC) | f ↑ → X_C ↓ | Bloquea DC, pasa HF |
---

## Impedancia y Potencia

| **Concepto** | **Fórmula** | **Unidades** |
|----------|---------|----------|
| Impedancia | Z = R + jX = √(R² + X²) ∠ arctan(X/R) | Ω |
| Potencia activa | P = V × I × cosφ | W |
| Potencia reactiva | Q = V × I × sinφ | VAR |
| Potencia aparente | S = V × I | VA |
| Factor de potencia | FP = cosφ = P/S | Adimensional |
---

## Circuitos Serie

| **Circuito** | **Impedancia** | **Ángulo** |
|----------|-----------|--------|
| R | Z = R | 0° |
| L | Z = jX_L | +90° |
| C | Z = -jX_C | -90° |
| R-L | Z = R + jX_L | arctan(X_L/R) |
| R-C | Z = R - jX_C | -arctan(X_C/R) |
| R-L-C | Z = R + j(X_L - X_C) | arctan((X_L - X_C)/R) |
---

## Resonancia

| **Tipo** | **Condición** | **Impedancia** | **Frecuencia** |
|------|-----------|-----------|-----------|
| Serie | X_L = X_C | Z = R (mínima) | f₀ = 1/(2π√LC) |
| Paralelo | X_L = X_C | Z → ∞ (máxima) | f₀ = 1/(2π√LC) |
| Factor de calidad | Q = X_L/R = X_C/R | — | BW = f₀/Q |
---

## Sistemas Trifásicos

| **Conexión** | **Voltaje línea-fase** | **Corriente línea-fase** | **Neutro** |
|----------|-------------------|---------------------|--------|
| Estrella (Y) | V_L = √3 × V_F | I_L = I_F | Sí |
| Triángulo (Δ) | V_L = V_F | I_L = √3 × I_F | No |
---

## Potencia Trifásica

| **Tipo** | **Fórmula** | **Unidades** |
|------|---------|----------|
| Activa | P = √3 × V_L × I_L × cosφ | W |
| Reactiva | Q = √3 × V_L × I_L × sinφ | VAR |
| Aparente | S = √3 × V_L × I_L | VA |
---

## Transformadores

| **Concepto** | **Fórmula** | **Notas** |
|----------|---------|-------|
| Relación de transformación | a = N₁/N₂ = V₁/V₂ = I₂/I₁ | Ideal |
| Fem inducida | e = -N × dΦ/dt | Ley de Faraday |
| Eficiencia | η = P_out/(P_out + P_núcleo + P_cobre) | ×100% |
| Eficiencia máx | P_cobre = P_núcleo | Punto óptimo |
| Regulación | Reg = (V_vacío - V_carga)/V_carga × 100% | — |
---

## Ensayos de Transformador

| **Ensayo** | **Conexión** | **Mide** | **Resultado** |
|--------|----------|------|-----------|
| Circuito abierto | V₁ nominal, sec. abierto | I₀, P₀ | Pérdidas núcleo |
| Cortocircuito | I₂ nominal, sec. corto | V_cc, P_cc | Pérdidas cobre |
---

## Armónicos y Filtros

| **Concepto** | **Fórmula** | **Límite** |
|----------|---------|--------|
| THD | THD = √(ΣI_n²)/I₁ × 100% | < 5% (IEEE 519) |
| Frecuencia corte RC | f_c = 1/(2πRC) | Hz |
| Frecuencia resonancia LC | f₀ = 1/(2π√LC) | Hz |
| Ancho de banda | BW = R/(2πL) | Hz |
---

## Autotransformadores

| **Propiedad** | **Fórmula** | **Comparación con convencional** |
|-----------|---------|------------------------------|
| Relación | a = N₁/N₂ = V₁/V₂ | Igual |
| Corriente devanado | I₂ - I₁ | Menor (más eficiente) |
| Aislamiento | No galvánico | ⚠️ Peligro |
---

*Fin del documento — Corriente Alterna completa*
*39 temas · Desde onda sinusoidal hasta filtros armónicos*
