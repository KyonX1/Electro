# Corriente Directa

La corriente directa (DC) es el flujo de carga en una sola dirección a través de un circuito. A diferencia de la corriente alterna, la magnitud y el sentido de la corriente continua permanecen constantes en régimen permanente, lo que simplifica considerablemente el análisis de redes resistivas. Este capítulo desarrolla las herramientas fundamentales para el análisis de circuitos DC: asociaciones de resistencias, leyes de Kirchhoff, teoremas de equivalencia, métodos sistemáticos de resolución, comportamiento transitorio de condensadores e inductores, y la instrumentación empleada para su medición [@boylestad2023, cap. 5].

El dominio de estos conceptos es prerrequisito para el estudio de la corriente alterna (Capítulo 3) y de las máquinas eléctricas (Capítulo 4), donde las técnicas de Thévenin y Norton se aplican nuevamente sobre circuitos con impedancias [@alexander2021, cap. 2].

---

## Circuitos en Serie y en Paralelo

### Resistencias en Serie

Dos o más resistencias están en serie cuando por ellas circula exactamente la misma corriente, es decir, cuando están conectadas una a continuación de la otra sin derivaciones intermedias. La resistencia equivalente de $n$ resistencias en serie es la suma de sus valores:

$$R_{eq} = R_1 + R_2 + \dots + R_n = \sum_{i=1}^{n} R_i$$

La resistencia equivalente en serie siempre es **mayor** que la mayor de las resistencias individuales. El voltaje total se reparte entre las resistencias en proporción directa a su valor.

| **Propiedad** | **Comportamiento en serie** |
| :-----------: | :-------------------------: |
| Corriente | Igual en todas las resistencias |
| :-----------: | :-------------------------: |
| Voltaje | Se reparte: $V_i = I R_i$ |
| :-----------: | :-------------------------: |
| Potencia | $P_i = I^2 R_i$, la mayor se disipa en la mayor resistencia |
| :-----------: | :-------------------------: |
| Resistencia equivalente | Suma de todas: $R_{eq} = \sum R_i$ |
| :-----------: | :-------------------------: |

```python
# Resistencias en serie: R_eq y reparto de voltaje
R = [100.0, 220.0, 330.0]   # ohm
V_total = 12.0
R_eq = sum(R)
I = V_total / R_eq
print(f"R_eq = {R_eq:.1f} ohm")
print(f"I = {I*1000:.2f} mA")
for i, Ri in enumerate(R, 1):
    print(f"V_{i} = {I*Ri:.3f} V, P_{i} = {I**2*Ri:.3f} W")
```

### Resistencias en Paralelo

Dos o más resistencias están en paralelo cuando comparten los mismos dos nodos y, por tanto, soportan el mismo voltaje. La resistencia equivalente se obtiene con la suma de las conductancias:

$$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots + \frac{1}{R_n}$$

Para dos resistencias, la expresión se simplifica al producto sobre la suma:

$$R_{eq} = \frac{R_1 R_2}{R_1 + R_2}$$

La resistencia equivalente en paralelo siempre es **menor** que la menor de las resistencias individuales. La corriente total se reparte en proporción inversa a los valores de resistencia.

```python
# Resistencias en paralelo
R1, R2, R3 = 100.0, 220.0, 330.0   # ohm
R_eq = 1 / (1/R1 + 1/R2 + 1/R3)
print(f"R_eq = {R_eq:.2f} ohm")
# Caso especial dos resistencias
R2eq = R1 * R2 / (R1 + R2)
print(f"R1||R2 = {R2eq:.2f} ohm")
```

| **Propiedad** | **Comportamiento en paralelo** |
| :-----------: | :----------------------------: |
| Voltaje | Igual en todas las resistencias |
| :-----------: | :----------------------------: |
| Corriente | Se reparte: $I_i = V/R_i$ |
| :-----------: | :----------------------------: |
| Potencia | $P_i = V^2/R_i$, la mayor se disipa en la menor resistencia |
| :-----------: | :----------------------------: |
| Resistencia equivalente | Menor que la más pequeña |
| :-----------: | :----------------------------: |

> **Nota:** Cuando se conectan resistencias en paralelo, la resistencia equivalente tiende al valor de la menor resistencia. Para $n$ resistencias iguales de valor $R$, la equivalente es $R/n$.

### Redes Serie-Paralelo

La mayoría de los circuitos prácticos combinan asociaciones en serie y en paralelo. La estrategia de reducción consiste en identificar pares de resistencias claramente en serie o en paralelo, reemplazarlos por su equivalente y repetir el proceso hasta obtener una sola resistencia [@alexander2021, cap. 2].

```python
# Red reducible: R1 y R2 en serie, ambas en paralelo con R3
R1, R2, R3 = 100.0, 200.0, 300.0
R_serie = R1 + R2
R_eq = R_serie * R3 / (R_serie + R3)
print(f"R_serie = {R_serie:.1f} ohm")
print(f"R_eq = {R_eq:.2f} ohm")
V = 12.0
I_total = V / R_eq
I_rama1 = V / R_serie
I_rama2 = V / R3
print(f"I_total = {I_total*1000:.2f} mA")
print(f"I_rama serie = {I_rama1*1000:.2f} mA, I_rama R3 = {I_rama2*1000:.2f} mA")
```

**Procedimiento general de reducción:**

| **Paso** | **Accion** |
| :------: | :---------: |
| 1 | Identificar resistencias en serie pura y reemplazarlas por su suma |
| :------: | :---------: |
| 2 | Identificar resistencias en paralelo puro y reemplazarlas por su equivalente |
| :------: | :---------: |
| 3 | Repetir hasta obtener una sola resistencia vista desde los terminales |
| :------: | :---------: |
| 4 | Calcular la corriente total con la ley de Ohm |
| :------: | :---------: |
| 5 | Expandir de regreso para hallar voltajes y corrientes parciales |
| :------: | :---------: |

---

## Leyes de Kirchhoff

Las leyes de Kirchhoff son los postulados fundamentales del análisis de circuitos. Se derivan de la conservación de la carga y de la energía, y son válidas para cualquier circuito, lineal o no lineal, en DC o en AC [@boylestad2023, cap. 6].

### Ley de Corrientes de Kirchhoff (KCL)

La ley de corrientes de Kirchhoff establece que la suma algebraica de las corrientes que entran a un nodo es cero:

$$\sum_{k=1}^{n} I_k = 0$$

Equivalentemente, la suma de las corrientes que entran es igual a la suma de las que salen. La ley expresa la conservación de la carga: la carga no se acumula en un nodo.

```python
# KCL en un nodo con tres ramas
I_entran = 5.0 + 3.0      # A
I_salen = 8.0             # A
print(f"I_entran = {I_entran:.1f} A, I_salen = {I_salen:.1f} A")
print(f"Balance: {I_entran - I_salen:.2f} A (debe ser 0)")
```

### Ley de Voltajes de Kirchhoff (KVL)

La ley de voltajes de Kirchhoff establece que la suma algebraica de las diferencias de potencial a lo largo de cualquier trayectoria cerrada (malla) es cero:

$$\sum_{k=1}^{n} V_k = 0$$

La ley expresa la conservación de la energía: al recorrer una malla cerrada, el potencial vuelve a su valor inicial.

```python
# KVL en una malla: V = 12 V, R1 = 100 ohm, R2 = 200 ohm
V = 12.0
R1, R2 = 100.0, 200.0
I = V / (R1 + R2)
V_R1 = I * R1
V_R2 = I * R2
print(f"V_R1 = {V_R1:.2f} V, V_R2 = {V_R2:.2f} V")
print(f"KVL: {V} - {V_R1:.2f} - {V_R2:.2f} = {V - V_R1 - V_R2:.2f} V")
```

### Convención de Signos

Para aplicar KVL correctamente se elige un sentido de recorrido y se asignan signos:

| **Elemento** | **Polaridad encontrada al recorrer** | **Signo en la ecuacion** |
| :----------: | :----------------------------------: | :----------------------: |
| Resistor | $+$ a $-$ (caída) | Negativo |
| :----------: | :----------------------------------: | :----------------------: |
| Resistor | $-$ a $+$ (elevación) | Positivo |
| :----------: | :----------------------------------: | :----------------------: |
| Fuente | $-$ a $+$ (elevación) | Positivo |
| :----------: | :----------------------------------: | :----------------------: |
| Fuente | $+$ a $-$ (caída) | Negativo |
| :----------: | :----------------------------------: | :----------------------: |

### Ejemplo Resuelto: Malla Simple

Considere una malla con $V = 24$ V, $R_1 = 100$ ohm y $R_2 = 300$ ohm en serie. Aplicando KVL en sentido horario:

$$-V + V_{R_1} + V_{R_2} = 0 \qquad \Rightarrow \qquad V = I(R_1 + R_2)$$

$$I = \frac{V}{R_1 + R_2} = \frac{24}{400} = 60\ \text{mA}$$

```python
V = 24.0
R1, R2 = 100.0, 300.0
I = V / (R1 + R2)
print(f"I = {I*1000:.1f} mA")
print(f"V_R1 = {I*R1:.2f} V, V_R2 = {I*R2:.2f} V")
print(f"P_R1 = {I**2*R1:.3f} W, P_R2 = {I**2*R2:.3f} W, P_total = {I**2*(R1+R2):.3f} W")
```

---

## Divisores de Voltaje y de Corriente

Los divisores son aplicaciones directas de las leyes de Kirchhoff que permiten obtener un voltaje o una corriente fraccionaria sin resolver el circuito completo [@boylestad2023, cap. 5].

### Divisor de Voltaje

Una serie de resistencias conectada a una fuente $V$ reparte el voltaje en proporción a cada resistencia:

$$V_i = V \frac{R_i}{R_1 + R_2 + \dots + R_n}$$

Para dos resistencias:

$$V_1 = V \frac{R_1}{R_1 + R_2} \qquad V_2 = V \frac{R_2}{R_1 + R_2}$$

**Divisor cargado:** si se conecta una carga $R_L$ en paralelo con $R_2$, el voltaje de salida disminuye:

$$V_{out} = V \frac{R_2 \parallel R_L}{R_1 + (R_2 \parallel R_L)}$$

```python
# Divisor de voltaje sin y con carga
V = 12.0
R1, R2 = 1000.0, 2000.0
V_out = V * R2 / (R1 + R2)
print(f"V_out sin carga = {V_out:.2f} V")
# Con carga RL = 1 kohm en paralelo con R2
RL = 1000.0
R2L = R2 * RL / (R2 + RL)
V_out_cargado = V * R2L / (R1 + R2L)
print(f"V_out con RL = 1k = {V_out_cargado:.2f} V")
print(f"Reduccion = {100*(1 - V_out_cargado/V_out):.1f}%")
```

### Divisor de Corriente

En un paralelo, la corriente total se reparte en proporción inversa a las resistencias. Para dos resistencias:

$$I_1 = I_{total} \frac{R_2}{R_1 + R_2} \qquad I_2 = I_{total} \frac{R_1}{R_1 + R_2}$$

La corriente circula preferentemente por la rama de menor resistencia.

```python
# Divisor de corriente de dos ramas
I_total = 50e-3         # 50 mA
R1, R2 = 100.0, 400.0
I1 = I_total * R2 / (R1 + R2)
I2 = I_total * R1 / (R1 + R2)
print(f"I1 = {I1*1000:.2f} mA, I2 = {I2*1000:.2f} mA")
print(f"Suma = {(I1+I2)*1000:.2f} mA (KCL)")
```

| **Divisor** | **Formula** | **Uso tipico** |
| :---------: | :---------: | :------------: |
| Voltaje | $V_i = V \frac{R_i}{\sum R}$ | Sensores, referencias |
| :---------: | :---------: | :------------: |
| Corriente | $I_i = I \frac{R_{otra}}{\sum R}$ | Amperimetros, derivadores |
| :---------: | :---------: | :------------: |

> **Nota:** Un divisor de voltaje ideal debe operar con una carga mucho mayor que la resistencia de salida ($R_L \gg R_2$), de lo contrario el voltaje de salida cae apreciablemente.

---

## Teoremas de Circuitos

Los teoremas de equivalencia permiten simplificar redes complejas en circuitos elementales desde el punto de vista de una carga específica [@alexander2021, cap. 4].

### Teorema de Thévenin

Cualquier red lineal de fuentes y resistencias, vista desde dos terminales $a$-$b$, puede reemplazarse por una fuente de voltaje $V_{th}$ en serie con una resistencia $R_{th}$:

- **Tensión de Thévenin** $V_{th}$: voltaje en circuito abierto entre $a$ y $b$.
- **Resistencia de Thévenin** $R_{th}$: resistencia equivalente entre $a$ y $b$ con todas las fuentes independientes apagadas (fuentes de voltaje en cortocircuito, fuentes de corriente en circuito abierto).

```python
# Ejemplo: circuito con V = 24 V, R1 = 100 ohm en serie, R2 = 300 ohm entre a-b
V = 24.0
R1, R2 = 100.0, 300.0
# V_th = voltaje en circuito abierto sobre R2 (divisor)
V_th = V * R2 / (R1 + R2)
# R_th = R1 || R2 con la fuente apagada (cortocircuito)
R_th = R1 * R2 / (R1 + R2)
print(f"V_th = {V_th:.2f} V, R_th = {R_th:.2f} ohm")
# Corriente en una carga RL conectada
RL = 150.0
I_L = V_th / (R_th + RL)
print(f"I_RL = {I_L*1000:.2f} mA")
```

### Teorema de Norton

Alternativamente, la misma red puede representarse como una fuente de corriente $I_N$ en paralelo con una resistencia $R_N$:

- **Corriente de Norton** $I_N$: corriente de cortocircuito entre $a$ y $b$.
- **Resistencia de Norton** $R_N$: igual a la resistencia de Thévenin $R_N = R_{th}$.

```python
# Continuacion del ejemplo anterior
I_N = V_th / R_th          # corriente de cortocircuito
R_N = R_th
print(f"I_N = {I_N*1000:.2f} mA, R_N = {R_N:.2f} ohm")
```

### Relación Thévenin-Norton

Ambos teoremas son equivalentes y se relacionan por la transformación de fuente:

$$V_{th} = I_N R_N \qquad I_N = \frac{V_{th}}{R_{th}} \qquad R_{th} = R_N$$

| **Equivalente** | **Fuente** | **Elemento en serie/paralelo** | **Uso** |
| :-------------: | :--------: | :---------------------------: | :-----: |
| Thévenin | Voltaje $V_{th}$ | En serie: $R_{th}$ | Análisis de carga en serie |
| :-------------: | :--------: | :---------------------------: | :-----: |
| Norton | Corriente $I_N$ | En paralelo: $R_N$ | Análisis de carga en paralelo |
| :-------------: | :--------: | :---------------------------: | :-----: |

### Teorema de Superposición

En un circuito lineal con múltiples fuentes independientes, la respuesta (voltaje o corriente) en cualquier elemento es la suma algebraica de las respuestas producidas por cada fuente actuando sola, con las demás fuentes apagadas.

```python
# Superposicion: dos fuentes de voltaje
# Fuente 1: V1 = 12 V, R1 serie = 100 ohm, R2 = 200 ohm
# Fuente 2: V2 = 6 V en paralelo con R2 (lado derecho)
V1, V2 = 12.0, 6.0
R1, R2 = 100.0, 200.0
# Contribucion de V1 (V2 en corto): V_R2' = V1 * R2/(R1+R2)
V_R2_1 = V1 * R2 / (R1 + R2)
# Contribucion de V2 (V1 en corto): V_R2'' = V2 * R1/(R1+R2)
V_R2_2 = V2 * R1 / (R1 + R2)
V_R2 = V_R2_1 + V_R2_2
print(f"V_R2' = {V_R2_1:.2f} V, V_R2'' = {V_R2_2:.2f} V")
print(f"V_R2 total = {V_R2:.2f} V")
```

### Máxima Transferencia de Potencia

Una fuente con resistencia interna $R_{th}$ entrega la máxima potencia a una carga $R_L$ cuando la resistencia de carga es igual a la resistencia interna:

$$R_L = R_{th}$$

La potencia máxima entregada es:

$$P_{max} = \frac{V_{th}^2}{4 R_{th}}$$

```python
V_th, R_th = 18.0, 50.0
R_L = R_th
P_max = V_th**2 / (4 * R_th)
I_L = V_th / (R_th + R_L)
print(f"R_L optima = {R_L:.1f} ohm")
print(f"P_max = {P_max:.2f} W")
print(f"I_L = {I_L*1000:.1f} mA")
# Eficiencia en el punto de maxima potencia
P_fuente = V_th * I_L
print(f"Eficiencia = {100*P_max/P_fuente:.1f}% (50% en este punto)")
```

> **Nota:** La máxima transferencia de potencia implica una eficiencia de solo el 50%. En sistemas de potencia se busca la máxima eficiencia (carga mucho mayor que la resistencia interna), mientras que en comunicaciones se busca la máxima transferencia.

---

## Análisis de Mallas y Nodos

Para circuitos con más de una malla, los métodos de mallas y nodos proporcionan un procedimiento sistemático basado en KVL y KCL respectivamente [@alexander2021, cap. 3].

### Método de Mallas (KVL)

Se asigna una corriente de malla a cada lazo cerrado independiente y se plantea KVL en cada uno. Para un circuito con $n$ mallas se obtiene un sistema de $n$ ecuaciones lineales.

$$R_{11} i_1 - R_{12} i_2 - \dots = V_1$$

```python
# Metodo de mallas: dos mallas acopladas por R_x
# Malla 1: V1=10V, R1=100, luego Rx=200 compartida con malla 2
# Malla 2: V2=5V, R2=150
import numpy as np

V1, V2 = 10.0, 5.0
R1, Rx, R2 = 100.0, 200.0, 150.0
A = np.array([[R1 + Rx, -Rx], [-Rx, R2 + Rx]])
b = np.array([V1, V2])
i = np.linalg.solve(A, b)
print(f"i1 = {i[0]*1000:.2f} mA, i2 = {i[1]*1000:.2f} mA")
print(f"I en Rx = {(i[0]-i[1])*1000:.2f} mA")
```

### Método de Nodos (KCL)

Se elige un nodo de referencia (tierra) y se plantea KCL en los nodos restantes, expresando las corrientes como $I = V/R$ o como conductancias $G = 1/R$:

$$G_{11} v_1 - G_{12} v_2 - \dots = I_{fuente}$$

```python
# Metodo de nodos: dos nodos con fuente de corriente
# Nodo 1: Is = 50 mA, G1 = 1/100, G12 = 1/200
# Nodo 2: G2 = 1/150
Is = 50e-3
G1, G12, G2 = 1/100.0, 1/200.0, 1/150.0
A = np.array([[G1 + G12, -G12], [-G12, G2 + G12]])
b = np.array([Is, 0.0])
v = np.linalg.solve(A, b)
print(f"v1 = {v[0]:.3f} V, v2 = {v[1]:.3f} V")
print(f"I_12 = {(v[0]-v[1])*G12*1000:.2f} mA")
```

### Comparación de Métodos

| **Metodo** | **Base** | **Incognitas** | **Mejor cuando** |
| :--------: | :------: | :------------: | :--------------: |
| Mallas | KVL | Corrientes de malla | Predominan fuentes de voltaje |
| :--------: | :------: | :------------: | :--------------: |
| Nodos | KCL | Voltajes de nodo | Predominan fuentes de corriente |
| :--------: | :------: | :------------: | :--------------: |
| Reduccion | Ohm + Kirchhoff | Variable unica | Circuitos reducibles |
| :--------: | :------: | :------------: | :--------------: |
| Thévenin/Norton | Equivalencia | Variables en la carga | Carga variable |
| :--------: | :------: | :------------: | :--------------: |

---

## Condensadores en Corriente Directa

### Comportamiento en Régimen Permanente

En régimen permanente DC, un condensador se comporta como un **circuito abierto**: $I_C = 0$ y el voltaje entre sus placas es constante. Durante los transitorios, la relación voltaje-corriente es:

$$I_C = C \frac{dV_C}{dt}$$

El condensador se opone a los cambios bruscos de voltaje: el voltaje en un condensador **no puede cambiar instantáneamente** [@alexander2021, cap. 6].

### Circuito RC de Carga

Al cerrar el interruptor en un circuito RC serie con la fuente $V$, el voltaje del condensador crece exponencialmente:

$$V_C(t) = V \left( 1 - e^{-t/\tau} \right)$$

$$I_C(t) = \frac{V}{R} e^{-t/\tau}$$

La constante de tiempo es $\tau = RC$ (en segundos). Después de $5\tau$ se considera el régimen permanente alcanzado.

| **Tiempo** | **$V_C(t)/V$** | **Porcentaje** |
| :--------: | :------------: | :------------: |
| $t = \tau$ | $1 - e^{-1}$ | 63.2% |
| :--------: | :------------: | :------------: |
| $t = 2\tau$ | $1 - e^{-2}$ | 86.5% |
| :--------: | :------------: | :------------: |
| $t = 3\tau$ | $1 - e^{-3}$ | 95.0% |
| :--------: | :------------: | :------------: |
| $t = 5\tau$ | $1 - e^{-5}$ | 99.3% |
| :--------: | :------------: | :------------: |

```python
import math
R = 1000.0      # ohm
C = 100e-6      # F (100 uF)
V = 12.0
tau = R * C
print(f"tau = {tau*1000:.2f} ms")
t = tau * 5
V_c = V * (1 - math.exp(-t/tau))
I_c = (V/R) * math.exp(-t/tau)
print(f"A 5*tau: V_C = {V_c:.3f} V, I_C = {I_c*1000:.3f} mA")
print(f"Tiempo para 5*tau: {t*1000:.2f} ms")
```

### Circuito RC de Descarga

Si el condensador cargado a $V_0$ se descarga a través de una resistencia:

$$V_C(t) = V_0 e^{-t/\tau}$$

$$I_C(t) = -\frac{V_0}{R} e^{-t/\tau}$$

```python
# Descarga desde V0 = 12 V
V0 = 12.0
R, C = 1000.0, 100e-6
tau = R * C
for t in [0.0, tau, 2*tau, 3*tau, 5*tau]:
    V_c = V0 * math.exp(-t/tau)
    print(f"t = {t*1000:6.1f} ms -> V_C = {V_c:6.3f} V")
```

**Energía almacenada en el condensador:** ver la sección de energía almacenada más adelante.

**Aplicaciones:** filtros, temporizadores (monoestables), fuentes de alimentación (almacenamiento de energía), circuitos de retardo y protección de contactos.

---

## Inductores en Corriente Directa

### Comportamiento en Régimen Permanente

En régimen permanente DC, un inductor se comporta como un **cortocircuito**: $V_L = 0$ y la corriente es constante. La relación voltaje-corriente es:

$$V_L = L \frac{dI_L}{dt}$$

La corriente en un inductor **no puede cambiar instantáneamente**; el inductor se opone a los cambios bruscos de corriente [@alexander2021, cap. 6].

### Circuito RL de Establecimiento

Al conectar un circuito RL serie a la fuente $V$, la corriente crece exponencialmente:

$$I_L(t) = \frac{V}{R} \left( 1 - e^{-t/\tau} \right)$$

$$V_L(t) = V e^{-t/\tau}$$

La constante de tiempo es $\tau = L/R$ (en segundos).

```python
R = 10.0        # ohm
L = 50e-3       # H (50 mH)
V = 12.0
tau = L / R
print(f"tau = {tau*1000:.2f} ms")
I_final = V / R
for t in [0.0, tau, 2*tau, 3*tau, 5*tau]:
    I_L = I_final * (1 - math.exp(-t/tau))
    V_L = V * math.exp(-t/tau)
    print(f"t = {t*1000:6.2f} ms -> I_L = {I_L*1000:6.2f} mA, V_L = {V_L:6.3f} V")
```

### Desconexión y Protección

Al desconectar la fuente, el inductor intenta mantener la corriente. Sin un camino de descarga, el voltaje puede alcanzar valores destructivos (sobretensión de apertura). Por ello se utilizan diodos de libre circulación (rueda libre) en circuitos con relés y motores.

| **Escenario** | **Comportamiento del inductor** | **Riesgo** |
| :-----------: | :-----------------------------: | :--------: |
| Fuente conectada | Corriente crece hacia $V/R$ | Corriente excesiva |
| :-----------: | :-----------------------------: | :--------: |
| Fuente desconectada | Corriente tiende a mantenerse | Sobretension |
| :-----------: | :-----------------------------: | :--------: |
| Régimen permanente | Cortocircuito ($V_L = 0$) | Consumo sin limite |
| :-----------: | :-----------------------------: | :--------: |

```python
# Sobretension de apertura sin diodo de rueda libre
L, R = 50e-3, 10.0
I0 = 1.2            # A circulando antes de abrir
R_abertura = 5e3    # ohm (contacto que se abre)
V_pico = L * I0 * R_abertura / L   # aproximacion instantanea
print(f"I0 = {I0:.2f} A, V_pico estimado > {R_abertura*I0/1000:.0f} kV (destructivo)")
```

> **Nota:** La energía almacenada en un inductor no puede disiparse instantáneamente. En la práctica se coloca un diodo en antiparalelo (rueda libre) para recircular la corriente de forma segura en relés, contactores y fuentes conmutadas.

---

## Energía Almacenada

### Energía en un Condensador

La energía almacenada en el campo eléctrico de un condensador es:

$$W_C = \frac{1}{2} C V^2 = \frac{1}{2} \frac{Q^2}{C} = \frac{1}{2} Q V$$

Un condensador cargado puede entregar esta energía de forma casi instantánea, lo que lo hace peligroso incluso con la fuente desconectada.

```python
C = 1000e-6      # 1000 uF (1 mF)
V = 400.0        # V (capacitor de fuente conmutada)
W = 0.5 * C * V**2
print(f"W_C = {W:.2f} J")
# Descarga equivalente en 1 ms -> potencia media
P = W / 1e-3
print(f"Potencia media en 1 ms = {P/1000:.1f} kW")
```

### Energía en un Inductor

La energía almacenada en el campo magnético de un inductor es:

$$W_L = \frac{1}{2} L I^2$$

```python
L = 50e-3        # 50 mH
I = 10.0         # A
W = 0.5 * L * I**2
print(f"W_L = {W:.2f} J")
```

### Comparación de Elementos de Almacenamiento

| **Elemento** | **Variable de estado** | **Energia** | **Regimen DC** | **Oposicion a** |
| :----------: | :--------------------: | :---------: | :------------: | :-------------: |
| Condensador | Voltaje $V_C$ | $\frac{1}{2}CV^2$ | Circuito abierto | Cambios de voltaje |
| :----------: | :--------------------: | :---------: | :------------: | :-------------: |
| Inductor | Corriente $I_L$ | $\frac{1}{2}LI^2$ | Cortocircuito | Cambios de corriente |
| :----------: | :--------------------: | :---------: | :------------: | :-------------: |

> **Nota:** En circuitos conmutados (fuentes DC-DC), condensadores e inductores operan como dispositivos de almacenamiento intermedio de energía, alternando entre almacenar y entregar energía en cada ciclo de conmutación. Este principio se estudia en detalle en electrónica de potencia.

---

## Instrumentación para Circuitos DC

### Multímetro Digital

El multímetro digital es el instrumento básico de medición. Sus funciones principales en DC son voltímetro, amperímetro y ohmímetro [@boylestad2023, cap. 3].

| **Modo** | **Conexion** | **Resistencia interna** | **Cuidado** |
| :------: | :----------: | :---------------------: | :---------: |
| Voltimetro | En paralelo | Muy alta (ideal infinito) | No medir voltaje en modo corriente |
| :------: | :----------: | :---------------------: | :---------: |
| Amperimetro | En serie | Muy baja (ideal cero) | Nunca en paralelo con la fuente |
| :------: | :----------: | :---------------------: | :---------: |
| Ohmimetro | Sin alimentacion | Fuente interna propia | Circuito apagado y descargado |
| :------: | :----------: | :---------------------: | :---------: |

```python
# Error de carga del voltimetro: Rm = 10 Mohm sobre divisor R1 = 1M, R2 = 1M
V = 12.0
R1, R2 = 1e6, 1e6
Rm = 10e6
V_ideal = V * R2 / (R1 + R2)
R2m = R2 * Rm / (R2 + Rm)
V_medido = V * R2m / (R1 + R2m)
print(f"V_ideal = {V_ideal:.2f} V, V_medido = {V_medido:.2f} V")
print(f"Error = {100*abs(V_medido-V_ideal)/V_ideal:.2f}%")
```

### Osciloscopio

El osciloscopio permite visualizar voltajes variables en el tiempo. Para señales DC puras muestra una línea horizontal cuyo desplazamiento vertical es proporcional al voltaje. Sus parámetros fundamentales son:

- **Escala vertical** (V/div): sensibilidad del canal.
- **Escala horizontal** (s/div o ms/div): base de tiempo.
- **Sonda 1:10 (atenuadora)**: multiplica la escala por 10 y aumenta la impedancia de entrada.
- **Acoplamiento DC/AC**: en DC se observa el valor absoluto; en AC se elimina la componente continua.

```python
# Lectura de osciloscopio: Vpp y VDC de una forma de onda
V_pico = 3.3       # V
V_dc = 1.65        # V (offset)
V_pp = 2 * V_pico
V_rms = V_dc       # para DC puro, RMS = valor DC
print(f"Vpp = {V_pp:.2f} V, VDC = {V_dc:.2f} V")
```

### Medición de Potencia y Energía

La potencia DC se calcula a partir de mediciones de voltaje y corriente:

$$P = V I$$

La energía consumida se obtiene multiplicando la potencia media por el tiempo:

$$W = P \cdot t \qquad [\text{Wh}] \text{ o } [\text{kWh}]$$

```python
V, I = 120.0, 2.5
P = V * I
t_horas = 4.0
W_Wh = P * t_horas
print(f"P = {P:.1f} W, W = {W_Wh/1000:.3f} kWh en {t_horas:.0f} h")
```

### Seguridad en Mediciones

| **Regla** | **Justificacion** |
| :-------: | :---------------: |
| Verificar categoría del instrumento (CAT II/III/IV) | Protección ante transitorios |
| :-------: | :---------------: |
| Conectar el amperímetro solo en serie | Evitar cortocircuito |
| :-------: | :---------------: |
| Descargar condensadores antes de medir | Riesgo de descarga letal |
| :-------: | :---------------: |
| Nunca cambiar de modo con puntas conectadas | Evitar daño interno y arcos |
| :-------: | :---------------: |
| Usar guantes y herramientas aisladas | Protección personal |
| :-------: | :---------------: |

> **Nota:** Los condensadores pueden retener carga peligrosa mucho después de apagar el circuito. Siempre descargarlos con una resistencia adecuada y verificar con el multímetro antes de manipularlos. Ver también [@retie, art. 10].

---

## Resumen de Fórmulas Clave

| **Concepto** | **Formula** |
| :----------- | :--------- |
| Serie | $R_{eq} = \sum R_i$ |
| :----------- | :--------- |
| Paralelo | $\frac{1}{R_{eq}} = \sum \frac{1}{R_i}$ |
| :----------- | :--------- |
| Paralelo (2 elementos) | $R_{eq} = \frac{R_1 R_2}{R_1 + R_2}$ |
| :----------- | :--------- |
| KCL | $\sum I_{entran} = \sum I_{salen}$ |
| :----------- | :--------- |
| KVL | $\sum V_{malla} = 0$ |
| :----------- | :--------- |
| Divisor de voltaje | $V_i = V \frac{R_i}{\sum R}$ |
| :----------- | :--------- |
| Divisor de corriente | $I_i = I \frac{R_{otra}}{\sum R}$ |
| :----------- | :--------- |
| Thévenin | $V_{th}, R_{th}$ (fuente serie) |
| :----------- | :--------- |
| Norton | $I_N = V_{th}/R_{th}$ (fuente paralelo) |
| :----------- | :--------- |
| Máxima transferencia | $R_L = R_{th}$, $P_{max} = V_{th}^2/(4R_{th})$ |
| :----------- | :--------- |
| Condensador | $I_C = C\frac{dV_C}{dt}$, $\tau = RC$ |
| :----------- | :--------- |
| Carga RC | $V_C(t) = V(1 - e^{-t/\tau})$ |
| :----------- | :--------- |
| Descarga RC | $V_C(t) = V_0 e^{-t/\tau}$ |
| :----------- | :--------- |
| Inductor | $V_L = L\frac{dI_L}{dt}$, $\tau = L/R$ |
| :----------- | :--------- |
| Establecimiento RL | $I_L(t) = \frac{V}{R}(1 - e^{-t/\tau})$ |
| :----------- | :--------- |
| Energía condensador | $W_C = \frac{1}{2}CV^2$ |
| :----------- | :--------- |
| Energía inductor | $W_L = \frac{1}{2}LI^2$ |
| :----------- | :--------- |
| Potencia DC | $P = VI$ |
| :----------- | :--------- |

---

## Referencias

[@boylestad2023] Boylestad, R. L. *Introductory Circuit Analysis*. 14th ed. Pearson, 2023.

[@alexander2021] Alexander, C. K. and Sadiku, M. N. O. *Fundamentals of Electric Circuits*. 7th ed. McGraw-Hill, 2021.

[@chapman2012] Chapman, S. J. *Electric Machinery Fundamentals*. 5th ed. McGraw-Hill, 2012.

[@retie] RETIE. *Reglamento Técnico de Instalaciones Eléctricas*. Colombia.