# 04 — Tabla Maestra de Fórmulas

---

## 1. Corriente Directa (DC)

| **Concepto** | **Fórmula** | **Unidades** |
|---|---|---|
| Ley de Ohm | V = I · R | V [V], I [A], R [Ω] |
| Potencia | P = V · I = I² · R = V² / R | P [W] |
| Energía | E = P · t | E [J], t [s] |
| Calor de Joule | Q = I² · R · t | Q [J] |
| Resistencia en serie | R_t = R₁ + R₂ + … + Rₙ = Σ Rᵢ | R_t [Ω] |
| Resistencia en paralelo | 1/R_t = 1/R₁ + 1/R₂ + … + 1/Rₙ = Σ 1/Rᵢ | R_t [Ω] |
| Divisor de voltaje | V_x = V · (R_x / R_t) | V_x [V] |
| Divisor de corriente | I_x = I_total · (R_t / R_x) | I_x [A] |
| Teorema de Thévenin | V_th = V_circuito_abierto ; R_th = R_eq (fuentes desactivadas) | V_th [V], R_th [Ω] |
| Teorema de Norton | I_n = V_th / R_th ; R_n = R_th | I_n [A], R_n [Ω] |
| Capacitor (carga) | C = Q / V | C [F], Q [C] |
| Energía del capacitor | E = ½ · C · V² = ½ · Q² / C | E [J] |
| Inductor (energía) | E = ½ · L · I² | E [J], L [H] |
| Constante de tiempo RC | τ = R · C | τ [s] |
| Constante de tiempo RL | τ = L / R | τ [s] |
| Carga del capacitor RC | q(t) = Q_max · (1 − e^(−t/RC)) | q [C] |
| Descarga del capacitor RC | q(t) = Q_max · e^(−t/RC) | q [C] |
| Corriente en RL (carga) | i(t) = (V/R) · (1 − e^(−Rt/L)) | i [A] |
---

## 2. Corriente Alterna (AC)

| **Concepto** | **Fórmula** | **Unidades** |
|---|---|---|
| Señal senoidal | v(t) = V_max · sin(ωt + φ) | V [V], ω [rad/s] |
| Frecuencia angular | ω = 2πf = 2π/T | ω [rad/s] |
| Relación frecuencia-período | f = 1/T | f [Hz], T [s] |
| Valor RMS (voltaje) | V_rms = V_max / √2 ≈ 0,707 · V_max | V_rms [V] |
| Valor RMS (corriente) | I_rms = I_max / √2 ≈ 0,707 · I_max | I_rms [A] |
| Factor de forma (señal sinusoidal) | FF = V_rms / V_media = π/(2√2) ≈ 1,11 | FF [adim] |
| Reactancia inductiva | X_L = 2πfL = ωL | X_L [Ω] |
| Reactancia capacitiva | X_C = 1 / (2πfC) = 1 / (ωC) | X_C [Ω] |
| Impedancia | Z = √(R² + (X_L − X_C)²) | Z [Ω] |
| Ángulo de fase | φ = arctan((X_L − X_C) / R) | φ [rad] o [°] |
| Corriente (ley de Ohm AC) | I = V / Z | I [A] |
| Potencia activa | P = V · I · cosφ = I² · R | P [W] |
| Potencia reactiva | Q = V · I · sinφ = I² · X | Q [VAR] |
| Potencia aparente | S = V · I = √(P² + Q²) | S [VA] |
| Factor de potencia | FP = cosφ = P / S | FP [adim] |
| Corrección del FP (capacitor) | C = P · (tanφ₁ − tanφ₂) / (ω · V²) | C [F] |
| Frecuencia de resonancia | f₀ = 1 / (2π√(LC)) | f₀ [Hz] |
| Factor de calidad (serie) | Q_factor = X_L / R = (1/R) · √(L/C) | Q [adim] |
| Ancho de banda | BW = f₀ / Q | BW [Hz] |
| Resonancia paralelo (ideal) | f₀ = 1 / (2π√(LC)) | f₀ [Hz] |
---

## 3. Corriente Trifásica

| **Concepto** | **Fórmula** | **Unidades** |
|---|---|---|
| **Conexión Estrella (Y)** ||
| Relación voltaje | V_L = √3 · V_F | V_L [V], V_F [V] |
| Relación corriente | I_L = I_F | I_L [A], I_F [A] |
| **Conexión Triángulo (Δ)** ||
| Relación voltaje | V_L = V_F | V_L [V], V_F [V] |
| Relación corriente | I_L = √3 · I_F | I_L [A], I_F [A] |
| **Potencia (ambas conexiones)** ||
| Potencia activa trifásica | P = √3 · V_L · I_L · cosφ | P [W] |
| Potencia reactiva trifásica | Q = √3 · V_L · I_L · sinφ | Q [VAR] |
| Potencia aparente trifásica | S = √3 · V_L · I_L | S [VA] |
---

## 4. Transformador

| **Concepto** | **Fórmula** | **Unidades** |
|---|---|---|
| Relación de vueltas | a = N₁ / N₂ | a [adim] |
| Relación de voltajes | a = V₁ / V₂ = N₁ / N₂ | V₁ [V], V₂ [V] |
| Relación de corrientes | a = I₂ / I₁ = N₁ / N₂ | I₁ [A], I₂ [A] |
| Potencia ideal | V₁ · I₁ = V₂ · I₂ | P [W] |
| Eficiencia | η = P_out / (P_out + P_pérdidas) × 100% | η [%] |
| Pérdidas totales | P_pérdidas = P_núcleo + P_cobre | P [W] |
| Pérdidas en cobre | P_cobre = I² · R_eq | P [W] |
| Pérdidas en núcleo | P_núcleo = P_historéresis + P_corrientes_parásitas | P [W] |
| Sobrevoltaje de excitación | V_exc ≈ 2–5% de V_nominal | V [V] |
---

## 5. Constantes y Prefijos SI

### Prefijos del Sistema Internacional

| **Prefijo** | **Símbolo** | **Factor** |
|---|---|---|
| giga | G | 10⁹ |
| mega | M | 10⁶ |
| kilo | k | 10³ |
| (base) | — | 10⁰ |
| mili | m | 10⁻³ |
| micro | μ | 10⁻⁶ |
| nano | n | 10⁻⁹ |
| pico | p | 10⁻¹² |
### Conversiones Comunes

| **De** | **A** | **Multiplicar por** |
|---|---|---|
| CV (caballos de vapor) | W | 735,49875 |
| kWh | J | 3 600 000 |
| °C | K | + 273,15 |
| °F | °C | (°F − 32) × 5/9 |
| HP (horsepower, imperial) | W | 745,7 |
| BTU/h | W | 0,29307 |
| cmil (circular mil) | m² | 5,067 × 10⁻¹⁰ |
| VAR | W | (× cosφ para activa) |
| VA | W | (× FP para activa) |
### Constantes Físicas Relevantes

| **Constante** | **Símbolo** | **Valor** |
|---|---|---|
| Permeabilidad del vacío | μ₀ | 4π × 10⁻⁷ H/m ≈ 1,2566 × 10⁻⁶ H/m |
| Permitividad del vacío | ε₀ | 8,854 × 10⁻¹² F/m |
| Constante de Coulomb | k_e | 8,988 × 10⁹ N·m²/C² |
| Carga del electrón | e | 1,602 × 10⁻¹⁹ C |
| Velocidad de la luz | c | 2,998 × 10⁸ m/s |