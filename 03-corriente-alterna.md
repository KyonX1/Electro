# Corriente Alterna

La corriente alterna (AC) es el flujo de carga que invierte periódicamente su sentido. Su forma de onda más común es la sinusoidal, producida por generadores síncronos en centrales eléctricas. La AC presenta ventajas decisivas frente a la corriente directa: el voltaje puede elevarse y reducirse fácilmente mediante transformadores, lo que permite transmitir energía a grandes distancias con pérdidas reducidas. Por esta razón, prácticamente toda la generación, transmisión y distribución de energía eléctrica se realiza en corriente alterna [@boylestad2023, cap. 13].

Este capítulo desarrolla el análisis de circuitos AC: representación fasorial, impedancia, potencia, resonancia, sistemas trifásicos, filtros y análisis de Fourier. Los conceptos de DC del Capítulo 2 (leyes de Kirchhoff, Thévenin, Norton) se extienden aquí al dominio de la frecuencia mediante los fasores [@alexander2021, cap. 9].

---

## Forma de Onda Sinusoidal

### Parámetros Fundamentales

Una señal sinusoidal de voltaje se expresa como:

$$v(t) = V_m \sin(\omega t + \phi)$$

donde $V_m$ es la amplitud (valor pico), $\omega = 2\pi f$ es la pulsación en rad/s, $f$ es la frecuencia en hercios, y $\phi$ es el ángulo de fase inicial en radianes. El periodo $T = 1/f$ es el tiempo necesario para completar un ciclo.

| **Parametro** | **Simbolo** | **Unidad** | **Relacion** |
| :-----------: | :---------: | :--------: | :----------: |
| Amplitud (pico) | $V_m$ | V | Valor maximo de la onda |
| :-----------: | :---------: | :--------: | :----------: |
| Frecuencia | $f$ | Hz | $f = 1/T$ |
| :-----------: | :---------: | :--------: | :----------: |
| Periodo | $T$ | s | $T = 1/f$ |
| :-----------: | :---------: | :--------: | :----------: |
| Pulsacion | $\omega$ | rad/s | $\omega = 2\pi f$ |
| :-----------: | :---------: | :--------: | :----------: |
| Fase | $\phi$ | rad | Desplazamiento horizontal |
| :-----------: | :---------: | :--------: | :----------: |

```python
import math

# Generar una onda sinusoidal de 50 Hz
f = 50.0            # Hz
V_m = 311.0         # V (pico de 220 V rms)
omega = 2 * math.pi * f
T = 1 / f
print(f"omega = {omega:.1f} rad/s, T = {T*1000:.2f} ms")

for k in range(5):
    t = k * T / 4
    v = V_m * math.sin(omega * t)
    print(f"t = {t*1000:6.2f} ms -> v = {v:8.2f} V")
```

### Diferencia de Fase

Dos sinusoides de la misma frecuencia pueden estar desfasadas. Si $v_1(t) = V_m \sin(\omega t)$ y $v_2(t) = V_m \sin(\omega t - \phi)$, se dice que $v_2$ está **retrasada** respecto a $v_1$ en $\phi$ radianes. En circuitos inductivos la corriente se retrasa respecto al voltaje; en circuitos capacitivos la corriente se adelanta.

$$v(t) = V_m \sin(\omega t \pm \phi)$$

```python
import math
# Desfase entre voltaje y corriente (circuito inductivo)
phi_deg = 30.0      # corriente retrasada 30 deg
phi = math.radians(phi_deg)
t = 0.005
v = 311.0 * math.sin(2 * math.pi * 50 * t)
i = 5.0 * math.sin(2 * math.pi * 50 * t - phi)
print(f"En t={t*1000:.1f} ms: v = {v:.1f} V, i = {i:.2f} A")
print(f"La corriente alcanza su pico {phi_deg:.0f} deg despues del voltaje")
```

---

## Valores de la Onda Sinusoidal

### Valor Pico y Pico-Pico

El valor pico $V_m$ es la amplitud máxima; el valor pico-pico es $V_{pp} = 2 V_m$.

### Valor Eficaz (RMS)

El valor eficaz (root mean square) de una señal es el valor de DC que disiparía la misma potencia en una resistencia. Para una sinusoide:

$$V_{rms} = \frac{V_m}{\sqrt{2}} \qquad I_{rms} = \frac{I_m}{\sqrt{2}}$$

La mayoría de los multímetros miden valores RMS (o valores promedio calibrados para sinusoides). Las tensiones domésticas nominales (220 V, 110 V) son valores eficaces.

### Valor Promedio

El valor promedio de una sinusoide pura sobre un ciclo completo es cero. Para una onda rectificada de onda completa:

$$V_{prom} = \frac{2 V_m}{\pi}$$

### Factores de Forma y de Cresta

| **Factor** | **Formula** | **Sinusoide** |
| :--------: | :---------: | :------------: |
| Forma | $V_{rms}/V_{prom}$ | $\pi/(2\sqrt{2}) \approx 1.11$ |
| :--------: | :---------: | :------------: |
| Cresta | $V_m/V_{rms}$ | $\sqrt{2} \approx 1.414$ |
| :--------: | :---------: | :------------: |

```python
import math
V_m = 311.0
V_rms = V_m / math.sqrt(2)
V_pp = 2 * V_m
V_prom_rect = 2 * V_m / math.pi
print(f"V_m = {V_m:.1f} V")
print(f"V_rms = {V_rms:.1f} V")
print(f"V_pp = {V_pp:.1f} V")
print(f"V_prom (rect. onda completa) = {V_prom_rect:.1f} V")
print(f"Factor de forma = {V_rms/V_prom_rect:.3f}")
print(f"Factor de cresta = {V_m/V_rms:.3f}")
```

> **Nota:** La tensión nominal "220 V" es el valor RMS. El valor pico real es $220\sqrt{2} \approx 311$ V, y el pico-pico de una red monofásica es de aproximadamente 622 V. Esto es importante al dimensionar aislamientos y protecciones.

---

## Fasores y Números Complejos

### Números Complejos en Forma Rectangular y Polar

Un número complejo puede expresarse en forma rectangular $Z = a + jb$ o polar $Z = |Z| \angle \theta$:

$$|Z| = \sqrt{a^2 + b^2} \qquad \theta = \arctan\left(\frac{b}{a}\right)$$

$$a = |Z| \cos\theta \qquad b = |Z| \sin\theta$$

El operador $j = \sqrt{-1}$ rota un fasor 90°. En ingeniería eléctrica se usa $j$ (no $i$) para no confundir con la corriente.

```python
import math
# Conversion rectangular <-> polar
a, b = 3.0, 4.0
Z_mag = math.hypot(a, b)
Z_ang = math.degrees(math.atan2(b, a))
print(f"Rectangular: {a} + j{b}")
print(f"Polar: {Z_mag:.2f} ang {Z_ang:.2f} deg")

# Producto en polar: magnitudes se multiplican, angulos se suman
Z1_m, Z1_a = 5.0, 30.0
Z2_m, Z2_a = 2.0, 45.0
Zp_m = Z1_m * Z2_m
Zp_a = Z1_a + Z2_a
print(f"Z1*Z2 = {Zp_m:.1f} ang {Zp_a:.1f} deg")
```

### Representación Fasorial

Un fasor es un número complejo que representa la amplitud y fase de una sinusoide de frecuencia fija, eliminando la dependencia temporal. La relación entre el dominio temporal y el fasorial es:

$$V_m \cos(\omega t + \phi) \quad \longleftrightarrow \quad V_m \angle \phi$$

Con fasores, las operaciones de circuitos AC se convierten en álgebra compleja: las leyes de Kirchhoff y los teoremas de Thévenin/Norton del Capítulo 2 se aplican igual, sustituyendo resistencias por impedancias.

```python
import math
# Suma de dos fasores (senos con desfase)
V1_m, V1_a = 100.0, 0.0     # V
V2_m, V2_a = 100.0, 90.0    # V (desfasada 90 deg)
V1x = V1_m * math.cos(math.radians(V1_a))
V1y = V1_m * math.sin(math.radians(V1_a))
V2x = V2_m * math.cos(math.radians(V2_a))
V2y = V2_m * math.sin(math.radians(V2_a))
Vx = V1x + V2x
Vy = V1y + V2y
V_m = math.hypot(Vx, Vy)
V_a = math.degrees(math.atan2(Vy, Vx))
print(f"V1 + V2 = {V_m:.1f} V ang {V_a:.1f} deg (141.4 ang 45)")
```

---

## Impedancia: Resistencia, Inductancia y Capacitancia

### Impedancia de Elementos Básicos

La impedancia $Z$ es la oposición total de un elemento al paso de corriente alterna. Es un número complejo con parte real (resistencia $R$) y parte imaginaria (reactancia $X$):

$$Z = R + jX$$

| **Elemento** | **Impedancia** | **Angulo de fase** | **Efecto** |
| :----------: | :------------: | :----------------: | :--------: |
| Resistencia | $Z_R = R$ | $0^\circ$ | Disipa energia |
| :----------: | :------------: | :----------------: | :--------: |
| Inductor | $Z_L = j\omega L = jX_L$ | $+90^\circ$ | Corriente retrasada |
| :----------: | :------------: | :----------------: | :--------: |
| Condensador | $Z_C = -j/(\omega C) = -jX_C$ | $-90^\circ$ | Corriente adelantada |
| :----------: | :------------: | :----------------: | :--------: |

Las reactancias dependen de la frecuencia:

$$X_L = \omega L = 2\pi f L \qquad X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C}$$

```python
import math
L = 100e-3       # H
C = 10e-6        # F
f = 50.0         # Hz
omega = 2 * math.pi * f
X_L = omega * L
X_C = 1 / (omega * C)
print(f"f = {f:.0f} Hz: X_L = {X_L:.1f} ohm, X_C = {X_C:.1f} ohm")
f2 = 1000.0
X_L2 = 2 * math.pi * f2 * L
X_C2 = 1 / (2 * math.pi * f2 * C)
print(f"f = {f2:.0f} Hz: X_L = {X_L2:.1f} ohm, X_C = {X_C2:.1f} ohm")
# La inductancia domina a alta frecuencia, la capacitancia a baja
```

### Ley de Ohm en CA

La ley de Ohm se generaliza a fasores:

$$\vec{V} = \vec{I} \cdot Z \qquad \vec{I} = \frac{\vec{V}}{Z}$$

```python
import math
# Corriente en un circuito RL serie
V = 230.0        # V rms
R = 100.0        # ohm
X_L = 188.5      # ohm (50 Hz, L = 0.6 H)
Z_mag = math.hypot(R, X_L)
I = V / Z_mag
phi = math.degrees(math.atan2(X_L, R))
print(f"Z = {Z_mag:.1f} ohm ang {phi:.1f} deg")
print(f"I = {I:.2f} A (retrasada {phi:.1f} deg respecto a V)")
```

---

## Circuitos RLC en Serie y en Paralelo

### Circuito RLC Serie

En serie, las impedancias se suman:

$$Z = R + j(X_L - X_C)$$

La corriente es común a todos los elementos; el voltaje de la fuente se reparte según cada impedancia:

$$\vec{V} = \vec{I}(R + jX_L - jX_C)$$

Si $X_L > X_C$ el circuito es inductivo (la corriente se retrasa); si $X_C > X_L$ es capacitivo (la corriente se adelanta). Cuando $X_L = X_C$ ocurre la resonancia (sección posterior). El diagrama fasorial resume las relaciones de magnitud y fase:

```text
+--------------------+     +---------------------+     +----------------+
| Z (hipotenusa)     | --> | R (cateto real)     | --> | Eje real      |
+--------------------+     +---------------------+     +----------------+
         |                       |                          ^
         |                       v                          |
         |                    +-----+                       |
         +------------------> | phi | ----------------------+
         |                    +-----+
         v
+---------------------+     +----------------+
| XL - XC (cateto)    | --> | Eje imaginario |
+---------------------+     +----------------+
```

El ángulo $\phi$ entre $R$ y $Z$ define el carácter del circuito: $\phi > 0$ inductivo, $\phi < 0$ capacitivo.

```python
import math
R = 50.0
X_L = 100.0
X_C = 40.0
Z_mag = math.hypot(R, X_L - X_C)
phi = math.degrees(math.atan2(X_L - X_C, R))
print(f"RLC serie: Z = {Z_mag:.1f} ohm ang {phi:.1f} deg (inductivo)")
V = 230.0
I = V / Z_mag
V_R = I * R
V_L = I * X_L
V_C = I * X_C
print(f"I = {I:.2f} A")
print(f"V_R = {V_R:.1f} V, V_L = {V_L:.1f} V, V_C = {V_C:.1f} V")
print(f"Check: V = {math.hypot(V_R, V_L - V_C):.1f} V")
```

### Circuito RLC Paralelo

En paralelo se suman las admitancias $Y = 1/Z$:

$$Y = \frac{1}{R} + j\left(\frac{1}{X_C} - \frac{1}{X_L}\right)$$

El voltaje es común; cada rama toma su propia corriente según la impedancia. La corriente total es la suma fasorial de las corrientes de rama.

```python
import math
R = 100.0
X_L = 200.0
X_C = 50.0
V = 230.0
I_R = V / R
I_L = V / X_L
I_C = V / X_C
I_total_x = I_R                     # componente real
I_total_y = I_C - I_L               # componente imaginaria
I_total = math.hypot(I_total_x, I_total_y)
phi = math.degrees(math.atan2(I_total_y, I_total_x))
print(f"I_R = {I_R:.2f} A, I_L = {I_L:.2f} A, I_C = {I_C:.2f} A")
print(f"I_total = {I_total:.2f} A ang {phi:.1f} deg")
```

### Comparación Serie vs Paralelo

| **Circuito** | **Magnitud comun** | **Suma fasorial** | **Resonancia** |
| :----------: | :----------------: | :---------------: | :------------: |
| Serie | Corriente | Impedancias $Z = R + j(X_L - X_C)$ | $Z$ minima |
| :----------: | :----------------: | :---------------: | :------------: |
| Paralelo | Voltaje | Admitancias $Y = G + j(B_C - B_L)$ | $Y$ minima |
| :----------: | :----------------: | :---------------: | :------------: |

---

## Potencia en Circuitos de Corriente Alterna

### Potencia Activa, Reactiva y Aparente

En AC aparecen tres tipos de potencia:

$$P = V I \cos\phi \qquad [\text{W}]$$

$$Q = V I \sin\phi \qquad [\text{VAR}]$$

$$S = V I \qquad [\text{VA}]$$

- **Potencia activa $P$**: se convierte en trabajo útil o calor (única que factura el suministrador).
- **Potencia reactiva $Q$**: oscila entre fuente y elementos reactivos sin realizar trabajo neto.
- **Potencia aparente $S$**: producto directo de $V$ e $I$; dimensiona transformadores y conductores.

La relación entre ellas es el triángulo de potencias:

$$S^2 = P^2 + Q^2$$

```text
+--------+     +-------+     +----------+     +-----+     +----------------+
| S (VA) | --> | P (W) | --> | Eje real | --> | phi | --> | Q (VAR)       |
+--------+     +-------+     +----------+     +-----+     +----------------+
                 |                              ^
                 +------------------------------+
```

El triángulo de potencias: $S$ es la hipotenusa, $P$ el cateto real y $Q$ el cateto imaginario; $\phi$ es el ángulo entre $S$ y $P$.

| **Potencia** | **Simbolo** | **Unidad** | **Caracter** |
| :----------: | :---------: | :--------: | :-----------: |
| Activa | $P$ | W | Se convierte en trabajo/calor |
| :----------: | :---------: | :--------: | :-----------: |
| Reactiva | $Q$ | VAR | Oscila sin trabajo neto |
| :----------: | :---------: | :--------: | :-----------: |
| Aparente | $S$ | VA | Dimensiona equipos |
| :----------: | :---------: | :--------: | :-----------: |

```python
import math
V, I = 230.0, 10.0
phi = math.radians(30.0)     # factor de potencia 0.866
P = V * I * math.cos(phi)
Q = V * I * math.sin(phi)
S = V * I
print(f"P = {P:.0f} W, Q = {Q:.0f} VAR, S = {S:.0f} VA")
print(f"Check: {math.sqrt(P**2 + Q**2):.0f} VA = S")
```

### Factor de Potencia

El factor de potencia es el coseno del ángulo de desfase:

$$FP = \cos\phi = \frac{P}{S}$$

Un factor de potencia bajo (cargas inductivas: motores, transformadores) incrementa la corriente para una misma potencia útil, aumentando pérdidas en conductores y penalizaciones económicas.

### Corrección del Factor de Potencia

La corrección típica consiste en conectar condensadores en paralelo para compensar la reactancia inductiva:

$$Q_C = P (\tan\phi_1 - \tan\phi_2) \qquad C = \frac{Q_C}{\omega V^2}$$

```python
import math
# Correccion FP de 0.75 a 0.95
P = 50000.0        # W
V = 230.0
f = 50.0
phi1 = math.acos(0.75)
phi2 = math.acos(0.95)
Q1 = P * math.tan(phi1)
Q2 = P * math.tan(phi2)
Q_C = Q1 - Q2
C = Q_C / (2 * math.pi * f * V**2)
print(f"Q1 = {Q1/1000:.1f} kVAR, Q2 = {Q2/1000:.1f} kVAR")
print(f"Q_C = {Q_C/1000:.2f} kVAR")
print(f"C = {C*1e6:.0f} uF (por fase)")
print(f"Reduccion de corriente: {(Q1-Q2)/V:.1f} A menos")
```

> **Nota:** La mejora del factor de potencia es obligatoria en muchas instalaciones industriales (facturación con penalización por FP < 0.90 en muchos países). Ver Capítulo 5 sobre instalaciones eléctricas [@retie, art. 20].

---

## Resonancia

### Resonancia Serie

En un circuito RLC serie, la resonancia ocurre cuando la reactancia inductiva iguala a la capacitiva:

$$X_L = X_C \quad \Rightarrow \quad \omega_r = \frac{1}{\sqrt{LC}} \qquad f_r = \frac{1}{2\pi\sqrt{LC}}$$

En resonancia, la impedancia es puramente resistiva y mínima ($Z = R$), la corriente es máxima, y el voltaje en $L$ y $C$ puede ser mucho mayor que el de la fuente (sobrevoltaje de resonancia).

```python
import math
L = 100e-3      # H
C = 10e-6       # F
R = 10.0        # ohm
f_r = 1 / (2 * math.pi * math.sqrt(L * C))
X_r = 2 * math.pi * f_r * L
Q_f = X_r / R
print(f"f_r = {f_r:.1f} Hz")
print(f"X_L = X_C = {X_r:.1f} ohm")
print(f"Factor de calidad Q = {Q_f:.1f}")
V = 10.0
I_res = V / R
V_L_res = I_res * X_r
print(f"I en resonancia = {I_res:.2f} A")
print(f"V_L = V_C = {V_L_res:.0f} V (amplificacion Q veces la fuente)")
```

### Factor de Calidad y Ancho de Banda

El factor de calidad relaciona la energía almacenada con la disipada:

$$Q_0 = \frac{\omega_r L}{R} = \frac{1}{\omega_r C R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$

El ancho de banda es el intervalo de frecuencias donde la potencia cae a la mitad ($-3$ dB):

$$BW = \frac{f_r}{Q_0}$$

### Resonancia Paralelo

En paralelo, la resonancia ocurre a la misma frecuencia $f_r = 1/(2\pi\sqrt{LC})$ (aproximadamente, para $Q$ alto). En resonancia la admitancia es mínima y la impedancia máxima: el circuito se comporta como un alto rechazo a esa frecuencia.

| **Tipo** | **Impedancia en resonancia** | **Corriente en resonancia** | **Aplicacion** |
| :------: | :--------------------------: | :-------------------------: | :------------: |
| Serie | Minima ($Z = R$) | Maxima | Sintonizacion, deteccion |
| :------: | :--------------------------: | :-------------------------: | :------------: |
| Paralelo | Maxima | Minima (en la fuente) | Rechazo, osciladores |
| :------: | :--------------------------: | :-------------------------: | :------------: |

---

## Sistemas Trifásicos

### Generación y Ventajas

El sistema trifásico consta de tres tensiones sinusoidales desfasadas $120^\circ$ entre sí, generadas por tres devanados del estator separados geométricamente $120^\circ$:

$$v_a(t) = V_m \sin(\omega t)$$

$$v_b(t) = V_m \sin(\omega t - 120^\circ)$$

$$v_c(t) = V_m \sin(\omega t + 120^\circ)$$

Las ventajas principales son: potencia constante y uniforme, ahorro de cobre (menos conductores para igual potencia), y disponibilidad de dos niveles de tensión (línea y fase) [@chapman2012, cap. 2].

### Conexión Estrella (Y)

En estrella, los tres devanados comparten un punto común (neutro). Las tensiones de línea son $\sqrt{3}$ veces las de fase, y las corrientes de línea igualan las de fase:

$$V_{linea} = \sqrt{3}\, V_{fase} \qquad I_{linea} = I_{fase}$$

```text
+--------------------+     +--------------------+     +---------------------+
| Red 400 V          | --> | Estrella (Y)       | --> | V_F = V_L / sqrt(3) |
+--------------------+     +--------------------+     +---------------------+
         |                      |                          ^
         |                      v                          |
         |                   +-----+                      |
         +------------------> | Y   | -> I_L = I_F -------+
                              +-----+
```

### Conexión Delta (Δ)

En delta, los devanados se conectan en triángulo sin neutro. Las tensiones de línea igualan las de fase, y las corrientes de línea son $\sqrt{3}$ veces las de fase:

$$V_{linea} = V_{fase} \qquad I_{linea} = \sqrt{3}\, I_{fase}$$

```text
+--------------------+     +--------------------+     +---------------------+
| Red 400 V          | --> | Delta (D)          | --> | V_F = V_L          |
+--------------------+     +--------------------+     +---------------------+
         |                      |                          ^
         |                      v                          |
         |                   +-----+                      |
         +------------------> | D   | -> I_L = sqrt(3)*I_F-+
                              +-----+
```

| **Conexion** | **V_linea vs V_fase** | **I_linea vs I_fase** | **Neutro** |
| :----------: | :-------------------: | :-------------------: | :--------: |
| Estrella | $V_L = \sqrt{3}\, V_F$ | $I_L = I_F$ | Disponible |
| :----------: | :-------------------: | :-------------------: | :--------: |
| Delta | $V_L = V_F$ | $I_L = \sqrt{3}\, I_F$ | No |
| :----------: | :-------------------: | :-------------------: | :--------: |

```python
import math
# Red de 400 V de linea (estrella): tension de fase
V_L = 400.0
V_F = V_L / math.sqrt(3)
print(f"V_fase (Y) = {V_F:.1f} V (220 V nominal)")
# Potencia trifasica balanceada
P = math.sqrt(3) * V_L * 50.0 * 0.9   # I = 50 A, FP = 0.9
print(f"P trifasica = {P/1000:.1f} kW")
```

### Potencia en Sistemas Trifásicos Balanceados

Para una carga balanceada, la potencia total es:

$$P_{3\phi} = \sqrt{3}\, V_L I_L \cos\phi = 3\, V_F I_F \cos\phi$$

$$Q_{3\phi} = \sqrt{3}\, V_L I_L \sin\phi$$

$$S_{3\phi} = \sqrt{3}\, V_L I_L$$

La potencia trifásica instantánea es constante, lo que elimina las vibraciones de par en motores.

```python
import math
V_L = 400.0
I_L = 20.0
FP = 0.85
phi = math.acos(FP)
S = math.sqrt(3) * V_L * I_L
P = S * FP
Q = S * math.sin(phi)
print(f"S = {S/1000:.2f} kVA, P = {P/1000:.2f} kW, Q = {Q/1000:.2f} kVAR")
```

### Cargas Desbalanceadas y Neutro

En cargas desbalanceadas (estrella con neutro), el neutro conduce la corriente de desequilibrio:

$$\vec{I}_N = \vec{I}_a + \vec{I}_b + \vec{I}_c$$

En delta (sin neutro), el desequilibrio produce corrientes de circulación internas y tensiones asimétricas en las fases, lo que debe evitarse.

---

## Filtros Pasivos

### Filtro Paso Bajo RC

Un filtro paso bajo deja pasar las frecuencias bajas y atenúa las altas. La frecuencia de corte es:

$$f_c = \frac{1}{2\pi RC}$$

A la frecuencia de corte la ganancia cae a $1/\sqrt{2}$ (es decir, $-3$ dB) y el desfase es $-45^\circ$.

```python
import math
R, C = 1000.0, 100e-9      # 1 kohm, 100 nF
f_c = 1 / (2 * math.pi * R * C)
print(f"f_c = {f_c:.0f} Hz")
# Ganancia a f_c, 10*f_c y 0.1*f_c
for factor in [0.1, 1.0, 10.0]:
    f = factor * f_c
    gan = 1 / math.sqrt(1 + (f/f_c)**2)
    print(f"f = {f:8.1f} Hz -> |H| = {gan:.3f} ({20*math.log10(gan):.1f} dB)")
```

### Filtro Paso Alto RC

El filtro paso alto atenúa las frecuencias bajas. Tiene la misma frecuencia de corte $f_c = 1/(2\pi RC)$.

### Filtros Paso Banda y Rechazo Banda

Los filtros paso banda y rechazo banda se construyen con circuitos RLC resonantes: el paso banda deja pasar un intervalo alrededor de $f_r$; el rechazo banda lo elimina. Sus parámetros son la frecuencia central $f_r$ y el ancho de banda $BW$.

| **Filtro** | **Topologia basica** | **Frecuencia caracteristica** | **Aplicacion** |
| :--------: | :------------------: | :---------------------------: | :------------: |
| Paso bajo | RC (salida en C) | $f_c = 1/(2\pi RC)$ | Suavizado, audio |
| :--------: | :------------------: | :---------------------------: | :------------: |
| Paso alto | RC (salida en R) | $f_c = 1/(2\pi RC)$ | Acoplamiento AC |
| :--------: | :------------------: | :---------------------------: | :------------: |
| Paso banda | RLC serie/paralelo | $f_r = 1/(2\pi\sqrt{LC})$ | Radio, comunicaciones |
| :--------: | :------------------: | :---------------------------: | :------------: |
| Rechazo banda | RLC serie en paralelo | $f_r$, ancho $BW$ | Eliminacion de interferencias |
| :--------: | :------------------: | :---------------------------: | :------------: |

---

## Análisis de Fourier Básico

### Serie de Fourier

Toda señal periódica puede descomponerse en una suma de sinusoides: una componente fundamental (a la frecuencia de la señal) más armónicos a múltiplos enteros de esa frecuencia:

$$v(t) = V_0 + \sum_{n=1}^{\infty} [a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)]$$

La componente $V_0$ es el valor promedio (componente DC).

### Espectro de una Onda Cuadrada

Una onda cuadrada de amplitud $V_m$ y frecuencia $f_0$ contiene solo armónicos impares:

$$v(t) = \frac{4V_m}{\pi} \left( \sin(\omega_0 t) + \frac{1}{3}\sin(3\omega_0 t) + \frac{1}{5}\sin(5\omega_0 t) + \dots \right)$$

```python
import math
# Aproximacion de onda cuadrada con N armonicos
V_m = 1.0
f0 = 1000.0     # Hz
t = 0.25 / f0   # instante en el primer cuarto de periodo
v_approx = 0.0
for n in range(1, 20, 2):
    v_approx += (4 * V_m / math.pi) * math.sin(2 * math.pi * n * f0 * t) / n
print(f"Aproximacion con 10 armonicos: v = {v_approx:.3f} (ideal 1.0)")
# El error se reduce agregando armonicos (fenomeno de Gibbs en los bordes)
```

### Aplicaciones del Análisis Armónico

| **Aplicacion** | **Uso de Fourier** |
| :------------: | :----------------: |
| Calidad de energia | Deteccion de armonicos en redes (THD) |
| :------------: | :----------------: |
| Audio | Sintesis y analisis espectral |
| :------------: | :----------------: |
| Electrónica de potencia | Analisis de convertidores conmutados |
| :------------: | :----------------: |
| Vibraciones | Identificacion de modos de resonancia |
| :------------: | :----------------: |

> **Nota:** El contenido armónico de las cargas no lineales (variadores de velocidad, fuentes conmutadas, LED) distorsiona la red. La distorsión armónica total (THD) se calcula como la relación entre la energía de los armónicos y la de la fundamental, y está limitada por normas de calidad de energía [@iec60364, sec. 3].

---

## Resumen de Fórmulas Clave

| **Concepto** | **Formula** |
| :----------- | :--------- |
| Sinusoide | $v(t) = V_m \sin(\omega t + \phi)$ |
| :----------- | :--------- |
| Pulsacion | $\omega = 2\pi f$ |
| :----------- | :--------- |
| Valor eficaz | $V_{rms} = V_m/\sqrt{2}$ |
| :----------- | :--------- |
| Valor promedio (rect. onda completa) | $V_{prom} = 2V_m/\pi$ |
| :----------- | :--------- |
| Reactancia inductiva | $X_L = \omega L$ |
| :----------- | :--------- |
| Reactancia capacitiva | $X_C = 1/(\omega C)$ |
| :----------- | :--------- |
| Impedancia | $Z = R + j(X_L - X_C)$ |
| :----------- | :--------- |
| Potencia activa | $P = VI\cos\phi$ |
| :----------- | :--------- |
| Potencia reactiva | $Q = VI\sin\phi$ |
| :----------- | :--------- |
| Potencia aparente | $S = VI$ |
| :----------- | :--------- |
| Triangulo de potencias | $S^2 = P^2 + Q^2$ |
| :----------- | :--------- |
| Frecuencia de resonancia | $f_r = 1/(2\pi\sqrt{LC})$ |
| :----------- | :--------- |
| Factor de calidad | $Q_0 = \omega_r L/R$ |
| :----------- | :--------- |
| Estrella | $V_L = \sqrt{3}V_F$, $I_L = I_F$ |
| :----------- | :--------- |
| Delta | $V_L = V_F$, $I_L = \sqrt{3}I_F$ |
| :----------- | :--------- |
| Potencia trifasica | $P_{3\phi} = \sqrt{3}V_L I_L \cos\phi$ |
| :----------- | :--------- |
| Frecuencia de corte RC | $f_c = 1/(2\pi RC)$ |
| :----------- | :--------- |
| Onda cuadrada (armonicos) | $v = \frac{4V_m}{\pi}\sum \frac{\sin(n\omega_0 t)}{n}$, $n$ impar |
| :----------- | :--------- |

---

## Referencias

Boylestad, R. L. *Introductory Circuit Analysis*. 14th ed. Pearson, 2023.

Alexander, C. K. and Sadiku, M. N. O. *Fundamentals of Electric Circuits*. 7th ed. McGraw-Hill, 2021.

Chapman, S. J. *Electric Machinery Fundamentals*. 5th ed. McGraw-Hill, 2012.

IEC 60364. *Low-voltage electrical installations*. International Electrotechnical Commission.

RETIE. *Reglamento Técnico de Instalaciones Eléctricas*. Colombia.

