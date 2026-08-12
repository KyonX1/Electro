# 01 — Corriente Directa (CD / DC)

> Todo sobre circuitos de corriente directa: desde Ley de Ohm hasta análisis de transitorios.
> Cada concepto se explica con definición, fórmula, ejemplo y verificación.

---

## Índice

1. [Ley de Ohm](#1-ley-de-ohm)
2. [Circuitos serie](#2-circuitos-serie)
3. [Circuitos paralelo](#3-circuitos-paralelo)
4. [Circuitos mixtos](#4-circuitos-mixtos-serie-paralelo)
5. [Ley de Kirchhoff de Corrientes (LCK)](#5-ley-de-kirchhoff-de-corrientes-lck)
6. [Ley de Kirchhoff de Voltajes (LKV)](#6-ley-de-kirchhoff-de-voltajes-lkv)
7. [Divisor de voltaje](#7-divisor-de-voltaje)
8. [Divisor de corriente](#8-divisor-de-corriente)
9. [Teorema de Thevenin](#9-teorema-de-thevenin)
10. [Teorema de Norton](#10-teorema-de-norton)
11. [Transformación de fuentes](#11-transformación-de-fuentes)
12. [Teorema de superposición](#12-teorema-de-superposición)
13. [Transferencia de máxima potencia](#13-transferencia-de-máxima-potencia)
14. [Análisis de mallas](#14-análisis-de-mallas)
15. [Análisis de nodos](#15-análisis-de-nodos)
16. [Ley de Joule y efecto térmico](#16-ley-de-joule-y-efecto-térmico)
17. [Capacitores en CD](#17-capacitores-en-cd)
18. [Inductores en CD](#18-inductores-en-cd)
19. [Circuitos RC en CD (transitorio)](#19-circuitos-rc-en-cd-transitorio)
20. [Circuitos RL en CD (transitorio)](#20-circuitos-rl-en-cd-transitorio)
21. [Constante de tiempo (τ)](#21-constante-de-tiempo-τ)

---

## 1. Ley de Ohm

### Definición

La ley de Ohm establece que la corriente que circula por un conductor es directamente proporcional al voltaje aplicado e inversamente proporcional a su resistencia. Es la ecuación más importante de la electrotecnia.

### Fórmula

```
V = I × R

Despejes:
  I = V / R    (para calcular corriente)
  R = V / I    (para calcular resistencia)
```

Donde:
- **V** = voltaje o diferencia de potencial (Volts, V)
- **I** = corriente eléctrica (Amperios, A)
- **R** = resistencia (Ohmios, Ω)

### Analogía

El tubo de agua:
- Voltaje = presión del agua
- Corriente = cantidad de agua que fluye
- Resistencia = obstrucción en el tubo
- Más presión → más agua fluye (V ↑ → I ↑)
- Más obstrucción → menos agua fluye (R ↑ → I ↓)

### Regla práctica

En la ley de Ohm siempre conoces **dos** variables y calculas la tercera. Es como una calculadora de tres botones: presionas dos y obtienes el tercero.

### Ejemplo resuelto 1

*Una resistencia de 470 Ω se conecta a una fuente de 12V. ¿Cuánta corriente circula?*

```
I = V / R = 12 / 470 = 0.02553 A = 25.53 mA
```

**Verificación**: V = I × R = 0.02553 × 470 = 12.00 V ✓

### Ejemplo resuelto 2

*Un motor consume 3.5A cuando se le aplican 24V. ¿Cuál es su resistencia equivalente?*

```
R = V / I = 24 / 3.5 = 6.857 Ω
```

**Verificación**: I = V/R = 24/6.857 = 3.5 A ✓

### Ejemplo resuelto 3

*Si necesito limitar la corriente a 20 mA con una fuente de 5V, ¿qué resistencia necesito?*

```
R = V / I = 5 / 0.020 = 250 Ω
```

### ⚠️ Error común

La ley de Ohm se aplica **punto por punto**. En un circuito con múltiples componentes, V en la fórmula es el voltaje **específico** sobre **esa** resistencia, no necessarily el voltaje de la fuente.

---

## 2. Circuitos serie

### Definición

Un circuito serie es aquel donde todos los componentes están conectados uno tras otro, formando **un solo camino** para la corriente.

### Propiedades fundamentales

| **Propiedad** | **Fórmula** | **Explicación** |
|-----------|---------|-------------|
| Corriente | I_total = I₁ = I₂ = I₃ | La misma corriente en todos |
| Voltaje | V_total = V₁ + V₂ + V₃ | Se reparte entre los componentes |
| Resistencia | R_total = R₁ + R₂ + R₃ | Se suman directamente |
### ¿Por qué se suman las resistencias?

Cada resistencia "obstruye" el flujo. Si pones tres embudos en fila, la obstrucción total es la suma de las tres. Cada electrón tiene que pasar por todas las resistencias.

### Ejemplo resuelto

*En un circuito serie con R₁ = 100 Ω, R₂ = 220 Ω y R₃ = 330 Ω, conectado a 12V:*

**Paso 1**: Resistencia total
```
R_total = 100 + 220 + 330 = 650 Ω
```

**Paso 2**: Corriente del circuito (la misma en todos)
```
I = V / R_total = 12 / 650 = 0.01846 A = 18.46 mA
```

**Paso 3**: Voltaje en cada resistencia
```
V₁ = I × R₁ = 0.01846 × 100 = 1.846 V
V₂ = I × R₂ = 0.01846 × 220 = 4.061 V
V₃ = I × R₃ = 0.01846 × 330 = 6.092 V
```

**Verificación**: V_total = 1.846 + 4.061 + 6.092 = 11.999 V ≈ 12 V ✓

### Potencia en serie

```
P_total = P₁ + P₂ + P₃
P₁ = I² × R₁ = V₁² / R₁ = V₁ × I
```

### Aplicaciones reales

- Cadenas de luces navideñas (si se quema una, apagan todas)
- Resistencias limitadoras de corriente en serie con LEDs
- Fusibles siempre en serie con la carga

---

## 3. Circuitos paralelo

### Definición

Un circuito paralelo es aquel donde todos los componentes comparten los **mismos dos puntos** de conexión, creando **múltiples caminos** para la corriente.

### Propiedades fundamentales

| **Propiedad** | **Fórmula** | **Explicación** |
|-----------|---------|-------------|
| Voltaje | V_total = V₁ = V₂ = V₃ | El mismo voltaje en todos |
| Corriente | I_total = I₁ + I₂ + I₃ | Se reparte entre las ramas |
| Resistencia | 1/R_total = 1/R₁ + 1/R₂ + 1/R₃ | Se combinan inversamente |
### Resistencia equivalente (abreviación)

**Para dos resistencias** (la fórmula más usada):
```
R_eq = (R₁ × R₂) / (R₁ + R₂)
```

**Para resistencias iguales**:
```
R_eq = R / n    (donde n es el número de resistencias)
```

### ¿Por qué la resistencia total es MENOR que la menor individual?

Porque al abrir más caminos, la corriente total aumenta. Es como agregar carriles a una autopista: aunque cada carril individual tenga su propio flujo, el flujo total es mayor. Agregar más resistencias en paralelo siempre reduce la resistencia total.

### Ejemplo resuelto

*Tres resistencias en paralelo: R₁ = 100 Ω, R₂ = 200 Ω, R₃ = 400 Ω. Fuente de 24V.*

**Paso 1**: Resistencia total
```
1/R_total = 1/100 + 1/200 + 1/400
1/R_total = 0.01 + 0.005 + 0.0025
1/R_total = 0.0175
R_total = 1/0.0175 = 57.14 Ω
```

**Paso 2**: Corriente total
```
I_total = V / R_total = 24 / 57.14 = 0.42 A = 420 mA
```

**Paso 3**: Corriente en cada rama
```python
I₁ = V / R₁ = 24 / 100 = 0.24 A = 240 mA
I₂ = V / R₂ = 24 / 200 = 0.12 A = 120 mA
I₃ = V / R₃ = 24 / 400 = 0.06 A = 60 mA
```

**Verificación**: I_total = 240 + 120 + 60 = 420 mA ✓

### Aplicaciones reales

- Enchufes en una pared (todos reciben 110V/220V)
- Luces de una casa (cada luz se puede encender independientemente)
- La distribución eléctrica de un edificio

---

## 4. Circuitos mixtos (serie-paralelo)

### Definición

Los circuitos mixtos combinan elementos en serie y paralelo. Son los más comunes en la práctica real.

### Estrategia de resolución

**Paso a paso, de adentro hacia afuera:**

1. Identificar qué está en paralelo y qué en serie
2. Resolver los bloques paralelos primero (combíналos en una resistencia equivalente)
3. Resolver la serie con las resistencias resultantes
4. Calcular la corriente total
5. Ir "regresando" para encontrar voltajes y corrientes individuales

### Ejemplo resuelto completo

*Circuito: R₁ = 100Ω en serie con (R₂ = 200Ω ∥ R₃ = 300Ω). Fuente = 30V.*

**Paso 1**: Resolver la parte paralela
```
R₂₃ = (R₂ × R₃) / (R₂ + R₃) = (200 × 300) / (200 + 300) = 60000 / 500 = 120 Ω
```

**Paso 2**: Resistencia total (serie)
```
R_total = R₁ + R₂₃ = 100 + 120 = 220 Ω
```

**Paso 3**: Corriente total
```
I_total = V / R_total = 30 / 220 = 0.13636 A = 136.36 mA
```

**Paso 4**: Voltaje en cada parte
```
V₁ = I_total × R₁ = 0.13636 × 100 = 13.636 V
V₂₃ = I_total × R₂₃ = 0.13636 × 120 = 16.364 V
```

**Verificación**: V₁ + V₂₃ = 13.636 + 16.364 = 30.000 V ✓

**Paso 5**: Corriente en cada resistencia del paralelo
```python
I₂ = V₂₃ / R₂ = 16.364 / 200 = 0.08182 A = 81.82 mA
I₃ = V₂₃ / R₃ = 16.364 / 300 = 0.05455 A = 54.55 mA
```

**Verificación corriente**: I₂ + I₃ = 81.82 + 54.55 = 136.37 mA ≈ I_total ✓

### 💡 Tip

Cuando no estés seguro, dibuja el circuito con los colores de los cables. Colorea de rojo el nodo de mayor voltaje y de azul el de menor. Los componentes que conectan los mismos colores están en paralelo.

---

## 5. Ley de Kirchhoff de Corrientes (LCK)

### Definición

En cualquier nodo (punto de unión de conductores), la suma de corrientes que entran es igual a la suma de corrientes que salen.

### Fórmula

```
Σ I_entrada = Σ I_salida

O equivalentemente:
Σ I = 0  (tomando entrada como positiva y salida como negativa)
```

### Analogía

Un nodo es como una tubería T. Si por un extremo entran 10 litros/minuto y por el otro entran 5 litros/minuto, por el tercer extremo salen 15 litros/minuto. No se crea ni destruye agua.

### ¿Por qué funciona?

Porque la carga se conserva. Los electrones no aparecen ni desaparecen en un nodo. Todo lo que entra, sale.

### Ejemplo resuelto

*En un nodo entran 5A por la rama A y 3A por la rama B. ¿Cuánta corriente sale por la rama C?*

```python
I_A + I_B = I_C
5 + 3 = I_C
I_C = 8 A
```

### Ejemplo más complejo

*Un nodo tiene 4 ramas: I₁ = 10A (entra), I₂ = 4A (sale), I₃ = ? (entra), I₄ = 8A (sale)*

```python
I_entrada = I_salida
I₁ + I₃ = I₂ + I₄
10 + I₃ = 4 + 8
I₃ = 12 - 10 = 2 A (entra)
```

### Aplicación práctica

La LCK es la base del **análisis de mallas** y **análisis de nodos**, los métodos más poderosos para resolver cualquier circuito.

---

## 6. Ley de Kirchhoff de Voltajes (LKV)

### Definición

En cualquier malla (lazo cerrado) de un circuito, la suma algebraica de todos los voltajes es cero.

### Fórmula

```
Σ V = 0  (en una malla cerrada)

O equivalentemente:
Σ V_subidas = Σ V_caidas
```

### Convención de signos

| **Situación** | **Signo** | **Ejemplo** |
|-----------|-------|---------|
| De − a + (subida) | Positivo | Cruzar una fuente de − a + |
| De + a − (caída) | Negativo | Cruzar una resistencia en dirección de corriente |
| Con la corriente | Negativo (caída) | I × R positivo, pero se resta |
| Contra la corriente | Positivo (subida) | I × R se suma |
### Analogía

Si caminas en círculo por una montaña, la altura total que subes es igual a la altura total que bajas. Vuelves al mismo nivel.

### Ejemplo resuelto

*Una fuente de 12V alimenta dos resistencias en serie: R₁ = 300Ω y R₂ = 100Ω. Verificar la LKV.*

```
Malla: fuente → R₁ → R₂ → fuente

+12V - I×R₁ - I×R₂ = 0

Primero calculamos I:
I = 12 / (300+100) = 0.03 A

Verificación LKV:
+12 - (0.03×300) - (0.03×100) = 12 - 9 - 3 = 0 ✓
```

### Regla práctica

Recorre la malla en cualquier dirección. Cada vez que cruzas algo:
- **Fuente**: de − a + → sumas V; de + a − → restas V
- **Resistencia**: siempre resta I×R (por convención)

Si el resultado no es cero, hay un error de cálculo o de signos.

---

## 7. Divisor de voltaje

### Definición

El divisor de voltaje es una fórmula que permite calcular el voltaje sobre una resistencia en un circuito serie, sin calcular primero la corriente.

### Fórmula

```
V_x = V_total × (R_x / R_total)

Para dos resistencias en serie:
V₁ = V_total × R₁ / (R₁ + R₂)
V₂ = V_total × R₂ / (R₁ + R₂)
```

### ¿Por qué funciona?

En serie, la corriente es la misma en todas las resistencias. El voltaje se reparte proporcionalmente a la resistencia. Una resistencia más grande "atrapa" más voltaje.

### Analogía

Imagina una manguera con dos secciones de distinto diámetro. La sección más estrecha (mayor resistencia) tiene más caída de presión (voltaje).

### Ejemplo resuelto

*Fuente de 9V, R₁ = 1kΩ y R₂ = 2kΩ en serie. Calcular V sobre R₂.*

```
V₂ = 9 × 2000 / (1000 + 2000)
V₂ = 9 × 2000 / 3000
V₂ = 9 × 0.6667
V₂ = 6V
```

**Verificación**: V₁ = 9 × 1000/3000 = 3V. V₁ + V₂ = 3 + 6 = 9V ✓

### Aplicaciones reales

- Obtener un voltaje intermedio a partir de una fuente mayor
- Sensores de temperatura (termistores en divisor de voltaje)
- Referencias de voltaje en circuitos electrónicos

### ⚠️ Error común

El divisor de voltaje asume **carga infinita** (que nada conecta a la salida). Si conectas una carga en paralelo con R₂, la resistencia equivalente cambia y el voltaje también. En ese caso, primero calcula la Thevenin.

---

## 8. Divisor de corriente

### Definición

El divisor de corriente permite calcular la corriente que pasa por una rama de un circuito paralelo, sin calcular primero el voltaje.

### Fórmula

**Para dos resistencias en paralelo:**
```
I₁ = I_total × R₂ / (R₁ + R₂)
I₂ = I_total × R₁ / (R₁ + R₂)
```

**Para n resistencias en paralelo:**
```
I_x = I_total × R_eq / R_x
```

Donde R_eq es la resistencia equivalente de todas las resistencias en paralelo.

### ¿Por qué funciona?

En paralelo, el voltaje es el mismo. La corriente se reparte inversamente a la resistencia. La rama de menor resistencia "absorbe" más corriente.

### Ejemplo resuelto

*200mA se divide entre R₁ = 60Ω y R₂ = 40Ω en paralelo.*

```
I₁ = 200 × 40 / (60 + 40) = 200 × 40/100 = 80 mA
I₂ = 200 × 60 / (60 + 40) = 200 × 60/100 = 120 mA
```

**Verificación**: 80 + 120 = 200 mA ✓

### Nota importante

Observa que en el divisor de corriente, para calcular I₁ usas R₂ en el numerador (la otra resistencia). Es el **inverso** del divisor de voltaje.

---

## 9. Teorema de Thevenin

### Definición

Cualquier circuito lineal (con resistencias y fuentes) visto desde dos terminales, se puede reemplazar por una **única fuente de voltaje** en serie con una **única resistencia**.

```
Circuito complejo → V_Th en serie con R_Th → Carga
```

### Pasos para encontrar el circuito equivalente de Thevenin

**Paso 1 — Voltaje de Thevenin (V_Th):**
- Retira la carga del circuito
- Mide (o calcula) el voltaje en circuito abierto entre los dos terminales
- Ese voltaje es V_Th

**Paso 2 — Resistencia de Thevenin (R_Th):**
- Apaga todas las fuentes independientes:
  - Fuentes de voltaje → reemplaza por cortocircuito (cable)
  - Fuentes de corriente → reemplaza por circuito abierto
- Calcula la resistencia equivalente entre los dos terminales
- Esa resistencia es R_Th

**Paso 3 — Monta el circuito equivalente:**
- Pon V_Th en serie con R_Th
- Conecta la carga

### Analogía

Thevenin dice: "No me importa lo complicado que sea el circuito por dentro. Desde afuera, me ves como un voltaje y una resistencia."

### Ejemplo resuelto

*Fuente de 12V con R₁ = 4Ω en serie. Desde los terminales de la carga:*

```
V_Th = voltaje en circuito abierto = 12V (no hay corriente, no hay caída en R₁)

R_Th = resistencia con fuente cortocircuitada = 4Ω

Circuito equivalente: 12V en serie con 4Ω
```

Si ahora conectamos una carga de 8Ω:
```
I = V_Th / (R_Th + R_carga) = 12 / (4 + 8) = 1A
V_carga = I × R_carga = 1 × 8 = 8V
```

### ⚠️ Error común

No apagar las fuentes al calcular R_Th. Si olvidas cortocircuitar la fuente de voltaje, obtendrás un valor incorrecto.

---

## 10. Teorema de Norton

### Definición

El equivalente dual de Thevenin. Cualquier circuito lineal visto desde dos terminales se puede reemplazar por una **única fuente de corriente** en paralelo con una **única resistencia**.

```
Circuito complejo → I_N en paralelo con R_N → Carga
```

### Pasos para encontrar el circuito de Norton

**Paso 1 — Corriente de Norton (I_N):**
- Cortocircuita los dos terminales
- Mide (o calcula) la corriente por el cortocircuito
- Esa corriente es I_N

**Paso 2 — Resistencia de Norton (R_N):**
- Es la misma que R_Th (se calcula igual)
- R_N = R_Th

**Paso 3 — Relación con Thevenin:**
```
V_Th = I_N × R_N
I_N = V_Th / R_Th
R_N = R_Th
```

### Ejemplo resuelto

*El mismo circuito anterior: fuente 12V con R₁ = 4Ω*

```
I_N = corriente de cortocircuito = 12/4 = 3A
R_N = 4Ω (= R_Th)

Norton equivalente: 3A en paralelo con 4Ω
```

Si conectamos carga de 8Ω:
```
I_carga = I_N × R_N / (R_N + R_carga) = 3 × 4 / (4+8) = 12/12 = 1A ✓
V_carga = I_carga × R_carga = 1 × 8 = 8V ✓
```

Mismo resultado que Thevenin. Son equivalentes.

---

## 11. Transformación de fuentes

### Definición

Permite convertir una fuente de voltaje (V en serie con R) en una fuente de corriente (I en paralelo con R), y viceversa, sin cambiar el comportamiento del circuito.

### Fórmulas de conversión

```
De Thevenin a Norton:    I_N = V_Th / R
De Norton a Thevenin:    V_Th = I_N × R

La resistencia R es la misma en ambos casos.
```

### Ejemplo

*Fuente de 24V en serie con 6Ω*

```
I_N = 24/6 = 4A
R_N = 6Ω

Equivalente: 4A en paralelo con 6Ω
```

### ¿Cuándo se usa?

Cuando tienes un circuito con fuentes de voltaje y fuentes de corriente mezcladas. Transformando todo a un solo tipo, puedes resolver por reducción de serie/paralelo.

### ⚠️ Regla

Solo puedes transformar fuentes **independientes**. Las fuentes dependientes (controladas por otra variable del circuito) no se transforman directamente.

---

## 12. Teorema de superposición

### Definición

En un circuito con **múltiples fuentes independientes**, la corriente (o voltaje) en cualquier punto es la suma algebraica de las contribuciones de cada fuente actuando **individualmente**.

### Pasos

1. Deja **una sola fuente** activa
2. Apaga las demás:
   - Fuentes de voltaje → cortocircuito (cable)
   - Fuentes de corriente → circuito abierto
3. Calcula la corriente/voltaje deseado por esa fuente
4. Repite para cada fuente
5. Suma algebraicamente todos los resultados (respetando signos)

### Analogía

Imagina que dos personas empujan un carrito en direcciones diferentes. La fuerza total es la suma vectorial de cada empuje individual.

### Ejemplo resuelto

*Dos fuentes: V₁ = 10V (izq) y V₂ = 6V (der), con R₁ = 2Ω, R₂ = 3Ω, R₃ = 5Ω en el medio. Calcular corriente por R₃.*

**Solo V₁ activa (V₂ cortocircuitada):**
```
R_total = R₁ + (R₂ ∥ R₃) = 2 + (3×5)/(3+5) = 2 + 1.875 = 3.875Ω
I_total₁ = 10/3.875 = 2.581A
V_medio₁ = I_total₁ × (R₂∥R₃) = 2.581 × 1.875 = 4.839V
I_R3₁ = V_medio₁ / R₃ = 4.839/5 = 0.968A (de izq a der)
```

**Solo V₂ activa (V₁ cortocircuitada):**
```
R_total = R₂ + (R₁ ∥ R₃) = 3 + (2×5)/(2+5) = 3 + 1.429 = 4.429Ω
I_total₂ = 6/4.429 = 1.355A
V_medio₂ = I_total₂ × (R₁∥R₃) = 1.355 × 1.429 = 1.936V
I_R3₂ = V_medio₂ / R₃ = 1.936/5 = 0.387A (de der a izq)
```

**Resultado total:**
```
I_R3 = I_R3₁ - I_R3₂ = 0.968 - 0.387 = 0.581A (de izq a der)
```

### ⚠️ Error común

Sumar sin respetar la dirección. Si una contribución es de izquierda a derecha y la otra de derecha a izquierda, se restan. Siempre define un sentido positivo y mantenlo.

---

## 13. Transferencia de máxima potencia

### Definición

La potencia máxima se transfiere a la carga cuando la resistencia de carga es **igual** a la resistencia de Thevenin del circuito que la alimenta.

### Fórmula

```
Condición:     R_carga = R_Th
Potencia máx:  P_max = V_Th² / (4 × R_Th)
```

### Ejemplo

*Fuente de Thevenin: V_Th = 12V, R_Th = 100Ω*

```
Para máxima potencia: R_carga = 100Ω

P_max = 12² / (4 × 100) = 144 / 400 = 0.36 W = 360 mW
```

### ¿Cuándo se usa?

En sistemas de comunicación y audio donde se quiere maximizar la potencia entregada al altavoz o antena. **No** se usa en distribución eléctrica (donde se busca máxima eficiencia, no máxima potencia).

---

## 14. Análisis de mallas

### Definición

Método sistemático para resolver circuitos con múltiples mallas. Se escribe una ecuación de LKV para cada malla y se resuelve el sistema de ecuaciones.

### Procedimiento

1. Identifica todas las mallas (lazos independientes)
2. Asigna una corriente de malla a cada una (todas en sentido horario)
3. Escribe la LKV para cada malla
4. Resuelve el sistema de ecuaciones

### Formato de ecuación

```
Para cada malla:
(resistencias de la malla) × I_malla - (resistencias compartidas) × I_vecina = fuentes en la malla
```

Las fuentes suman si entran con la corriente de malla, restan si van en contra.

### Ejemplo resuelto

*Dos mallas: R₁ = 10Ω (malla 1), R₂ = 20Ω (malla 2), R₃ = 30Ω (compartida). V₁ = 12V (malla 1), V₂ = 6V (malla 2).*

```python
Malla 1: (R₁ + R₃)I₁ - R₃·I₂ = V₁
         40·I₁ - 30·I₂ = 12    ... (ecuación 1)

Malla 2: -R₃·I₁ + (R₂ + R₃)I₂ = -V₂
         -30·I₁ + 50·I₂ = -6   ... (ecuación 2)
```

Resolviendo (multiplicar ec.1 por 5/3):
```
66.67·I₁ - 50·I₂ = 20
-30·I₁ + 50·I₂ = -6
─────────────────────
36.67·I₁ = 14
I₁ = 0.382 A

I₂ = (30×0.382 - 6)/50 = (11.46-6)/50 = 0.109 A
```

---

## 15. Análisis de nodos

### Definición

Método que usa la LCK para resolver circuitos. Se expresa cada corriente en función de los voltajes de los nodos y se resuelve el sistema.

### Procedimiento

1. Elige un nodo como referencia (tierra, 0V)
2. Asigna voltajes desconocidos a los demás nodos
3. Escribe la LCK para cada nodo no referencia
4. Expresa cada corriente como (V_nodo - V_vecino) / R
5. Resuelve el sistema

### Ejemplo resuelto

*Dos nodos: N₁ con V₁ = ?, N₂ (referencia = 0V). R₁ = 10Ω entre N₁ y N₂. Fuente de 5A entrando a N₁. R₂ = 20Ω entre N₁ y tierra.*

```
Nodo N₁:
I_fuente = (V₁ - 0)/R₁ + (V₁ - 0)/R₂
5 = V₁/10 + V₁/20
5 = V₁(1/10 + 1/20)
5 = V₁(3/20)
V₁ = 5 × 20/3 = 33.33V
```

### Cuándo usar mallas vs nodos

| **Situación** | **Mejor método** |
|-----------|-------------|
| Pocas mallas, muchas ramas | Mallas |
| Pocos nodos, muchas ramas | Nodos |
| Fuentes de voltaje dominantes | Mallas |
| Fuentes de corriente dominantes | Nodos |
---

## 16. Ley de Joule y efecto térmico

### Definición

Cuando una corriente circula por un conductor con resistencia, se genera calor. Esta energía térmica es la base del funcionamiento de calentadores, fusibles y también la causa del sobrecalentamiento en cables.

### Fórmulas

```
Q = I² × R × t       (Joules de calor generado)
Q = V × I × t        (si conoces V)
Q = V² × t / R       (si conoces V y R)

Potencia disipada como calor:
P = I² × R           (Watts)
```

Donde:
- Q = energía térmica (Joules, J)
- I = corriente (A)
- R = resistencia (Ω)
- t = tiempo (s)

### Analogía

Es como la fricción cuando frotas tus manos: la resistencia al movimiento genera calor. A mayor presión (voltaje), más corriente fluye, más fricción hay, más calor se genera.

### Ejemplo resuelto

*Un cable de 2.5Ω lleva 15A durante 10 minutos. ¿Cuánto calor se genera?*

```
Q = I² × R × t = 15² × 2.5 × (10×60)
Q = 225 × 2.5 × 600
Q = 337,500 J = 337.5 kJ

P = I² × R = 225 × 2.5 = 562.5 W
```

### Aplicaciones

| **Aplicación** | **Principio** |
|------------|-----------|
| Calentadores eléctricos | I²R en resistencias de alta R |
| Fusibles | Se funden cuando I²R alcanza cierta temperatura |
| Soldadura por arco | I²R genera calor extremo en el arco |
| Cables (pérdidas) | I²R es una pérdida indeseada |
### Regla del cuadrado

Observa que la corriente influye al **cuadrado**. Si duplicas la corriente, las pérdidas por calor se **cuadruplican**. Por eso los cables de alta corriente son gruesos: para reducir R y minimizar I²R.

---

## 17. Capacitores en CD

### ¿Qué es un capacitor?

Un capacitor es un dispositivo que almacena energía en un **campo eléctrico**. Consiste en dos placas conductoras separadas por un material dieléctrico (aislante).

### Analogía

Un capacitor es como un **tanque de agua con émbolo**:
- Cuando aplicas presión (voltaje), el émbolo se mueve y almacena agua (carga)
- Cuando quitas la presión, el émbolo puede liberar el agua (descargar)
- La capacidad es el tamaño del tanque

### Fórmulas fundamentales

```
C = Q / V           (definición de capacitancia)
Q = C × V           (carga almacenada)
E = ½ × C × V²      (energía almacenada)
E = Q² / (2 × C)    (energía en función de carga)
```

Donde:
- C = capacitancia (Faradios, F)
- Q = carga almacenada (Coulombs, C)
- V = voltaje entre las placas (V)
- E = energía (Joules, J)

### Unidad de medida

- **Faradio (F)**: capacidad de almacenar 1 Coulomb con 1 Voltio
- 1F es enorme. Se usan subdivisiones: μF (×10⁻⁶), nF (×10⁻⁹), pF (×10⁻¹²)

### Capacitancia de un capacitor de placas paralelas

```
C = ε₀ × εᵣ × A / d

Donde:
  ε₀ = 8.854 × 10⁻¹² F/m (permitividad del vacío)
  εᵣ = permitividad relativa del dieléctrico
  A = área de las placas (m²)
  d = distancia entre placas (m)
```

### Capacitores en serie

```
1/C_total = 1/C₁ + 1/C₂ + 1/C₃ + ...
```

**Nota**: ¡Es al revés que las resistencias! Para capacitores en serie, la capacidad total es **menor** que la menor individual.

### Capacitores en paralelo

```
C_total = C₁ + C₂ + C₃ + ...
```

Se suman directamente (al revés que las resistencias).

### Comportamiento en CD (regímenes)

| **Momento** | **Capacitor** | **Corriente** |
|---------|-----------|-----------|
| Al conectar (t = 0) | Descargado, actúa como cortocircuito | Máxima: I = V/R |
| Estado estacionario (t → ∞) | Cargado, actúa como circuito abierto | Cero: I = 0 |
### Ejemplo resuelto

*Un capacitor de 100μF se carga a 50V. ¿Cuánta energía almacena?*

```
E = ½ × C × V² = ½ × 100×10⁻⁶ × 50²
E = ½ × 0.0001 × 2500
E = 0.125 J = 125 mJ
```

---

## 18. Inductores en CD

### ¿Qué es un inductor?

Un inductor es un dispositivo que almacena energía en un **campo magnético**. Consiste en una bobina de alambre enrollado, frecuentemente alrededor de un núcleo ferromagnético.

### Analogía

Un inductor es como una **turbina en una tubería de agua**:
- Al abrir la llave, la turbina tiene inercia y tarda en acelerarse (la corriente crece lentamente)
- Una vez girando, mantiene el flujo (la corriente se mantiene)
- Al cerrar la llave, la turbina sigue girando por inercia (genera un pico de voltaje)

### Fórmulas fundamentales

```
V = L × (di/dt)     (voltaje en función del cambio de corriente)
E = ½ × L × I²      (energía almacenada)
```

Donde:
- L = inductancia (Henrios, H)
- I = corriente (A)
- di/dt = tasa de cambio de corriente (A/s)
- E = energía (J)

### Unidad de medida

- **Henrio (H)**: genera 1V cuando la corriente cambia a 1A/s
- Se usan subdivisiones: mH (×10⁻³), μH (×10⁻⁶)

### Comportamiento en CD

| **Momento** | **Inductor** | **Voltaje** |
|---------|----------|---------|
| Al conectar (t = 0) | Se opone al cambio, actúa como circuito abierto | Máximo: V = L×(di/dt) |
| Estado estacionario (t → ∞) | Actúa como cortocircuito (solo su resistencia interna) | Casi cero |
### Inductores en serie

```
L_total = L₁ + L₂ + L₃ + ...
```

Se suman directamente (igual que las resistencias).

### Inductores en paralelo

```
1/L_total = 1/L₁ + 1/L₂ + 1/L₃ + ...
```

Igual que los capacitores en serie.

### Ejemplo resuelto

*Un inductor de 50mH lleva 4A. ¿Cuánta energía almacena?*

```
E = ½ × L × I² = ½ × 0.050 × 4²
E = ½ × 0.050 × 16
E = 0.4 J = 400 mJ
```

---

## 19. Circuitos RC en CD (transitorio)

### ¿Qué es un transitorio?

Cuando cambias algo en un circuito (conectar o desconectar una fuente), el circuito no cambia instantáneamente. Hay un **período de transición** donde voltajes y corrientes cambian gradualmente. Eso es el transitorio.

### Circuito RC cargándose

*Un capacitor se carga a través de una resistencia desde una fuente V.*

```
Voltaje en el capacitor:
  v_C(t) = V × (1 - e^(-t/RC))

Corriente en el circuito:
  i(t) = (V/R) × e^(-t/RC)
```

### Circuito RC descargándose

*Un capacitor cargado se descarga a través de una resistencia.*

```
Voltaje en el capacitor:
  v_C(t) = V₀ × e^(-t/RC)

Corriente en el circuito:
  i(t) = -(V₀/R) × e^(-t/RC)
```

### Tabla de valores (cargando)

| **Tiempo (τ)** | **v_C (% de V final)** | **i (% de I inicial)** |
|------------|--------------------|--------------------|
| 0 | 0% | 100% |
| 1τ | 63.2% | 36.8% |
| 2τ | 86.5% | 13.5% |
| 3τ | 95.0% | 5.0% |
| 4τ | 98.2% | 1.8% |
| 5τ | 99.3% | 0.7% |
> **Regla práctica**: Después de 5τ, se considera que el capacitor está cargado (99.3%).

### Ejemplo resuelto

*R = 10kΩ, C = 100μF. Fuente de 12V. ¿Cuánto tarda en cargarse al 95%?*

```
τ = R × C = 10000 × 100×10⁻⁶ = 1 s

Para 95%: t = 3τ = 3 segundos
```

**Verificación**: v_C(3) = 12 × (1 - e⁻³) = 12 × (1 - 0.0498) = 12 × 0.9502 = 11.40V ≈ 95% de 12V ✓

---

## 20. Circuitos RL en CD (transitorio)

### Circuito RL energizándose

*Un inductor se energiza a través de una resistencia desde una fuente V.*

```
Corriente en el inductor:
  i_L(t) = (V/R) × (1 - e^(-Rt/L))

Voltaje en el inductor:
  v_L(t) = V × e^(-Rt/L)
```

### Circuito RL desenergizándose

*Un inductor con corriente se descarga a través de una resistencia.*

```
Corriente en el inductor:
  i_L(t) = I₀ × e^(-Rt/L)

Voltaje en la resistencia:
  v_R(t) = I₀ × R × e^(-Rt/L)
```

### Tabla de valores (energizando)

| **Tiempo (τ)** | **i_L (% de I final)** | **v_L (% de V inicial)** |
|------------|--------------------|--------------------|
| 0 | 0% | 100% |
| 1τ | 63.2% | 36.8% |
| 2τ | 86.5% | 13.5% |
| 3τ | 95.0% | 5.0% |
| 4τ | 98.2% | 1.8% |
| 5τ | 99.3% | 0.7% |
Observa: ¡Las tablas son idénticas a las del RC! La forma matemática es la misma, solo cambia la constante de tiempo.

---

## 21. Constante de tiempo (τ)

### Definición

La constante de tiempo indica **qué tan rápido** responde un circuito RC o RL a cambios. Es una medida de la velocidad del transitorio.

### Fórmulas

```
Circuito RC:  τ = R × C    (segundos)
Circuito RL:  τ = L / R    (segundos)
```

Donde:
- τ = constante de tiempo (s)
- R = resistencia (Ω)
- C = capacitancia (F)
- L = inductancia (H)

### Interpretación física

- **τ grande** = circuito lento (tarda mucho en estabilizarse)
- **τ pequeña** = circuito rápido (se estabiliza casi instantáneamente)
- En 1τ, la variable alcanza el 63.2% de su valor final
- En 5τ, se considera estabilizado (>99%)

### Ejemplo práctico

*¿Cuánto tiempo tarda en estabilizarse un circuito RC con R = 47kΩ y C = 10μF?*

```
τ = R × C = 47000 × 10×10⁻⁶ = 0.47 s

Tiempo de estabilización = 5τ = 5 × 0.47 = 2.35 segundos
```

### Aplicaciones

| **Circuito** | **Uso de τ** |
|----------|---------|
| Filtro RC pasabajo | τ determina la frecuencia de corte |
| Retardos temporales | τ controla el tiempo de espera |
| Integradores | τ >> período de la señal |
| Diferenciadores | τ << período de la señal |
| Arranque de motores | τ del circuito de excitación |
---

## Resumen de Corriente Directa

```
┌─────────────────────────────────────────────────────────────┐
│                    CORRIENTE DIRECTA                         │
│                                                             │
│  Ley de Ohm:           V = I × R                            │
│                                                             │
│  Serie:                R_t = R₁+R₂+R₃    I = igual          │
│  Paralelo:             1/R_t = 1/R₁+1/R₂  V = igual        │
│                                                             │
│  Kirchhoff:            ΣI_nodo = 0    ΣV_malla = 0          │
│                                                             │
│  Divisor voltaje:      V₂ = V × R₂/(R₁+R₂)                 │
│  Divisor corriente:    I₁ = I × R₂/(R₁+R₂)                 │
│                                                             │
│  Thevenin:             V_Th + R_Th (serie)                   │
│  Norton:               I_N + R_N (paralelo)                  │
│                                                             │
│  Superposición:        Suma de contribuciones individuales   │
│                                                             │
│  Joule:                P = I²R  (calor)                      │
│                                                             │
│  Capacitor:            C = Q/V, E = ½CV²                     │
│  Inductor:             V = L(di/dt), E = ½LI²               │
│                                                             │
│  Transitorio:          τ = RC o τ = L/R                      │
│                        Después de 5τ → estabilizado          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Siguiente

Ahora pasamos a [Corriente Alterna](02-corriente-alterna.md), donde todo esto se complejiza con el concepto de impedancia, fasores, potencia reactiva y sistemas trifásicos.
