# Instalaciones Eléctricas

La instalación eléctrica de baja tensión es el conjunto de circuitos, equipos y dispositivos que llevan la energía desde el punto de suministro hasta los receptores (alumbrado, fuerza, equipos especiales). Su diseño debe garantizar tres objetivos simultáneos: seguridad de las personas y los bienes, correcto funcionamiento de los receptores y eficiencia económica. Las instalaciones se rigen por normas técnicas de obligado cumplimiento, entre ellas la serie IEC 60364 (internacional), el RETIE en Colombia y, en otros países, el NEC de Estados Unidos o el Reglamento Electrotécnico de Baja Tensión (REBT) en España [@iec60364, sec. 1].

Este capítulo integra los conocimientos de los capítulos anteriores: las leyes de Kirchhoff y la ley de Ohm (Capítulo 2) gobiernan los circuitos de distribución; los sistemas trifásicos (Capítulo 3) alimentan los cuadros industriales; las máquinas (Capítulo 4) son las cargas principales; y la protección contra contactos se fundamenta en el comportamiento de las corrientes de defecto [@retie, art. 1].

---

## Normativa Aplicable

### Estructura de la Norma IEC 60364

La serie IEC 60364 es la referencia internacional para instalaciones eléctricas de baja tensión (hasta 1000 V en AC y 1500 V en DC). Su estructura por partes:

| **Parte** | **Contenido** | **Tema** |
| :-------: | :-----------: | :-------: |
| 1 | Principios fundamentales | Seguridad, diseño |
| :-------: | :-----------: | :-------: |
| 4 | Protección para la seguridad | Contactos, sobreintensidades |
| :-------: | :-----------: | :-------: |
| 5 | Selección y montaje | Conductores, aparamenta |
| :-------: | :-----------: | :-------: |
| 6 | Verificación | Ensayos y comprobaciones |
| :-------: | :-----------: | :-------: |
| 7 | Locales especiales | Baños, piscinas, médicos |
| :-------: | :-----------: | :-------: |

### Marcos Regulatorios

| **Norma** | **Ambito** | **Tension maxima** | **Organismo** |
| :-------: | :--------: | :----------------: | :-----------: |
| IEC 60364 | Internacional | 1000 V AC | IEC |
| :-------: | :--------: | :----------------: | :-----------: |
| RETIE | Colombia | 1000 V AC | Min. Minas y Energía |
| :-------: | :--------: | :----------------: | :-----------: |
| NEC | Estados Unidos | 1000 V AC | NFPA |
| :-------: | :--------: | :----------------: | :-----------: |
| REBT | España | 1000 V AC | Ministerio |
| :-------: | :--------: | :----------------: | :-----------: |

El RETIE (Reglamento Técnico de Instalaciones Eléctricas) es de obligatorio cumplimiento en Colombia: toda instalación nueva o ampliada debe ser diseñada y ejecutada por personal certificado y recibir certificado de conformidad [@retie, art. 2].

---

## Sistemas de Puesta a Tierra

### Objetivos de la Puesta a Tierra

La puesta a tierra persigue: limitar la tensión de contacto, proporcionar un camino de retorno de las corrientes de defecto, y asegurar el funcionamiento de las protecciones. Según el sistema de distribución y la conexión de las masas se distinguen tres esquemas principales: TT, TN e IT [@iec60364, sec. 312].

| **Esquema** | **Neutro de la red** | **Masas de la instalacion** | **Defecto tipico** |
| :---------: | :------------------: | :-------------------------: | :----------------: |
| TT | Puesto a tierra | A tierra propia | Retorno por tierra |
| :---------: | :------------------: | :-------------------------: | :----------------: |
| TN | Puesto a tierra | Al neutro (PE) | Retorno por conductor |
| :---------: | :------------------: | :-------------------------: | :----------------: |
| IT | Aislado/impedante | A tierra propia | Sin retorno directo |
| :---------: | :------------------: | :-------------------------: | :----------------: |

### Esquema TT

En el esquema TT, el neutro del transformador se conecta a tierra (primera tierra) y las masas de la instalación del usuario tienen su propia tierra (segunda tierra). Un defecto de aislamiento cierra el circuito a través de la tierra; la corriente de defecto depende de las resistencias de tierra. La protección requiere un dispositivo diferencial (RCD) de alta sensibilidad:

$$I_{defecto} = \frac{V}{R_A + R_B}$$

donde $R_A$ es la resistencia de tierra de las masas y $R_B$ la del neutro.

```text
                                                   +-----------------+     +----------------------------+
                                                   | Diferencial RCD | --> |          Dispara           |
                                                   +-----------------+     +----------------------------+
                                                     ^
                                                     |
                                                     |
+---------------+     +------+     +---------+     +-----------------+     +----------------------------+     +--------------+     +--------------------+
| Transformador | --> | Fase | --> | Defecto | --> |      Masa       | --> | RB (electrodo instalacion) | --> | Tierra comun | --> | RA (electrodo red) |
+---------------+     +------+     +---------+     +-----------------+     +----------------------------+     +--------------+     +--------------------+
  |                                                                                                                                  ^
  |                                                                                                                                  |
  v                                                                                                                                  |
+---------------+                                                                                                                    |
|    Neutro     | -------------------------------------------------------------------------------------------------------------------+
+---------------+
```

El defecto fase-masa cierra el circuito por tierra a través de $R_B$ y $R_A$; el diferencial RCD detecta la corriente de fuga y desconecta la instalación.

```python
V = 230.0         # V (fase-neutro)
R_A = 10.0        # ohm (tierra de la instalacion)
R_B = 10.0        # ohm (tierra del neutro)
I_def = V / (R_A + R_B)
print(f"I_defecto = {I_def:.1f} A")
# Tension de contacto en las masas
V_contacto = I_def * R_A
print(f"V_contacto = {V_contacto:.0f} V")
print(f"Limite seguro < 50 V (locales secos): {'OK' if V_contacto < 50 else 'REQUIERE DIFERENCIAL'}")
```

### Esquema TN

En el esquema TN (el más usado en instalaciones industriales), las masas se conectan directamente al conductor de protección (PE) que a su vez está conectado al neutro puesto a tierra del transformador. Un defecto produce una corriente de cortocircuito elevada que dispara rápidamente el magnetotérmico o el fusible.

| **Variante** | **Conductor de proteccion** | **Uso tipico** |
| :----------: | :-------------------------: | :------------: |
| TN-S | PE separado del neutro | Instalaciones nuevas |
| :----------: | :-------------------------: | :------------: |
| TN-C | PEN combinado (neutro+PE) | Redes antiguas, industria |
| :----------: | :-------------------------: | :------------: |
| TN-C-S | Mixto | Entradas de red |
| :----------: | :-------------------------: | :------------: |

```python
# Defecto en TN-S: impedancia del bucle de fase-PE
V = 230.0
Z_bucle = 0.4     # ohm (incluye fuente, fase y PE)
I_cc = V / Z_bucle
print(f"I_cortocircuito = {I_cc:.0f} A")
print(f"Un magnetotermico de 16 A curva C dispara en: {0.1} s (magnetico)")
```

### Esquema IT

En el esquema IT, el neutro está aislado de tierra o conectado mediante una impedancia elevada. El primer defecto no produce corriente peligrosa y la instalación puede seguir operando (continuidad de servicio), pero se requiere un vigilante de aislamiento y la búsqueda del defecto. Es el esquema de hospitales, salas de operaciones y procesos continuos.

> **Nota:** La elección del esquema depende de criterios de continuidad de servicio, seguridad y coste. El TT es habitual en instalaciones domésticas y de pequeña potencia; el TN en industria; el IT donde la continuidad es crítica [@iec60364, sec. 312].

---

## Protecciones Eléctricas

### Protección contra Sobrecargas y Cortocircuitos

Las sobreintensidades se clasifican en sobrecargas (1.1 a 10 veces la nominal, funcionamiento prolongado) y cortocircuitos (mucho mayores, destrucción rápida). Los dispositivos básicos son:

| **Dispositivo** | **Funcion** | **Principio** | **Curvas/parametros** |
| :-------------: | :---------: | :-----------: | :--------------------: |
| Fusible | Sobrecarga y corto | Fusion del elemento | gG, aM (amperios) |
| :-------------: | :---------: | :-----------: | :--------------------: |
| Magnetotermico | Sobrecarga (termico) y corto (magnetico) | Bimetal + solenoide | B, C, D |
| :-------------: | :---------: | :-----------: | :--------------------: |
| Limitador | Cortocircuito | Repulsion de contactos | Poder de corte |
| :-------------: | :---------: | :-----------: | :--------------------: |
| Relé térmico | Sobrecarga de motores | Bimetal | Clases 10, 20, 30 |
| :-------------: | :---------: | :-----------: | :--------------------: |

### Curvas de Disparo de los Magnetotérmicos

El disparo magnético se produce a un múltiplo de la corriente nominal según la curva:

| **Curva** | **Disparo magnetico** | **Aplicacion** |
| :-------: | :-------------------: | :------------: |
| B | 3 a 5 x I_n | Cargas resistivas, alumbrado |
| :-------: | :-------------------: | :------------: |
| C | 5 a 10 x I_n | Cargas mixtas, tomas |
| :-------: | :-------------------: | :------------: |
| D | 10 a 20 x I_n | Motores, arranques con pico |
| :-------: | :-------------------: | :------------: |

```python
# Verificacion de disparo por cortocircuito en un circuito
I_n = 16.0        # A (magnetotermico)
curva = 'C'       # disparo 5-10 x I_n
I_cc = 230.0 / 0.4   # A (bucle de 0.4 ohm)
limites = {'B': (3, 5), 'C': (5, 10), 'D': (10, 20)}
lo, hi = limites[curva]
print(f"I_cc = {I_cc:.0f} A")
print(f"Curva {curva}: disparo entre {I_n*lo:.0f} y {I_n*hi:.0f} A")
print(f"Dispara: {'SI' if I_cc >= I_n*lo else 'NO'}")
```

### Protección Diferencial (RCD)

El interruptor diferencial detecta la diferencia entre la corriente de ida y la de retorno. Cuando una corriente de fuga supera la sensibilidad, desconecta el circuito. Protege contra contactos indirectos y directos:

$$\Delta I = I_{fase} - I_{neutro}$$

| **Sensibilidad** | **Uso** |
| :--------------: | :-----: |
| 30 mA | Contacto directo, locales húmedos |
| :--------------: | :-----: |
| 300 mA | Incendio, protección general |
| :--------------: | :-----: |
| 3000 mA | Selectividad, instalaciones especiales |
| :--------------: | :-----: |

```python
# Sensibilidad del diferencial
I_fase = 15.0      # A
I_neutro = 14.985  # A (fuga de 15 mA)
I_fuga = I_fase - I_neutro
sensibilidad = 0.030   # 30 mA
print(f"I_fuga = {I_fuga*1000:.1f} mA")
print(f"Dispara con 30 mA: {'SI' if I_fuga >= sensibilidad else 'NO'}")
# Tension de contacto con tierra de 100 ohm
R_A = 100.0
V_contacto = I_fuga * R_A
print(f"V_contacto limite = {V_contacto*1000:.0f} mV (inofensiva)")
```

### Coordinación y Selectividad

La selectividad garantiza que solo el dispositivo más cercano al defecto actúe, dejando el resto de la instalación en servicio. Se consigue escalonando calibres y curvas, o con dispositivos de tiempo inverso coordinados.

```python
# Ejemplo de escalonamiento de protecciones
protecciones = [
    ('Q1 general', 100.0),
    ('Q2 derivacion', 63.0),
    ('Q3 circuito', 16.0),
]
for nombre, calibre in protecciones:
    print(f"{nombre}: {calibre:.0f} A (dispara el de menor calibre primero)")
```

---

## Cálculo de Secciones de Conductor

### Criterios de Dimensionado

La sección de un conductor debe satisfacer tres criterios simultáneamente:

1. **Intensidad admisible** (calentamiento): la corriente de servicio no debe superar la admisible del conductor según su aislamiento y forma de instalación.
2. **Caída de tensión**: la tensión en el receptor no debe caer más de un valor admisible (típicamente 3% para alumbrado y 5% para fuerza en RETIE).
3. **Protección**: el conductor debe estar protegido contra sobrecargas y cortocircuitos (coordinación con el dispositivo).

### Intensidades Admisibles (extracto, cobre, aislamiento PVC)

| **Seccion (mm²)** | **Tubo en pared (A)** | **Bandeja al aire (A)** | **Enterrado (A)** |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 1.5 | 14.5 | 17.5 | 18 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 2.5 | 19.5 | 24 | 24 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 4 | 26 | 32 | 32 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 6 | 34 | 41 | 41 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 10 | 46 | 57 | 55 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 16 | 61 | 76 | 73 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 25 | 80 | 96 | 95 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 35 | 98 | 119 | 115 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 50 | 116 | 144 | 140 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 70 | 143 | 178 | 175 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 95 | 171 | 211 | 210 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 120 | 194 | 246 | 240 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 150 | 216 | 278 | 270 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 185 | 242 | 312 | 305 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 240 | 288 | 361 | 350 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |

### Caída de Tensión

La caída de tensión en una línea monofásica es:

$$\Delta V = 2 \cdot I \cdot L \cdot \rho \cdot \frac{\cos\phi}{S}$$

En trifásica:

$$\Delta V = \sqrt{3} \cdot I \cdot L \cdot \rho \cdot \frac{\cos\phi}{S}$$

En forma porcentual:

$$\Delta V\% = \frac{\Delta V}{V} \times 100$$

donde $L$ es la longitud (m), $S$ la sección (mm²), $\rho$ la resistividad del cobre ($\approx 0.018\ \Omega\cdot\text{mm}^2/\text{m}$) y $I$ la corriente de carga.

```python
import math
# Dimensionado por caida de tension (trifasica)
V = 400.0            # V
I = 60.0             # A
L = 80.0             # m
rho = 0.018          # ohm*mm2/m (cobre)
FP = 0.9
S = 25.0             # mm2
dV = math.sqrt(3) * I * L * rho * FP / S
dV_pct = dV / V * 100
print(f"dV = {dV:.1f} V ({dV_pct:.2f}%) con S = {S:.0f} mm2")
if dV_pct > 5:
    S = 35.0
    dV = math.sqrt(3) * I * L * rho * FP / S
    dV_pct = dV / V * 100
    print(f"Se aumenta a S = {S:.0f} mm2: dV = {dV:.1f} V ({dV_pct:.2f}%)")
```

### Procedimiento de Cálculo Completo

```python
import math
# Dimensionado completo de un circuito trifasico de fuerza
I_servicio = 94.0      # A
I_dispositivo = 100.0  # A (magnetotermico)
# Criterio 1: calentamiento (bandeja al aire)
tabla_bandeja = {16: 76, 25: 96, 35: 119, 50: 144, 70: 178}
S_calor = None
for S, I_adm in tabla_bandeja.items():
    if I_adm >= I_servicio:
        S_calor = S
        break
print(f"Por calentamiento: S >= {S_calor} mm2")
# Criterio 2: caida de tension
V, L, rho, FP = 400.0, 60.0, 0.018, 0.85
for S in [35, 50, 70]:
    dV_pct = math.sqrt(3) * I_servicio * L * rho * FP / S / V * 100
    if dV_pct <= 3:
        print(f"Por caida de tension: S = {S} mm2 (dV = {dV_pct:.2f}%)")
        break
# Criterio 3: coordinacion con la proteccion
I_z = tabla_bandeja[S]   # admisible del conductor elegido
print(f"Coordinacion: I_z = {I_z} A >= I_n = {I_dispositivo} A: {'OK' if I_z >= I_dispositivo else 'REVISAR'}")
```

> **Nota:** La sección final es la mayor de las tres obtenidas por los criterios de calentamiento, caída de tensión y coordinación con la protección. En circuitos largos, la caída de tensión suele ser el criterio dominante [@retie, art. 16].

### Conductores de Cobre: Resistencia por Unidad de Longitud

| **Seccion (mm²)** | **R (ohm/km)** |
| :----------------: | :-------------: |
| 1.5 | 12.1 |
| :----------------: | :-------------: |
| 2.5 | 7.41 |
| :----------------: | :-------------: |
| 4 | 4.61 |
| :----------------: | :-------------: |
| 6 | 3.08 |
| :----------------: | :-------------: |
| 10 | 1.83 |
| :----------------: | :-------------: |
| 16 | 1.15 |
| :----------------: | :-------------: |
| 25 | 0.727 |
| :----------------: | :-------------: |
| 35 | 0.524 |
| :----------------: | :-------------: |
| 50 | 0.387 |
| :----------------: | :-------------: |
| 70 | 0.268 |
| :----------------: | :-------------: |
| 95 | 0.193 |
| :----------------: | :-------------: |
| 120 | 0.153 |
| :----------------: | :-------------: |

---

## Circuitos de Alumbrado y Fuerza

### Circuitos de Alumbrado

En el RETIE y normativas afines, los circuitos de alumbrado se identifican con números C1, C2, etc. Los circuitos típicos de una instalación doméstica:

| **Circuito** | **Uso** | **Proteccion tipica** | **Seccion minima** |
| :----------: | :-----: | :-------------------: | :----------------: |
| C1 | Alumbrado interior | 10 A | 1.5 mm² |
| :----------: | :-----: | :-------------------: | :----------------: |
| C2 | Tomas de uso general | 16 A | 2.5 mm² |
| :----------: | :-----: | :-------------------: | :----------------: |
| C3 | Cocina y horno | 25 A | 6 mm² |
| :----------: | :-----: | :-------------------: | :----------------: |
| C4 | Lavadora | 20 A | 4 mm² |
| :----------: | :-----: | :-------------------: | :----------------: |
| C5 | Baño y auxiliares | 16 A | 2.5 mm² |
| :----------: | :-----: | :-------------------: | :----------------: |
| C6 | Fuerza industrial | Según calculo | Según calculo |
| :----------: | :-----: | :-------------------: | :----------------: |

### Esquemas de Mando

Los esquemas de mando básicos de alumbrado:

| **Esquema** | **Funcion** | **Elementos** |
| :---------: | :---------: | :------------: |
| Interruptor simple | Encender/apagar desde un punto | 1 interruptor |
| :---------: | :---------: | :------------: |
| Conmutado | Encender/apagar desde dos puntos | 2 conmutadores |
| :---------: | :---------: | :------------: |
| Cruce | Encender/apagar desde tres o mas puntos | Conmutadores + cruce |
| :---------: | :---------: | :------------: |

### Cuadro de Distribución

El cuadro general agrupa la protección y los circuitos. Disposición típica: interruptor general (IGA) o diferencial general, diferenciales por grupos, magnetotérmicos por circuito, y dispositivos de protección contra sobretensiones (DPS) en instalaciones con riesgo de rayos o maniobras [@iec60364, sec. 534].

```python
# Potencia simultanea de una vivienda (factor de simultaneidad)
P_circuitos = [800, 2000, 3500, 1500, 900]    # W por circuito
factor_sim = 0.6
P_total = sum(P_circuitos) * factor_sim
V = 230.0
I_calculo = P_total / V
print(f"P simultanea = {P_total/1000:.2f} kW")
print(f"I calculo = {I_calculo:.1f} A -> IGA recomendado 25 A")
```

---

## Instalaciones Especiales

### Locales Húmedos y Baños

En baños y locales húmedos se definen volúmenes (0, 1, 2, 3) con requisitos crecientes de protección: en el volumen 0 (dentro de la ducha o bañera) solo se permiten aparatos de muy baja tensión de seguridad (SELV); fuera de los volúmenes se exige diferencial de 30 mA.

| **Volumen** | **Zona** | **Requisito principal** |
| :---------: | :------: | :---------------------: |
| 0 | Interior de ducha/bañera | SELV 12 V max |
| :---------: | :------: | :---------------------: |
| 1 | Sobre la ducha (hasta 2.25 m) | IPX4, SELV |
| :---------: | :------: | :---------------------: |
| 2 | 0.6 m alrededor | IPX4 |
| :---------: | :------: | :---------------------: |
| 3 | 2.4 m alrededor | Dispositivos protegidos |
| :---------: | :------: | :---------------------: |

### Piscinas y Fuentes

En piscinas se aplican reglas similares con volúmenes ampliados; todos los circuitos deben ser SELV si están en contacto con el agua, con protección adicional de 30 mA y separación de circuitos [@iec60364, sec. 702].

### Locales Médicos

En locales de uso médico se exige continuidad de servicio (esquema IT típicamente), vigilante de aislamiento, transformadores de separación para zonas de pacientes (grupo 2) y diferenciales de 30 mA en circuitos de seguridad.

### Zonas Peligrosas (ATEX)

En atmósferas explosivas (gas, polvo) se clasifican las zonas 0/1/2 (gas) y 20/21/22 (polvo). Se exigen equipos certificados con marcado de protección (Ex d, Ex e, Ex i, etc.), estanqueidad adecuada y procedimientos de verificación periódica.

| **Zona (gas)** | **Presencia de atmosfera** | **Equipo requerido** |
| :------------: | :------------------------: | :------------------: |
| 0 | Continua | Ex ia / Ex d (categoria 1) |
| :------------: | :------------------------: | :------------------: |
| 1 | Probable | Ex d, Ex e, Ex i (categoria 2) |
| :------------: | :------------------------: | :------------------: |
| 2 | Improbable | Ex n (categoria 3) |
| :------------: | :------------------------: | :------------------: |

> **Nota:** El marcado ATEX incluye la categoría de equipo, el tipo de protección y el grupo de gas según la norma IEC 60079. La selección incorrecta de equipos en zonas clasificadas es causa frecuente de accidentes graves [@iec60364, sec. 7].

---

## Verificación y Ensayos de la Instalación

### Ensayos Exigidos

Antes de la puesta en servicio, toda instalación debe someterse a verificación. Los ensayos básicos son:

| **Ensayo** | **Objetivo** | **Metodo** | **Valor limite tipico** |
| :--------: | :----------: | :--------: | :---------------------: |
| Continuidad | Verificar conductores PE y uniones | Ohmimetro, caida de tension | < 1 ohm circuitos cortos |
| :--------: | :----------: | :--------: | :---------------------: |
| Aislamiento | Detectar fallas de aislamiento | Megger 500 V DC | >= 1 Mohm (500 V) |
| :--------: | :----------: | :--------: | :---------------------: |
| Bucle de defecto | Comprobar disparo por cortocircuito | Medidor de bucle | Disparo < 0.4 s |
| :--------: | :----------: | :--------: | :---------------------: |
| Diferencial | Verificar funcionamiento RCD | Inyector de fuga | Disparo <= 30 mA |
| :--------: | :----------: | :--------: | :---------------------: |
| Resistencia de tierra | Valor de la tierra de masas | Telurometro | <= 10 ohm segun RETIE |
| :--------: | :----------: | :--------: | :---------------------: |

### Medición de la Resistencia de Aislamiento

El ensayo de aislamiento se realiza entre conductores y entre cada conductor y tierra, con el circuito desconectado de la red:

$$R_{aislamiento} = \frac{V_{megger}}{I_{fuga}}$$

```python
# Ensayo de aislamiento: megado de un circuito
V_megger = 500.0   # V
I_fuga = 2e-6      # A (2 uA medidos)
R_aisl = V_megger / I_fuga
print(f"R_aislamiento = {R_aisl/1e6:.1f} Mohm")
print(f"Resultado: {'APTO' if R_aisl >= 1e6 else 'NO APTO'}")
```

### Verificación del Bucle de Defecto

En esquemas TN, la verificación garantiza que la corriente de defecto supera el umbral de disparo magnético del dispositivo de protección dentro del tiempo máximo (0.4 s en circuitos de 230 V):

$$I_{cc\,minima} = \frac{V}{Z_{bucle}} \geq I_n \cdot factor_{curva}$$

```python
V = 230.0
Z_bucle = 0.8      # ohm medido
I_cc_min = V / Z_bucle
I_n = 16.0         # A
factor_curva_C = 5.0
print(f"I_cc minima = {I_cc_min:.0f} A (exige >= {I_n*factor_curva_C:.0f} A)")
print(f"Verificacion: {'OK' if I_cc_min >= I_n*factor_curva_C else 'REVISAR SECCION'} (t: 0.4 s max)")
```

### Medición de la Resistencia de Tierra

La resistencia de tierra se mide con el método de las tres varillas (64% del telurómetro) o por pinza. Un valor típicamente aceptable es inferior a 10 ohm para la tierra de protección en instalaciones de baja tensión, pudiendo variar según el criterio del RETIE y la naturaleza del suelo [@retie, art. 15].

```python
# Metodo simplificado de caida de potencial (3 varillas)
V_medida = 24.0     # V entre sonda y varilla auxiliar
I_inyectada = 2.0   # A
R_tierra = V_medida / I_inyectada
print(f"R_tierra = {R_tierra:.1f} ohm")
print(f"Resultado: {'OK' if R_tierra <= 10 else 'MEJORAR PUESTA A TIERRA'}")
```

### Documentación y Puesta en Servicio

La verificación concluye con un informe (memoria técnica) que incluye: esquemas unifilares reales, resultados de ensayos, características de los equipos de protección, y certificado de instalación. La documentación es obligatoria para la conexión al suministro y para el mantenimiento posterior [@retie, art. 17].

---

## Resumen de Fórmulas Clave

| **Concepto** | **Formula** |
| :----------- | :--------- |
| Corriente de defecto (TT) | $I_{defecto} = V/(R_A + R_B)$ |
| :----------- | :--------- |
| Tension de contacto | $V_{contacto} = I_{defecto} \cdot R_A$ |
| :----------- | :--------- |
| Circuito diferencial | $\Delta I = I_{fase} - I_{neutro}$ |
| :----------- | :--------- |
| Caida de tension monofasica | $\Delta V = 2 I L \rho \cos\phi / S$ |
| :----------- | :--------- |
| Caida de tension trifasica | $\Delta V = \sqrt{3} I L \rho \cos\phi / S$ |
| :----------- | :--------- |
| Caida en porcentaje | $\Delta V\% = \Delta V/V \times 100$ |
| :----------- | :--------- |
| Potencia simultanea | $P_{total} = \sum P_i \cdot factor_{sim}$ |
| :----------- | :--------- |
| Resistencia de aislamiento | $R = V_{megger}/I_{fuga}$ |
| :----------- | :--------- |
| Cortocircuito en el bucle | $I_{cc} = V/Z_{bucle}$ |
| :----------- | :--------- |
| Resistencia de tierra (3 varillas) | $R_T = V_{sonda}/I_{inyectada}$ |
| :----------- | :--------- |

---

## Referencias

[@iec60364] IEC 60364. *Low-voltage electrical installations*. International Electrotechnical Commission.

[@retie] RETIE. *Reglamento Técnico de Instalaciones Eléctricas*. Colombia.

[@boylestad2023] Boylestad, R. L. *Introductory Circuit Analysis*. 14th ed. Pearson, 2023.

[@alexander2021] Alexander, C. K. and Sadiku, M. N. O. *Fundamentals of Electric Circuits*. 7th ed. McGraw-Hill, 2021.

[@chapman2012] Chapman, S. J. *Electric Machinery Fundamentals*. 5th ed. McGraw-Hill, 2012.