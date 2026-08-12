#  00 — Fundamentos de Electrotecnia

> La base sobre la que se construye todo lo demás. Si entiendes esto, el resto fluye.

---

## 1. La Carga Eléctrica

### ¿Qué es?

La carga eléctrica es una propiedad fundamental de la materia. Existen dos tipos:

| **Tipo** | **Símbolo** | **Portador real** | **Signo** |
| :--------: | :-----------: | :-----------------: | :---------: |
| Positiva | + | Protones (núcleo atómico) | Convencional |
| Negativa | − | Electrones (órbita exterior) | Real |

###  Analogía

Piensa en la carga como el **"peso eléctrico"**. Un objeto con carga "negativa" tiene exceso de electrones. Un objeto con carga "positiva" tiene déficit de electrones.

### Unidad de medida

| **Unidad** | **Símbolo** | **Valor** |
| :----------: | :-----------: | :---------: |
| Coulomb | C | Unidad del SI |
| Electrón | e | $1.602 \times 10^{-19}$ C |
| 1 Coulomb | C | $\approx 6.24 \times 10^{18}$ electrones |

### Propiedades fundamentales

1. **La carga se conserva**: la carga total en un sistema cerrado no cambia. Se puede transferir, pero no crear ni destruir.
2. **La carga se cuantiza**: toda carga es múltiplo entero de $e = 1.602 \times 10^{-19}$ C.
3. **Ley de Coulomb**: cargas del mismo signo se repelen, cargas de signo contrario se atraen.

---

###  Ley de Coulomb

$$F = k \times \frac{|q_1| \times |q_2|}{r^2}$$

| **Variable** | **Significado** | **Unidad** |
| :------------: | :---------------: | :----------: |
| $F$ | Fuerza entre las cargas | N (Newton) |
| $k$ | Constante de Coulomb | $8.99 \times 10^9$ N·m²/C² |
| $q_1, q_2$ | Magnitud de cada carga | C (Coulomb) |
| $r$ | Distancia entre las cargas | m (metro) |

---

###  Ejemplo Resuelto

**Pregunta:** ¿Cuál es la fuerza entre dos cargas de $+3\,\mu C$ y $-5\,\mu C$ separadas $0.2$ m?

```python
# Datos
q1 = 3e-6    # C (microcoulombs a coulombs)
q2 = 5e-6    # C
r  = 0.2     # m
k  = 8.99e9  # N.m2/C2

# Calculo
F = k * abs(q1) * abs(q2) / r**2
F = 0.1349 / 0.04
F = 3.37  # N

# Resultado
print(f"F = {F} N -> Las cargas se atraen (signos opuestos)")
```

> ** Verificación:** Si duplicas la carga, la fuerza se duplica. Si duplicas la distancia, la fuerza se reduce a $1/4$ (ley del cuadrado inverso).

> ** Error común:** Usar $\mu C$ directamente sin convertir. Recuerda: $1\,\mu C = 10^{-6}$ C. Siempre convierte antes de sustituir.

---

## 2. Corriente Eléctrica

### ¿Qué es?

La corriente eléctrica es el **flujo de carga** a través de un material conductor. Es el movimiento ordenado de electrones bajo la influencia de un campo eléctrico.

###  Analogía

Imagina un tubo de agua. La corriente es como el **caudal**: cuántos litros por segundo pasan por una sección del tubo.

### Convención de dirección

| **Convención** | **Dirección** | **Portador** |
| :--------------: | :-------------: | :------------: |
| **Convencional** (la que usamos) | Del polo + al polo − | Carga positiva imaginaria |
| **Real** (electrónica) | Del polo − al polo + | Electrones reales |

> ** Nota:** Usamos la convención convencional (de + a −) en todos los cálculos. Los resultados son correctos porque es una convención consistente.

---

###  Fórmula Fundamental

$$I = \frac{Q}{t}$$

| **Variable** | **Significado** | **Unidad** |
| :------------: | :---------------: | :----------: |
| $I$ | Corriente | A (Amperio) |
| $Q$ | Carga que cruza una sección | C (Coulomb) |
| $t$ | Tiempo transcurrido | s (segundo) |

### Unidad de medida

- **Amperio (A)**: $1\,\text{A} = 1\,\text{C/s}$
- $1\,\text{A} = 6.24 \times 10^{18}$ electrones pasando por un punto cada segundo
- Derivados: mA ($\times 10^{-3}$), μA ($\times 10^{-6}$), kA ($\times 10^{3}$)

---

###  Corriente en un Conductor

$$I = n \cdot A \cdot v_d \cdot q$$

| **Variable** | **Significado** | **Unidad** |
| :------------: | :---------------: | :----------: |
| $n$ | Densidad de electrones libres | electrones/m³ |
| $A$ | Sección transversal | m² |
| $v_d$ | Velocidad de deriva | m/s |
| $q$ | Carga del electrón | $1.602 \times 10^{-19}$ C |

> ** Dato curioso:** La velocidad de deriva de los electrones es sorprendentemente lenta ($\approx 0.1$ mm/s en un cable doméstico). La corriente se propaga casi a la velocidad de la luz porque el campo eléctrico se transmite rápidamente, no porque los electrones se muevan rápido.

---

### Tipos de corriente

| **Tipo** | **Símbolo** | **Comportamiento** |
| :--------: | :-----------: | :------------------: |
| Corriente directa (CD/DC) | $I$ constante | Flujo en una sola dirección |
| Corriente alterna (CA/AC) | $I(t)$ variable | Cambia de dirección periódicamente |
| Corriente pulsante | $I(t)$ variable | Cambia de magnitud, no de dirección |
| Corriente transitoria | $i(t)$ variable | Ocurre durante cambios en el circuito |

---

###  Ejemplo Resuelto

**Pregunta:** Si $2.5 \times 10^{18}$ electrones cruzan una sección en $0.5$ segundos, ¿cuál es la corriente?

```python
# Datos
n_electrones = 2.5e18
e = 1.602e-19   # C
t = 0.5          # s

# Cálculo
Q = n_electrones * e   # Carga total
I = Q / t              # Corriente

print(f"Q = {Q:.4f} C")
print(f"I = {I:.3f} A = {I*1000:.1f} mA")
```

> ** Verificación:** Un cable doméstico típico soporta 10-20 A. $0.8$ A es una corriente pequeña, consistente con unos pocos mil millones de electrones.

> ** Error común:** Confundir corriente con voltaje. La corriente es **flujo** (cuánto pasa), el voltaje es **empuje** (cuánto presiona).

---

## 3. Voltaje (Diferencia de Potencial)

### ¿Qué es?

El voltaje es la **diferencia de potencial eléctrico** entre dos puntos. Es la "presión" que empuja a los electrones a moverse.

###  Analogía

Un tanque de agua elevado: el voltaje es la **altura del tanque**. Cuanto más alto, más presión tiene el agua en la tubería.

---

###  Fórmula Fundamental

$$V = \frac{W}{q}$$

| **Variable** | **Significado** | **Unidad** |
| :------------: | :---------------: | :----------: |
| $V$ | Voltaje | V (Voltio) |
| $W$ | Trabajo o energía | J (Joule) |
| $q$ | Carga | C (Coulomb) |

### Unidad de medida

- **Voltio (V)**: $1\,\text{V} = 1\,\text{J/C}$
- Un Voltio es la diferencia de potencial necesaria para que un Coulomb gane un Joule de energía

---

### Fuentes de voltaje

| **Tipo** | **Ejemplo** | **Voltaje típico** |
| :--------: | :-----------: | :------------------: |
| Batería | Pila de 1.5V, carro 12V | 1.5V – 400V |
| Generador | Alternador de vehículo | 12V – 24V CC |
| Red eléctrica | Toma doméstica | 110V / 220V CA |
| Panel solar | Celda fotovoltaica | 0.5V – 0.6V por celda |
| USB | Cargador de celular | 5V |
| Fuente de laboratorio | Fuente regulada | 0–30V variable |

###  Conveniencia de tierra

- En circuitos, se toma un punto como referencia (**tierra**, 0V)
- Todos los voltajes se miden respecto a ese punto
- La tierra física se usa como referencia de seguridad en instalaciones reales

---

###  Ejemplo Resuelto

**Pregunta:** Una batería realiza 50 J de trabajo para mover 20 C. ¿Cuál es su voltaje?

```python
W = 50  # J
q = 20  # C
V = W / q
print(f"V = {V} V")
```

---

###  Voltaje en Campo Eléctrico Uniforme

$$V = E \cdot d$$

| **Variable** | **Significado** | **Unidad** |
| :------------: | :---------------: | :----------: |
| $E$ | Intensidad del campo eléctrico | V/m |
| $d$ | Distancia entre los puntos | m |

> ** Error común:** Decir "hay 220V en el cable". El voltaje siempre es **entre dos puntos**. Lo correcto: "hay 220V entre la fase y el neutro".

---

## 4. Relación entre Carga, Corriente y Voltaje

Los tres conceptos están profundamente relacionados:

```
Carga (Q)  <-- I = Q/t -->  Corriente (I)
    |                              |
V = W/q                    Ohm: V = I.R
    |                              |
Energia (W) <-- P = W/t -->  Potencia (P)
```

> ** Fórmula central:** $V = I \times R$

Cinco conceptos, una sola ecuación. Si recuerdas esto, entiendes el 50% de la electrotecnia.

---

## 5. Resistencia

### ¿Qué es?

La resistencia es la **oposición** que presenta un material al paso de corriente eléctrica. Es la "fricción" que encuentran los electrones.

###  Analogía

En el tubo de agua: la resistencia es el **diámetro del tubo**. Un tubo fino deja pasar poca agua para la misma presión.

---

###  Fórmula Fundamental

$$R = \rho \times \frac{L}{A}$$

| **Variable** | **Significado** | **Unidad** |
| :------------: | :---------------: | :----------: |
| $R$ | Resistencia | Ω (Ohmio) |
| $\rho$ | Resistividad del material | Ω·m |
| $L$ | Longitud del conductor | m |
| $A$ | Sección transversal | m² |

---

### Resistividad de Materiales Comunes

| **Material** | **Resistividad (Ω·m)** | **¿Conductor?** |
| :------------: | :----------------------: | :---------------: |
| Plata | $1.59 \times 10^{-8}$ | Excelente |
| Cobre | $1.68 \times 10^{-8}$ | Excelente |
| Oro | $2.44 \times 10^{-8}$ | Excelente |
| Aluminio | $2.65 \times 10^{-8}$ | Bueno |
| Hierro | $9.71 \times 10^{-8}$ | Regular |
| Carbón | $3\text{-}60 \times 10^{-5}$ | Semiconductor |
| Vidrio | $10^{10} - 10^{14}$ | Aislante |
| Caucho | $10^{13}$ | Aislante |

---

###  Conductancia

La inversa de la resistencia:

$$G = \frac{1}{R}$$

| **Variable** | **Significado** | **Unidad** |
| :------------: | :---------------: | :----------: |
| $G$ | Conductancia | S (Siemens) |
| $R$ | Resistencia | Ω |

$1\,\text{S} = 1\,\Omega^{-1}$

---

### ¿Por qué los conductores tienen resistencia?

Los electrones chocan con los átomos de la red cristalina. Cada colisión transforma energía cinética en calor. A más temperatura, más vibran los átomos, más chocan los electrones, más resistencia.

---

###  Coeficiente de Temperatura

$$R = R_0 \cdot [1 + \alpha \cdot (T - T_0)]$$

| **Variable** | **Significado** |
| :------------: | :---------------: |
| $R_0$ | Resistencia a temperatura de referencia $T_0$ |
| $\alpha$ | Coeficiente de temperatura (1/°C) |
| $T$ | Temperatura actual |
| $T_0$ | Temperatura de referencia (típicamente 20°C) |

| **Material** | **α (×10⁻³ /°C)** |
| :------------: | :------------------: |
| Cobre | 3.93 |
| Aluminio | 3.90 |
| Hierro | 5.0 |
| Plata | 3.8 |

---

###  Ejemplo Resuelto

**Pregunta:** Un cable de cobre de 100 m y 2.5 mm² de sección. ¿Cuál es su resistencia?

```python
rho = 1.68e-8  # Ω.m (cobre)
L = 100         # m
A = 2.5e-6      # m^2 (2.5 mm^2)

R = rho * L / A
print(f"R = {R:.4f} Ω")
```

> ** Verificación:** Un cable de 100m de sección pequeña tiene fracciones de ohmio. Los cables se fabrican para tener la menor resistencia posible.

> ** Error común:** Confundir resistencia con resistividad. La resistencia depende de la geometría (largo y grosor). La resistividad es una propiedad del material.

---

## 6. Potencia Eléctrica

### ¿Qué es?

La potencia es la **tasa** a la que se consume o suministra energía eléctrica. Es la rapidez con que se realiza trabajo eléctrico.

###  Analogía

Si la energía es la cantidad total de agua que consume una casa, la potencia es el **caudal** (litros por minuto) que sale del grifo.

---

###  Fórmulas Fundamentales

$$P = V \cdot I \qquad P = I^2 \cdot R \qquad P = \frac{V^2}{R}$$

| **Variable** | **Significado** | **Unidad** |
| :------------: | :---------------: | :----------: |
| $P$ | Potencia | W (Watt) |
| $V$ | Voltaje | V |
| $I$ | Corriente | A |
| $R$ | Resistencia | Ω |

---

### Unidades de Potencia

| **Unidad** | **Símbolo** | **Equivalencia** | **Uso típico** |
| :----------: | :-----------: | :----------------: | :--------------: |
| Watt | W | $1\,\text{W} = 1\,\text{V} \times 1\,\text{A}$ | Dispositivos pequeños |
| Kilowatt | kW | $1\,\text{kW} = 1000\,\text{W}$ | Electrodomésticos, motores |
| Megawatt | MW | $1\,\text{MW} = 10^6\,\text{W}$ | Centrales eléctricas |
| Caballo de vapor | CV (HP) | $1\,\text{CV} \approx 736\,\text{W}$ | Motores industriales |
| Tonelada de refrigeración | TR | $1\,\text{TR} \approx 3517\,\text{W}$ | Aire acondicionado |

---

###  Ejemplo Resuelto

**Pregunta:** Un calentador de 40 Ω conectado a 220V. ¿Cuánta potencia consume?

```python
V = 220  # V
R = 40   # Ω

P = V**2 / R
print(f"P = {P} W = {P/1000:.2f} kW")
```

> ** Verificación:** También: $I = V/R = 220/40 = 5.5$ A. Luego $P = V \cdot I = 220 \times 5.5 = 1210$ W 

> ** Error común:** Las fórmulas $P = I^2R$ y $P = V^2/R$ solo son válidas para resistencias puras. Para cargas reactivas necesitas el factor de potencia (en CA).

---

## 7. Energía Eléctrica

### ¿Qué es?

La energía eléctrica es el **trabajo total** realizado por la corriente. Mientras la potencia es "rápido", la energía es "cuánto".

---

###  Fórmula Fundamental

$$E = P \cdot t$$

| **Variable** | **Significado** | **Unidad** |
| :------------: | :---------------: | :----------: |
| $E$ | Energía | J (Joule) |
| $P$ | Potencia | W (Watt) |
| $t$ | Tiempo | s (segundo) |

### Unidades de Energía

| **Unidad** | **Símbolo** | **Equivalencia** | **Uso** |
| :----------: | :-----------: | :----------------: | :-------: |
| Joule | J | $1\,\text{J} = 1\,\text{W·s}$ | Unidad del SI |
| Kilowatt-hora | kWh | $1\,\text{kWh} = 3.6\,\text{MJ}$ | Factura eléctrica |
| Caloría | cal | $1\,\text{cal} = 4.186\,\text{J}$ | Nutrición |
| BTU | BTU | $1\,\text{BTU} \approx 1055\,\text{J}$ | Climatización |

---

###  Ejemplo Resuelto

**Pregunta:** Un aire acondicionado de 1.5 kW funciona 8 horas/día. ¿Energía al mes (30 días)? Costo a $0.12/kWh?

```python
P = 1.5      # kW
t = 8 * 30   # horas al mes
precio = 0.12  # $/kWh

E = P * t
costo = E * precio

print(f"E = {E} kWh")
print(f"Costo = ${costo:.2f} al mes")
```

---

###  Relación Potencia-Energía-Tiempo

$$P = \frac{E}{t} \qquad E = P \cdot t \qquad t = \frac{E}{P}$$

Es como la relación distancia-velocidad-tiempo: si conoces dos, calculas el tercero.

---

## 8. Resumen: Las 5 Variables Fundamentales

```
+---------------------------------------------------------+
|                                                         |
|   CARGA (Q)  <-- I = Q/t -->  CORRIENTE (I)            |
|       |                                  |              |
|   V = W/q                        Ohm: V = I.R           |
|       |                                  |              |
|   ENERGIA (W) <-- P = W/t -->  POTENCIA (P)             |
|                                                         |
|   + RESISTENCIA (R) = oposicion al flujo                |
|                                                         |
+---------------------------------------------------------+
```

> ** Fórmula central:** $V = I \times R$

Cinco conceptos, una sola ecuación. Si recuerdas esto, entiendes el 50% de la electrotecnia.

---

## Siguiente

Ahora que tienes la base, pasamos a [Corriente Directa](01-corriente-directa.md) donde veremos cómo aplicar estos conceptos en circuitos reales.
