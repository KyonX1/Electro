# 00 — Fundamentos de Electrotecnia

> La base sobre la que se construye todo lo demás. Si entiendes esto, el resto fluye.

---

## 1. La carga eléctrica

### ¿Qué es?

La carga eléctrica es una propiedad fundamental de la materia. Existen dos tipos:

| Tipo | Símbolo | Portador real | Signo |
|------|---------|---------------|-------|
| Positiva | + | Protones (en el núcleo atómico) | Convencional |
| Negativa | − | Electrones (en la órbita exterior) | Real |

### Analogía

Piensa en la carga como el "peso eléctrico". Un objeto con mucho carga "negativa" tiene exceso de electrones. Un objeto con carga "positiva" tiene déficit de electrones (no tiene protones extra, sino que le faltan electrones).

### Unidad de medida

- **Coulomb (C)**: la unidad del Sistema Internacional
- Un solo electrón tiene una carga de −1.602 × 10⁻¹⁹ C
- Un Coulomb equivale a aproximadamente 6.24 × 10¹⁸ electrones

### Propiedades fundamentales

1. **La carga se conserva**: la carga total en un sistema cerrado no cambia. Se puede transferir, pero no crear ni destruir.
2. **La carga se cuantiza**: toda carga es múltiplo entero de la carga del electrón (e = 1.602 × 10⁻¹⁹ C).
3. **Ley de Coulomb**: cargas del mismo signo se repelen, cargas de signo contrario se atraen.

### Ley de Coulomb (fuerza entre cargas)

```
F = k × (|q₁| × |q₂|) / r²

Donde:
  F = fuerza entre las cargas (Newton, N)
  k = constante de Coulomb = 8.99 × 10⁹ N·m²/C²
  q₁, q₂ = magnitud de cada carga (Coulombs, C)
  r = distancia entre las cargas (metros, m)
```

### Ejemplo resuelto

*¿Cuál es la fuerza entre dos cargas de +3 μC y −5 μC separadas 0.2 m?*

```
q₁ = 3 × 10⁻⁶ C
q₂ = 5 × 10⁻⁶ C
r = 0.2 m

F = (8.99 × 10⁹) × (3 × 10⁻⁶) × (5 × 10⁻⁶) / (0.2)²
F = (8.99 × 10⁹) × (15 × 10⁻¹²) / 0.04
F = 0.1349 / 0.04
F = 3.37 N

Resultado: Las cargas se atraen con una fuerza de 3.37 N (porque tienen signo contrario).
```

### Verificación rápida

Si duplicas la carga, la fuerza se duplica. Si duplicas la distancia, la fuerza se reduce a 1/4. Esto tiene sentido por la ley del cuadrado inverso.

### ⚠️ Error común

Usar microcoulombs (μC) directamente sin convertir. Recuerda: 1 μC = 10⁻⁶ C. Siempre convierte antes de sustituir en la fórmula.

---

## 2. Corriente eléctrica

### ¿Qué es?

La corriente eléctrica es el **flujo de carga** a través de un material conductor. Es el movimiento ordenado de electrones bajo la influencia de un campo eléctrico.

### Analogía

Imagina un tubo de agua. La corriente eléctrica es como el **caudal**: cuántos litros por segundo pasan por una sección del tubo. No importa la presión ni la velocidad individual del agua, solo cuánto pasa en total.

### Convención de dirección

| Convención | Dirección | Portador |
|------------|-----------|----------|
| **Convencional** (la que usamos) | Del polo + al polo − | Carga positiva imaginaria |
| **Real** (electrónica) | Del polo − al polo + | Electrones reales |

> **Nota importante**: Usamos la convención convenacional (de + a −) en todos los cálculos. Aunque los electrones se mueven en sentido contrario, los resultados son correctos porque es una convención consistente.

### Fórmula fundamental

```
I = Q / t

Donde:
  I = corriente (Amperios, A)
  Q = carga que cruza una sección (Coulombs, C)
  t = tiempo transcurrido (segundos, s)
```

### Unidad de medida

- **Amperio (A)**: un Amperio = un Coulomb por segundo
- 1 A = 6.24 × 10¹⁸ electrones pasando por un punto cada segundo
- Unidades derivadas: mA (×10⁻³), μA (×10⁻⁶), kA (×10³)

### Corriente en un conductor

```
I = n × A × v_d × q

Donde:
  n = densidad de electrones libres (electrones/m³)
  A = sección transversal del conductor (m²)
  v_d = velocidad de deriva de los electrones (m/s)
  q = carga del electrón = 1.602 × 10⁻¹⁹ C
```

> **Dato curioso**: La velocidad de deriva de los electrones es sorprendentemente lenta (aprox. 0.1 mm/s en un cable doméstico). La corriente se propaga casi a la velocidad de la luz porque el campo eléctrico se transmite rápidamente, no porque los electrones se muevan rápido.

### Tipos de corriente

| Tipo | Símbolo | Comportamiento |
|------|---------|----------------|
| Corriente directa (CD/DC) | I constante | Flujo en una sola dirección, magnitud constante |
| Corriente alterna (CA/AC) | I(t) variable | Cambia de dirección periódicamente, magnitud variable |
| Corriente pulsante | I(t) variable | Cambia de magnitud pero no de dirección |
| Corriente transitoria | i(t) variable | Ocurre durante cambios en el circuito |

### Ejemplo resuelto

*Si 2.5 × 10¹⁸ electrones cruzan una sección de un cable en 0.5 segundos, ¿cuál es la corriente?*

```
Q = n × e = 2.5 × 10¹⁸ × 1.602 × 10⁻¹⁹ = 0.4005 C
t = 0.5 s

I = Q / t = 0.4005 / 0.5 = 0.801 A ≈ 801 mA
```

### Verificación

Un cable doméstico típico soporta 10-20 A. 0.8 A es una corriente pequeña, consistente con lo que esperaríamos de unos pocos mil millones de electrones.

### ⚠️ Error común

Confundir corriente con voltaje. La corriente es **flujo** (cuánto pasa), el voltaje es **empuje** (cuánto presiona). Son conceptos diferentes pero relacionados.

---

## 3. Voltaje (diferencia de potencial)

### ¿Qué es?

El voltaje es la **diferencia de potencial eléctrico** entre dos puntos. Es la "presión" que empuja a los electrones a moverse a través de un conductor.

### Analogía

Piensa en un tanque de agua elevado. El voltaje es como la **altura del tanque**: cuanto más alto está, más presión tiene el agua en la tubería. La corriente es el caudal que fluye, y la resistencia es el diámetro de la tubería.

### Fórmula fundamental

```
V = W / q

Donde:
  V = voltaje (Voltios, V)
  W = trabajo o energía (Joules, J)
  q = carga (Coulombs, C)
```

### Unidad de medida

- **Voltio (V)**: un Voltio = un Joule por Coulomb
- Un Voltio es la diferencia de potencial necesaria para que un Coulomb de carga gane un Joule de energía

### Fuentes de voltaje

| Tipo | Ejemplo | Voltaje típico |
|------|---------|----------------|
| Batería | Pila de 1.5V, batería de carro 12V | 1.5V - 400V |
| Generador | Alternador de vehículo | 12V - 24V CC |
| Red eléctrica | Toma de corriente doméstica | 110V / 220V CA |
| Panel solar | Celda fotovoltaica | 0.5V - 0.6V por celda |
| USB | Cargador de celular | 5V |
| fuente de laboratorio | Fuente regulada | 0-30V variable |

### Conveniencia de tierra

- En circuitos, se toma un punto como referencia (tierra, 0V)
- Todos los demás voltajes se miden respecto a ese punto
- La tierra física (el suelo) se usa como referencia de seguridad en instalaciones reales

### Ejemplo resuelto

*Una batería realiza 50 Joules de trabajo para mover 20 Coulombs. ¿Cuál es su voltaje?*

```
V = W / q = 50 / 20 = 2.5 V
```

### Voltaje en un campo eléctrico uniforme

```
V = E × d

Donde:
  E = intensidad del campo eléctrico (V/m)
  d = distancia entre los puntos (m)
```

### ⚠️ Error común

Decir "hay 220V en el cable". El voltaje siempre es **entre dos puntos**. Lo correcto es "hay 220V entre la fase y el neutro".

---

## 4. Relación entre carga, corriente y voltaje

Los tres conceptos anteriores están profundamente relacionados:

```
Carga (Q)  ←→  Corriente (I = Q/t)  ←→  Voltaje (V = W/q)
   ↑                                              ↑
   |                                              |
   +-- Un Coulomb es "paquete" de carga           +-- Un Voltio es "empuje" por Coulomb
```

La corriente conecta la carga con el tiempo. El voltaje conecta la energía con la carga. Juntos, y con la resistencia, forman la base de toda la electrotecnia.

---

## 5. Resistencia

### ¿Qué es?

La resistencia es la **oposición** que presenta un material al paso de corriente eléctrica. Es la "fricción" que encuentran los electrones al moverse.

### Analogía

En el tubo de agua: la resistencia es el **diámetro del tubo**. Un tubo fino (mucha resistencia) deja pasar poca agua (poca corriente) para la misma presión (voltaje).

### Fórmula fundamental

```
R = ρ × L / A

Donde:
  R = resistencia (Ohmios, Ω)
  ρ = resistividad del material (Ω·m)
  L = longitud del conductor (m)
  A = sección transversal (m²)
```

### Resistividad de materiales comunes

| Material | Resistividad (Ω·m) | ¿Conductor? |
|----------|---------------------|-------------|
| Plata | 1.59 × 10⁻⁸ | Excelente |
| Cobre | 1.68 × 10⁻⁸ | Excelente |
| Oro | 2.44 × 10⁻⁸ | Excelente |
| Aluminio | 2.65 × 10⁻⁸ | Bueno |
| Hierro | 9.71 × 10⁻⁸ | Regular |
| Carbón | 3-60 × 10⁻⁵ | Malo (semiconductor) |
| Vidrio | 10¹⁰ - 10¹⁴ | Aislante |
| Caucho | 10¹³ | Aislante |

### Unidad de medida

- **Ohmio (Ω)**: la resistencia de un conductor que, con un voltaje de 1V, permite pasar 1A
- Unidades derivadas: mΩ (×10⁻³), kΩ (×10³), MΩ (×10⁶)

### Conductancia

La inversa de la resistencia:

```
G = 1 / R

Donde:
  G = conductancia (Siemens, S)
  R = resistencia (Ω)

1 S = 1 Ω⁻¹
```

### ¿Por qué los conductores tienen resistencia?

Los electrones chocan con los átomos de la red cristalina del material. Cada colisión transforma parte de la energía cinética del electrón en calor. A más temperatura, más vibran los átomos, más chocan los electrones, más resistencia.

### Coeficiente de temperatura

```
R = R₀ × [1 + α × (T - T₀)]

Donde:
  R₀ = resistencia a temperatura de referencia T₀
  α = coeficiente de temperatura (1/°C)
  T = temperatura actual
  T₀ = temperatura de referencia (típicamente 20°C o 25°C)
```

| Material | α (×10⁻³ /°C) |
|----------|----------------|
| Cobre | 3.93 |
| Aluminio | 3.90 |
| Hierro | 5.0 |
| Plata | 3.8 |

### Ejemplo resuelto

*Un cable de cobre tiene 100 m de largo y 2.5 mm² de sección. ¿Cuál es su resistencia?*

```
ρ = 1.68 × 10⁻⁸ Ω·m
L = 100 m
A = 2.5 mm² = 2.5 × 10⁻⁶ m²

R = (1.68 × 10⁻⁸ × 100) / (2.5 × 10⁻⁶)
R = 1.68 × 10⁻⁶ / 2.5 × 10⁻⁶
R = 0.672 Ω
```

### Verificación

Un cable de 100m de sección pequeña tiene una resistencia de fracciones de ohmio. Esto tiene sentido: los cables se fabrican para tener la menor resistencia posible.

### ⚠️ Error común

Confundir resistencia con resistividad. La resistencia depende de la geometría (largo y grosor). La resistividad es una propiedad del material. Un cable largo de cobre tiene más resistencia que uno corto del mismo cobre.

---

## 6. Potencia eléctrica

### ¿Qué es?

La potencia es la **tasa** a la que se consume o suministra energía eléctrica. Es la rapidez con que se realiza trabajo eléctrico.

### Analogía

Si la energía es la cantidad total de agua que consume una casa, la potencia es el caudal (litros por minuto) que sale del grifo. Una casa que consume mucha agua rápido tiene alta potencia.

### Fórmulas fundamentales

```
P = V × I          (la más general)
P = I² × R         (cuando conoces corriente y resistencia)
P = V² / R         (cuando conoces voltaje y resistencia)
```

Donde:
- P = potencia (Watts, W)
- V = voltaje (V)
- I = corriente (A)
- R = resistencia (Ω)

### Unidades de potencia

| Unidad | Símbolo | Equivalencia | Uso típico |
|--------|---------|--------------|------------|
| Watt | W | 1 W = 1 V × 1 A | Dispositivos pequeños |
| Kilowatt | kW | 1 kW = 1000 W | Electrodomésticos, motores |
| Megawatt | MW | 1 MW = 10⁶ W | Centrales eléctricas |
| Caballo de vapor | CV (HP) | 1 CV ≈ 736 W | Motores industriales |
| Tonelada de refrigeración | TR | 1 TR ≈ 3517 W | Aire acondicionado |

### Ejemplo resuelto

*Un calentador tiene una resistencia de 40 Ω conectada a 220V. ¿Cuánta potencia consume?*

```
P = V² / R = 220² / 40 = 48400 / 40 = 1210 W = 1.21 kW
```

### Verificación

También puedo calcular la corriente: I = V/R = 220/40 = 5.5 A. Luego P = V × I = 220 × 5.5 = 1210 W. ✓ Coincide.

### ⚠️ Error común

Olvidar que las fórmulas P = I²R y P = V²/R solo son válidas para resistencias puras. Para cargas reactivas (motores, transformadores) necesitas el factor de potencia (lo veremos en CA).

---

## 7. Energía eléctrica

### ¿Qué es?

La energía eléctrica es el **trabajo total** realizado por la corriente eléctrica. Mientras la potencia es "rápido", la energía es "cuánto".

### Fórmula fundamental

```
E = P × t

Donde:
  E = energía (Joules, J)
  P = potencia (Watts, W)
  t = tiempo (segundos, s)
```

### Unidades de energía

| Unidad | Símbolo | Equivalencia | Uso |
|--------|---------|--------------|-----|
| Joule | J | 1 J = 1 W·s | Unidad del SI |
| Kilowatt-hora | kWh | 1 kWh = 3.6 MJ | Factura eléctrica |
| Caloría | cal | 1 cal = 4.186 J | Nutrición |
| BTU | BTU | 1 BTU ≈ 1055 J | Climatización |

### Factura eléctrica

Las compañías eléctricas cobran por **energía consumida**, medida en kWh:

```
Costo = Consumo (kWh) × Precio (por kWh)
```

### Ejemplo resuelto

*Un aire acondicionado de 1.5 kW funciona 8 horas al día. ¿Cuánta energía consume al mes (30 días)?*

```
E = P × t = 1.5 kW × 8 h/día × 30 días = 360 kWh
```

Si el precio es $0.12/kWh:
```
Costo = 360 × 0.12 = $43.20 al mes
```

### Relación potencia-energía-tiempo

```
    Potencia (W) = Energía (J) / Tiempo (s)
    
    Energía (J) = Potencia (W) × Tiempo (s)
    
    Tiempo (s) = Energía (J) / Potencia (W)
```

Es como la relación distancia-velocidad-tiempo: si conoces dos, puedes calcular el tercero.

---

## 8. Resumen: Las 5 variables fundamentales

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   CARGA (Q)  ←── I = Q/t ──→  CORRIENTE (I)        │
│       ↕                              ↕              │
│   V = W/q                    Ohm: V = I·R           │
│       ↕                              ↕              │
│   ENERGÍA (W) ←── P = W/t ──→  POTENCIA (P)        │
│                                                     │
│   + RESISTENCIA (R) = oposición al flujo             │
│                                                     │
└─────────────────────────────────────────────────────┘
```

Cinco conceptos, una sola ecuación central: **V = I × R**.

Si recuerdas esto, entiendes el 50% de la electrotecnia.

---

## Siguiente

Ahora que tienes la base, pasamos a [Corriente Directa](01-corriente-directa.md) donde veremos cómo aplicar estos conceptos en circuitos reales.
