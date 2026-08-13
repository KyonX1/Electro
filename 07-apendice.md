```{=latex}
\clearpage
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \node[inner sep=0pt] at (current page.center) {\includegraphics[width=\paperwidth,height=\paperheight]{img/portadilla-07.png}};
\end{tikzpicture}
\clearpage
```

# Apéndice: Tablas, Constantes y Fórmulas



Este apéndice reúne en forma de tablas maestras los datos y expresiones de consulta rápida utilizados a lo largo del texto: propiedades de los materiales, capacidades de corriente de los conductores, códigos de colores, símbolos normalizados, prefijos del Sistema Internacional, constantes físicas y un resumen de fórmulas por capítulo. Su contenido complementa los capítulos 1 a 5 y sirve de referencia durante la resolución de los ejercicios del capítulo 6 [@iec60364, sec. 431].

---

## A.1 Resistividad y Conductividad de Materiales

La resistencia de un conductor depende de su resistividad ($\rho$), su longitud y su sección: $R = \rho L / A$. El cobre es el material conductor por excelencia en instalaciones; el aluminio se emplea en líneas de distribución por su menor peso y costo [@boylestad2023, cap. 3].

| **Material** | **Resistividad $\rho$ ($\Omega\cdot\text{m}$)** | **Coeficiente de temperatura $\alpha$ (1/°C)** | **Uso tipico** |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |
| Plata | $1.59 \times 10^{-8}$ | 0.0038 | Contactos de precisión |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |
| Cobre | $1.68 \times 10^{-8}$ | 0.00393 | Conductores, bobinados |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |
| Cobre recocido | $1.72 \times 10^{-8}$ | 0.00393 | Conductores eléctricos |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |
| Aluminio | $2.82 \times 10^{-8}$ | 0.00403 | Líneas de distribución |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |
| Wolframio | $5.6 \times 10^{-8}$ | 0.00450 | Filamentos de lámparas |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |
| Acero | $1.0 \times 10^{-7}$ | 0.00500 | Estructuras, rieles |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |
| Níquel | $6.84 \times 10^{-8}$ | 0.00590 | Termopares, resistencias |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |
| Nicromo (aleación) | $1.0 \times 10^{-6}$ | 0.00040 | Resistencias de calor |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |
| Carbono | $3.5 \times 10^{-5}$ | $-0.0005$ | Escobillas, resistencias |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |
| Vidrio | $10^{10}$–$10^{14}$ | — | Aislante |
| :----------: | :--------------------------------------------: | :------------------------------------------: | :------------: |

La resistividad se reduce al aumentar la sección y al bajar la temperatura; para un conductor de cobre a $T$ °C puede corregirse con $R_T = R_{20}[1 + \alpha(T - 20)]$.

---

## A.2 Secciones de Cable y Capacidad de Corriente (IEC 60364)

Extracto de intensidades admisibles para conductores de cobre con aislamiento de PVC a 30 °C de temperatura ambiente, en tres métodos de instalación (extracto ampliado del capítulo 5) [@iec60364, sec. 523].

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
| 185 | 245 | 318 | 310 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |
| 240 | 290 | 375 | 365 |
| :----------------: | :-------------------: | :---------------------: | :---------------: |

La sección mínima se determina por calentamiento (la corriente de servicio no supera la admisible) y se verifica por caída de tensión; el capítulo 5 y el ejercicio 6.3 muestran el procedimiento completo.

---

## A.3 Código de Colores de Resistencias

### Bandas de Resistores

Las resistencias de montaje superficial no se marcan con colores, pero las resistencias axiales tradicionales emplean bandas de color; cada color codifica un dígito y un multiplicador [@boylestad2023, cap. 2].

| **Color** | **Dígito** | **Multiplicador** | **Tolerancia** |
| :-------: | :--------: | :---------------: | :------------: |
| Negro | 0 | $\times 1$ | — |
| :-------: | :--------: | :---------------: | :------------: |
| Marrón | 1 | $\times 10$ | $\pm 1\%$ |
| :-------: | :--------: | :---------------: | :------------: |
| Rojo | 2 | $\times 100$ | $\pm 2\%$ |
| :-------: | :--------: | :---------------: | :------------: |
| Naranja | 3 | $\times 1\,\text{k}$ | — |
| :-------: | :--------: | :---------------: | :------------: |
| Amarillo | 4 | $\times 10\,\text{k}$ | — |
| :-------: | :--------: | :---------------: | :------------: |
| Verde | 5 | $\times 100\,\text{k}$ | $\pm 0.5\%$ |
| :-------: | :--------: | :---------------: | :------------: |
| Azul | 6 | $\times 1\,\text{M}$ | $\pm 0.25\%$ |
| :-------: | :--------: | :---------------: | :------------: |
| Violeta | 7 | $\times 10\,\text{M}$ | $\pm 0.1\%$ |
| :-------: | :--------: | :---------------: | :------------: |
| Gris | 8 | $\times 100\,\text{M}$ | — |
| :-------: | :--------: | :---------------: | :------------: |
| Blanco | 9 | $\times 1\,\text{G}$ | — |
| :-------: | :--------: | :---------------: | :------------: |
| Dorado | — | $\times 0.1$ | $\pm 5\%$ |
| :-------: | :--------: | :---------------: | :------------: |
| Plata | — | $\times 0.01$ | $\pm 10\%$ |
| :-------: | :--------: | :---------------: | :------------: |

Ejemplo: rojo, violeta, naranja, dorado codifica $27 \times 1\,\text{k} = 27\,\text{k}\Omega \pm 5\%$.

### Marcado de Condensadores

| **Código** | **Clase** | **Tolerancia** |
| :--------: | :-------: | :------------: |
| J | Cerámico clase 1 | $\pm 5\%$ |
| :--------: | :-------: | :------------: |
| K | Cerámico clase 2 | $\pm 10\%$ |
| :--------: | :-------: | :------------: |
| M | Electrolítico | $\pm 20\%$ |
| :--------: | :-------: | :------------: |

Los condensadores de pequeña capacidad emplean un código numérico de tres dígitos en picofaradios: los dos primeros son el valor y el tercero el número de ceros (p. ej. 104 = $100\,\text{nF}$).

---

## A.4 Símbolos Normalizados (IEC 60617)

Símbolos gráficos de uso frecuente en esquemas unifilares y diagramas de circuitos [@iec60364, sec. 601].

| **Elemento** | **Símbolo (texto)** | **Referencia IEC 60617** |
| :----------- | :------------------ | :----------------------: |
| Resistencia | Rectángulo | 04-01-01 |
| :----------- | :------------------ | :----------------------: |
| Condensador | Dos líneas paralelas | 04-02-01 |
| :----------- | :------------------ | :----------------------: |
| Inductor | Espiral o arcos | 04-03-01 |
| :----------- | :------------------ | :----------------------: |
| Fuente DC | Círculo con + y - | 06-04-01 |
| :----------- | :------------------ | :----------------------: |
| Fuente AC | Círculo con onda | 06-02-01 |
| :----------- | :------------------ | :----------------------: |
| Tierra | Tres líneas decrecientes | 02-13-01 |
| :----------- | :------------------ | :----------------------: |
| Interruptor | Línea con pivote | 07-01-01 |
| :----------- | :------------------ | :----------------------: |
| Lámpara | Círculo con aspa | 08-06-07 |
| :----------- | :------------------ | :----------------------: |
| Motor | Círculo con M | 06-09-01 |
| :----------- | :------------------ | :----------------------: |
| Contacto NA | Línea paralela abierta | 07-02-01 |
| :----------- | :------------------ | :----------------------: |
| Contacto NC | Línea paralela cerrada | 07-02-03 |
| :----------- | :------------------ | :----------------------: |
| Puente de medida | Círculo con cruz | 06-05-01 |
| :----------- | :------------------ | :----------------------: |
| Fusible | Rectángulo con línea | 07-03-01 |
| :----------- | :------------------ | :----------------------: |
| Diferencial | Rectángulo con RCD | 07-03-13 |
| :----------- | :------------------ | :----------------------: |
| Transformador | Dos bobinas acopladas | 06-08-01 |
| :----------- | :------------------ | :----------------------: |

---

## A.5 Prefijos del Sistema Internacional

| **Prefijo** | **Símbolo** | **Factor** | **Ejemplo** |
| :---------: | :---------: | :--------: | :----------: |
| Tera | T | $10^{12}$ | TW |
| :---------: | :---------: | :--------: | :----------: |
| Giga | G | $10^{9}$ | GHz |
| :---------: | :---------: | :--------: | :----------: |
| Mega | M | $10^{6}$ | MW, M$\Omega$ |
| :---------: | :---------: | :--------: | :----------: |
| Kilo | k | $10^{3}$ | kW, kV |
| :---------: | :---------: | :--------: | :----------: |
| Hecto | h | $10^{2}$ | hPa |
| :---------: | :---------: | :--------: | :----------: |
| Deca | da | $10^{1}$ | daL |
| :---------: | :---------: | :--------: | :----------: |
| Deci | d | $10^{-1}$ | dB |
| :---------: | :---------: | :--------: | :----------: |
| Centi | c | $10^{-2}$ | cm |
| :---------: | :---------: | :--------: | :----------: |
| Mili | m | $10^{-3}$ | mA, mV |
| :---------: | :---------: | :--------: | :----------: |
| Micro | $\mu$ | $10^{-6}$ | $\mu$A, $\mu$F |
| :---------: | :---------: | :--------: | :----------: |
| Nano | n | $10^{-9}$ | nF |
| :---------: | :---------: | :--------: | :----------: |
| Pico | p | $10^{-12}$ | pF |
| :---------: | :---------: | :--------: | :----------: |

En electrotecnia los prefijos más habituales son kilo, mega (potencias y tensiones), mili y micro (corrientes, capacidades) y nano/pico (capacidades parásitas).

---

## A.6 Constantes Físicas

| **Constante** | **Símbolo** | **Valor** | **Unidad** |
| :------------ | :---------: | :-------: | :---------: |
| Velocidad de la luz | $c$ | $2.998 \times 10^{8}$ | m/s |
| :------------ | :---------: | :-------: | :---------: |
| Constante de Coulomb | $k$ | $8.99 \times 10^{9}$ | N·m²/C² |
| :------------ | :---------: | :-------: | :---------: |
| Permitividad del vacío | $\varepsilon_0$ | $8.854 \times 10^{-12}$ | F/m |
| :------------ | :---------: | :-------: | :---------: |
| Permeabilidad del vacío | $\mu_0$ | $4\pi \times 10^{-7}$ | H/m |
| :------------ | :---------: | :-------: | :---------: |
| Carga elemental | $e$ | $1.602 \times 10^{-19}$ | C |
| :------------ | :---------: | :-------: | :---------: |
| Masa del electrón | $m_e$ | $9.109 \times 10^{-31}$ | kg |
| :------------ | :---------: | :-------: | :---------: |
| Aceleración de la gravedad | $g$ | $9.81$ | m/s² |
| :------------ | :---------: | :-------: | :---------: |
| Número de Avogadro | $N_A$ | $6.022 \times 10^{23}$ | 1/mol |
| :------------ | :---------: | :-------: | :---------: |

La relación $k = 1/(4\pi\varepsilon_0)$ y la velocidad de la luz $c = 1/\sqrt{\mu_0\varepsilon_0}$ conectan las constantes electromagnéticas entre sí [@alexander2021, apéndice B].

---

## A.7 Fórmulas Maestras por Tema

### A.7.1 Fundamentos (Capítulo 1)

| **Magnitud** | **Fórmula** |
| :----------- | :---------- |
| Fuerza de Coulomb | $F = k \dfrac{|q_1 q_2|}{r^2}$ |
| :----------- | :---------- |
| Campo eléctrico | $E = \dfrac{F}{q} = k \dfrac{Q}{r^2}$ |
| :----------- | :---------- |
| Potencial eléctrico | $V = k \dfrac{Q}{r}$ |
| :----------- | :---------- |
| Energía potencial | $W = qV$ |
| :----------- | :---------- |
| Resistencia | $R = \rho \dfrac{L}{A}$ |
| :----------- | :---------- |
| Ley de Ohm | $V = IR$ |
| :----------- | :---------- |
| Potencia | $P = VI = I^2R = \dfrac{V^2}{R}$ |
| :----------- | :---------- |
| Energía | $W = Pt$ |
| :----------- | :---------- |
| Resistencia vs. temperatura | $R_T = R_{20}[1 + \alpha(T - 20)]$ |
| :----------- | :---------- |
| Densidad de energía eléctrica | $u_E = \dfrac{1}{2}\varepsilon_0 \varepsilon_r E^2$ |
| :----------- | :---------- |

### A.7.2 Corriente Directa (Capítulo 2)

| **Magnitud** | **Fórmula** |
| :----------- | :---------- |
| Resistencias en serie | $R_{eq} = R_1 + R_2 + \dots$ |
| :----------- | :---------- |
| Resistencias en paralelo | $\dfrac{1}{R_{eq}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dots$ |
| :----------- | :---------- |
| Divisor de tensión | $V_x = V \dfrac{R_x}{R_{total}}$ |
| :----------- | :---------- |
| Divisor de corriente | $I_x = I \dfrac{R_{opuesta}}{R_{total}}$ |
| :----------- | :---------- |
| KCL | $\sum I_{entran} = \sum I_{salen}$ |
| :----------- | :---------- |
| KVL | $\sum V = 0$ |
| :----------- | :---------- |
| Thévenin | $V_{th} = V_{ab,circuito\,abierto}$, $R_{th} = \dfrac{V_{th}}{I_{cc}}$ |
| :----------- | :---------- |
| Norton | $I_N = I_{cc}$, $R_N = R_{th}$ |
| :----------- | :---------- |
| Máx. transferencia | $R_L = R_{th} \Rightarrow P_{max} = \dfrac{V_{th}^2}{4R_{th}}$ |
| :----------- | :---------- |
| Carga de condensador | $v_C(t) = V(1 - e^{-t/RC})$ |
| :----------- | :---------- |
| Descarga de condensador | $v_C(t) = V e^{-t/RC}$ |
| :----------- | :---------- |
| Constante de tiempo RC | $\tau = RC$ |
| :----------- | :---------- |
| Transitorio RL | $i_L(t) = \dfrac{V}{R}(1 - e^{-tR/L})$ |
| :----------- | :---------- |
| Constante de tiempo RL | $\tau = L/R$ |
| :----------- | :---------- |
| Energía en C | $W_C = \dfrac{1}{2}CV^2$ |
| :----------- | :---------- |
| Energía en L | $W_L = \dfrac{1}{2}LI^2$ |
| :----------- | :---------- |

### A.7.3 Corriente Alterna (Capítulo 3)

| **Magnitud** | **Fórmula** |
| :----------- | :---------- |
| Tensión instantánea | $v(t) = V_m \sin(\omega t + \phi)$ |
| :----------- | :---------- |
| Frecuencia angular | $\omega = 2\pi f$ |
| :----------- | :---------- |
| Valor RMS | $V_{rms} = \dfrac{V_m}{\sqrt{2}}$ |
| :----------- | :---------- |
| Reactancia inductiva | $X_L = \omega L = 2\pi fL$ |
| :----------- | :---------- |
| Reactancia capacitiva | $X_C = \dfrac{1}{\omega C} = \dfrac{1}{2\pi fC}$ |
| :----------- | :---------- |
| Impedancia serie RLC | $Z = \sqrt{R^2 + (X_L - X_C)^2}$ |
| :----------- | :---------- |
| Ángulo de fase | $\phi = \arctan\dfrac{X_L - X_C}{R}$ |
| :----------- | :---------- |
| Potencia aparente | $S = VI$ |
| :----------- | :---------- |
| Potencia activa | $P = VI\cos\phi$ |
| :----------- | :---------- |
| Potencia reactiva | $Q = VI\sin\phi$ |
| :----------- | :---------- |
| Frecuencia de resonancia | $f_r = \dfrac{1}{2\pi\sqrt{LC}}$ |
| :----------- | :---------- |
| Factor de calidad serie | $Q_s = \dfrac{X_L}{R}$ |
| :----------- | :---------- |
| Trifásica: tensión de fase | $V_F = \dfrac{V_L}{\sqrt{3}}$ (estrella) |
| :----------- | :---------- |
| Trifásica: potencia | $P_{3\phi} = \sqrt{3}\,V_L I_L \cos\phi$ |
| :----------- | :---------- |
| Corrección de FP | $Q_C = P(\tan\phi_1 - \tan\phi_2)$, $C = \dfrac{Q_C}{\omega V^2}$ |
| :----------- | :---------- |

### A.7.4 Máquinas Eléctricas (Capítulo 4)

| **Magnitud** | **Fórmula** |
| :----------- | :---------- |
| Ley de Faraday | $e = -N \dfrac{d\phi}{dt}$ |
| :----------- | :---------- |
| Fuerza sobre conductor | $F = BIl$ |
| :----------- | :---------- |
| FEM inducida (conductor) | $E = Blv$ |
| :----------- | :---------- |
| Relación de transformación | $\dfrac{V_1}{V_2} = \dfrac{N_1}{N_2} = a$ |
| :----------- | :---------- |
| Transformador ideal | $V_1 I_1 = V_2 I_2$ |
| :----------- | :---------- |
| Rendimiento transformador | $\eta = \dfrac{P_u}{P_u + P_{cu} + P_{fe}}$ |
| :----------- | :---------- |
| FEM máquina DC | $E = K\phi\omega$ |
| :----------- | :---------- |
| Par máquina DC | $T = K\phi I_a$ |
| :----------- | :---------- |
| Velocidad angular motor DC | $\omega = \dfrac{V - I_a R_a}{K\phi}$ |
| :----------- | :---------- |
| Frecuencia síncrona | $f = \dfrac{p \cdot n}{120}$ |
| :----------- | :---------- |
| Velocidad sincronismo | $n_s = \dfrac{120f}{p}$ |
| :----------- | :---------- |
| Deslizamiento | $s = \dfrac{n_s - n}{n_s}$ |
| :----------- | :---------- |
| Velocidad rotor inducción | $n = n_s(1 - s)$ |
| :----------- | :---------- |
| Potencia mecánica | $P_m = T\omega = T \dfrac{2\pi n}{60}$ |
| :----------- | :---------- |
| Tensión de fase del alternador | $V_\phi = \sqrt{E_a^2 - 2E_a I_a X_s \sin\phi + (I_a X_s)^2}$ |
| :----------- | :---------- |

### A.7.5 Instalaciones Eléctricas (Capítulo 5)

| **Magnitud** | **Fórmula** |
| :----------- | :---------- |
| Resistencia de tierra | $R_T = \dfrac{V_{sonda}}{I_{inyectada}}$ |
| :----------- | :---------- |
| Corriente de defecto (TT) | $I_{defecto} = \dfrac{V}{R_A + R_B}$ |
| :----------- | :---------- |
| Tensión de contacto | $V_c = I_{defecto} R_A$ |
| :----------- | :---------- |
| Sensibilidad del diferencial | $I_{\Delta n} \leq \dfrac{V_{c,max}}{R_A}$ |
| :----------- | :---------- |
| Caída de tensión monofásica | $\Delta V = \dfrac{2LI\rho\cos\phi}{S}$ |
| :----------- | :---------- |
| Caída de tensión trifásica | $\Delta V = \dfrac{\sqrt{3}\,LI\rho\cos\phi}{S}$ |
| :----------- | :---------- |
| Sección por calentamiento | $I_{admisible} \geq I_{servicio}$ |
| :----------- | :---------- |
| Selectividad amperimétrica | $I_{aguas\ arriba} \geq I_{aguas\ abajo}$ (calibres y curvas escalonados) |
| :----------- | :---------- |
| Corriente de cortocircuito | $I_{cc} = \dfrac{V}{Z_{bucle}}$ |
| :----------- | :---------- |
| Verificación disparo magnético | $I_{cc} \geq k \cdot I_n$ (curva C: $k = 5$) |
| :----------- | :---------- |

---

## A.8 Notas de Uso

- **Unidades:** todas las expresiones deben trabajarse en unidades SI coherentes; los prefijos de la sección A.5 permiten convertir sin error.
- **Tablas de conductores:** los valores de la sección A.2 son orientativos para cobre-PVC a 30 °C; en condiciones de agrupación, temperatura ambiente superior o aislamiento distinto deben aplicarse los factores de corrección de la norma IEC 60364.
- **Símbolos:** los códigos recogidos en A.4 son identificadores textuales; la norma IEC 60617 contiene los gráficos completos para su uso en planos oficiales.
- **Fórmulas maestras:** las tablas de A.7 resumen únicamente las expresiones de aplicación directa; las deducciones completas y los ejemplos numéricos se encuentran en los capítulos 1 a 5 y se ejercitan en el capítulo 6.

---

## Referencias

Boylestad, R. L. *Introductory Circuit Analysis*. 14th ed. Pearson, 2023.

Alexander, C. K. and Sadiku, M. N. O. *Fundamentals of Electric Circuits*. 7th ed. McGraw-Hill, 2021.

IEC 60364. *Low-voltage electrical installations*. International Electrotechnical Commission.

