#!/usr/bin/env python3
"""Genera diagramas profesionales PNG de alta resolución (300 DPI)
para el libro de Electrotecnia Industrial. Usa solo Pillow."""
import os
from PIL import Image, ImageDraw, ImageFont

D = 300  # dpi base -> escala 4x sobre puntos
OUT = os.path.join(os.path.dirname(__file__), "..", "img")

FONT_DIR = "/usr/share/texmf/fonts/opentype/public/tex-gyre"
REG = f"{FONT_DIR}/texgyretermes-regular.otf"
BOLD = f"{FONT_DIR}/texgyretermes-bold.otf"
ITAL = f"{FONT_DIR}/texgyretermes-italic.otf"

NAVY = (31, 56, 100)       # azul marino (títulos)
BLUE = (46, 92, 165)       # azul diagramas
LBLUE = (222, 232, 245)    # relleno cajas
GOLD = (185, 140, 30)      # acento
RED = (165, 42, 42)        # acento rojo suave
GREEN = (25, 105, 80)      # acento verde
GRAY = (90, 95, 105)
LGRAY = (238, 240, 244)


class Canvas:
    def __init__(self, w_pt, h_pt, scale=5):
        self.w = w_pt
        self.h = h_pt
        self.s = scale
        # fondo con degradado vertical suave (blanco -> azul clarisimo)
        W, H = w_pt * scale, h_pt * scale
        base = Image.new("RGB", (W, H))
        px = base.load()
        for y in range(H):
            t = y / max(1, H - 1)
            r = int(255 + (238 - 255) * t)
            g = int(255 + (243 - 255) * t)
            b = int(255 + (249 - 255) * t)
            for x in range(W):
                px[x, y] = (r, g, b)
        self.img = base
        self.d = ImageDraw.Draw(self.img)

    def pt(self, *coords):
        return tuple(int(c * self.s) for c in coords)

    def font(self, size, bold=False, italic=False):
        f = BOLD if bold else (ITAL if italic else REG)
        return ImageFont.truetype(f, int(size * self.s))

    def text(self, xy, txt, size=12, fill=NAVY, bold=False, italic=False,
             anchor="mm", font=None):
        f = font or self.font(size, bold, italic)
        self.d.text(self.pt(*xy), txt, font=f, fill=fill, anchor=anchor)

    def box(self, x, y, w, h, fill=LBLUE, outline=BLUE, width=2,
            radius=10, shadow=True):
        xy = [self.pt(x, y), self.pt(x + w, y + h)]
        if shadow:
            self.d.rounded_rectangle(
                [self.pt(x + 3, y + 4), self.pt(x + w + 3, y + h + 4)],
                radius=radius * self.s, fill=(225, 228, 235))
        self.d.rounded_rectangle(xy, radius=radius * self.s,
                                fill=fill, outline=outline,
                                width=max(2, int(width * self.s / 2)))

    def arrow(self, p1, p2, color=BLUE, width=3, head=10, dash=False):
        x1, y1 = self.pt(*p1)
        x2, y2 = self.pt(*p2)
        if dash:
            self.d.line([(x1, y1), (x2, y2)], fill=color,
                        width=max(1, width * self.s // 3))
        self.d.line([(x1, y1), (x2, y2)], fill=color,
                    width=max(2, int(width * self.s / 2)))
        # cabeza
        ang = math_atan2(y2 - y1, x2 - x1)
        import math
        ang = math.atan2(y2 - y1, x2 - x1)
        h = head * self.s
        for da in (0.42, -0.42):
            px = x2 - h * math.cos(ang + da)
            py = y2 - h * math.sin(ang + da)
            self.d.line([(x2, y2), (px, py)], fill=color,
                        width=max(2, int(width * self.s / 2)))

    def elabel(self, p1, p2, txt, size=11, fill=NAVY, offset=(0, 0),
               bold=False, anchor="mm"):
        mx = (p1[0] + p2[0]) / 2 + offset[0]
        my = (p1[1] + p2[1]) / 2 + offset[1]
        self.text((mx, my), txt, size=size, fill=fill, bold=bold, anchor=anchor)

    def save(self, name):
        path = os.path.join(OUT, name)
        self.img.save(path, "PNG")
        print(f"  {name}: {os.path.getsize(path)//1024} KB, "
              f"{self.img.size[0]}x{self.img.size[1]}")


def math_atan2(dy, dx):
    import math
    return math.atan2(dy, dx)


# ---------------------------------------------------------------------------
# 1. Divisor de tensión (02)
# ---------------------------------------------------------------------------
def divisor_tension():
    c = Canvas(1500, 500)
    y_top, y_mid, y_bot = 170, 250, 370
    # fila principal
    c.box(60, y_top - 40, 130, 80, fill=(255, 238, 205), outline=GOLD)
    c.text((125, y_top), "V", 16, bold=True)
    c.box(250, y_top - 40, 120, 80)
    c.text((310, y_top), "R1", 15, bold=True)
    c.box(430, y_top - 40, 170, 80, fill=(235, 240, 250))
    c.text((515, y_top), "Nodo A", 14, bold=True)
    c.box(660, y_top - 40, 120, 80)
    c.text((720, y_top), "R2", 15, bold=True)
    c.box(840, y_top - 40, 150, 80, fill=(235, 240, 250))
    c.text((915, y_top), "GND", 14, bold=True)
    # rama R3
    c.box(430, y_bot - 40, 120, 80)
    c.text((490, y_bot), "R3", 15, bold=True)
    c.box(840, y_bot - 40, 150, 80, fill=(235, 240, 250))
    c.text((915, y_bot), "GND", 14, bold=True)
    # flechas
    c.arrow((190, y_top), (250, y_top))
    c.arrow((370, y_top), (430, y_top))
    c.arrow((600, y_top), (660, y_top))
    c.arrow((780, y_top), (840, y_top))
    c.arrow((515, y_top + 40), (515, y_bot - 40))
    c.arrow((490 + 60, y_bot + 40), (915, y_bot - 40))
    # etiquetas
    c.text((280, y_top - 75), "I", 13, italic=True)
    c.text((515, (y_top + y_bot) // 2), "I3", 13, italic=True)
    c.text((620, y_bot + 20), "I1 = I2 + I3", 13, bold=True)
    c.save("diagrama-divisor-tension.png")


# ---------------------------------------------------------------------------
# 2. Circuito con carga RL (02)
# ---------------------------------------------------------------------------
def carga_rl():
    c = Canvas(1500, 500)
    y_top, y_bot = 180, 360
    c.box(60, y_top - 40, 130, 80, fill=(255, 238, 205), outline=GOLD)
    c.text((125, y_top), "V", 16, bold=True)
    c.box(250, y_top - 40, 120, 80); c.text((310, y_top), "R1", 15, bold=True)
    c.box(430, y_top - 40, 170, 80, fill=(235, 240, 250))
    c.text((515, y_top), "Salida", 14, bold=True)
    c.box(660, y_top - 40, 180, 80, fill=(255, 238, 205), outline=GREEN)
    c.text((750, y_top), "Carga RL", 14, bold=True)
    c.box(900, y_top - 40, 150, 80, fill=(235, 240, 250))
    c.text((975, y_top), "GND", 14, bold=True)
    c.box(430, y_bot - 40, 120, 80); c.text((490, y_bot), "R2", 15, bold=True)
    c.box(900, y_bot - 40, 150, 80, fill=(235, 240, 250))
    c.text((975, y_bot), "GND", 14, bold=True)
    c.arrow((190, y_top), (250, y_top))
    c.arrow((370, y_top), (430, y_top))
    c.arrow((600, y_top), (660, y_top))
    c.arrow((840, y_top), (900, y_top))
    c.arrow((515, y_top + 40), (515, y_bot - 40))
    c.arrow((550, y_bot + 40), (975, y_bot - 40))
    c.text((230, y_top - 78), "Itotal", 13, italic=True)
    c.text((515, (y_top + y_bot) // 2), "I2", 13, italic=True)
    c.text((715, y_top - 78), "Icarga", 13, italic=True)
    c.save("diagrama-carga-rl.png")


# ---------------------------------------------------------------------------
# 3. Triángulo de impedancias (03)
# ---------------------------------------------------------------------------
def triangulo_impedancias():
    c = Canvas(1400, 900)
    A, B, C = (700, 700), (200, 700), (700, 200)  # rectángulo en A
    # hipotenusa (A->B) y catetos
    c.arrow(A, B, color=GREEN, width=4)
    c.arrow(B, C, color=BLUE, width=4)
    c.arrow(C, A, color=BLUE, width=4, dash=True)
    # ángulo phi en A
    import math
    c.d.arc(c.pt(700 - 70, 700 - 70) + c.pt(700 + 70, 700 + 70),
            start=225 - 90, end=270 - 90, fill=RED,
            width=max(3, 2 * c.s))
    c.text((560, 640), "φ", 20, fill=RED, italic=True)
    # etiquetas
    c.text((450, 760), "R  (cateto real)", 15, bold=True)
    c.text((770, 430), "XL − XC", 15, bold=True)
    c.text((770, 455), "(cateto imag.)", 13)
    c.text((415, 445), "Z  (hipotenusa)", 15, bold=True, fill=GREEN)
    # marcas de ángulo recto
    c.d.line(c.pt(660, 700) + c.pt(660, 640), fill=NAVY, width=max(2, c.s // 2))
    c.d.line(c.pt(660, 640) + c.pt(700, 640), fill=NAVY, width=max(2, c.s // 2))
    c.text((700, 800), "Triángulo de impedancias", 11)
    c.save("diagrama-triangulo-impedancias.png")


# ---------------------------------------------------------------------------
# 4. Triángulo de potencias (03)
# ---------------------------------------------------------------------------
def triangulo_potencias():
    c = Canvas(1400, 900)
    A, B, C = (700, 700), (200, 700), (700, 180)
    c.arrow(A, B, color=BLUE, width=4)
    c.arrow(B, C, color=GREEN, width=4)
    c.arrow(C, A, color=RED, width=4, dash=True)
    import math
    c.d.arc(c.pt(700 - 70, 700 - 70) + c.pt(700 + 70, 700 + 70),
            start=225 - 90, end=270 - 90, fill=RED,
            width=max(3, 2 * c.s))
    c.text((560, 640), "φ", 20, fill=RED, italic=True)
    c.text((450, 760), "P  (W, real)", 15, bold=True)
    c.text((730, 430), "Q  (VAR, reactiva)", 15, bold=True)
    c.text((390, 430), "S  (VA, aparente)", 15, bold=True, fill=RED)
    c.d.line(c.pt(660, 700) + c.pt(660, 640), fill=NAVY, width=max(2, c.s // 2))
    c.d.line(c.pt(660, 640) + c.pt(700, 640), fill=NAVY, width=max(2, c.s // 2))
    c.text((700, 810), "Triángulo de potencias  (S² = P² + Q²)", 11)
    c.save("diagrama-triangulo-potencias.png")


# ---------------------------------------------------------------------------
# 5 y 6. Conexiones estrella y delta (03)
# ---------------------------------------------------------------------------
def conexion_estrella():
    c = Canvas(1500, 460)
    y = 200
    c.box(60, y - 45, 160, 90, fill=(255, 238, 205), outline=GOLD)
    c.text((140, y), "Red 400 V", 14, bold=True)
    c.box(290, y - 45, 150, 90)
    c.text((365, y), "Estrella (Y)", 14, bold=True)
    c.box(510, y - 45, 240, 90, fill=(235, 240, 250))
    c.text((630, y), "V_F = V_L / √3", 14, bold=True)
    c.box(820, y - 45, 200, 90, fill=(235, 240, 250))
    c.text((920, y), "I_L = I_F", 14, bold=True)
    c.arrow((220, y), (290, y))
    c.arrow((440, y), (510, y))
    c.arrow((750, y), (820, y))
    c.text((365, y - 80), "Neutro disponible", 12, italic=True)
    c.save("diagrama-conexion-estrella.png")


def conexion_delta():
    c = Canvas(1500, 460)
    y = 200
    c.box(60, y - 45, 160, 90, fill=(255, 238, 205), outline=GOLD)
    c.text((140, y), "Red 400 V", 14, bold=True)
    c.box(290, y - 45, 150, 90)
    c.text((365, y), "Delta (Δ)", 14, bold=True)
    c.box(510, y - 45, 200, 90, fill=(235, 240, 250))
    c.text((610, y), "V_F = V_L", 14, bold=True)
    c.box(780, y - 45, 260, 90, fill=(235, 240, 250))
    c.text((910, y), "I_L = √3 · I_F", 14, bold=True)
    c.arrow((220, y), (290, y))
    c.arrow((440, y), (510, y))
    c.arrow((710, y), (780, y))
    c.text((365, y - 80), "Sin neutro", 12, italic=True)
    c.save("diagrama-conexion-delta.png")


# ---------------------------------------------------------------------------
# 7. Circuito equivalente del transformador (04)
# ---------------------------------------------------------------------------
def transformador():
    c = Canvas(1700, 800)
    y1, y2 = 230, 570
    # primario
    c.box(60, y1 - 50, 210, 100)
    c.text((165, y1), "V1", 16, bold=True)
    c.box(330, y1 - 50, 210, 100)
    c.text((435, y1), "R1 + jX1", 14, bold=True)
    # núcleo
    c.box(600, y1 - 55, 340, 110, fill=(240, 235, 225), outline=NAVY)
    c.text((770, y1 - 20), "NÚCLEO", 16, bold=True)
    # secundario
    c.box(1000, y1 - 50, 210, 100)
    c.text((1105, y1), "R2 + jX2", 14, bold=True)
    c.box(1270, y1 - 50, 170, 100)
    c.text((1355, y1), "V2", 16, bold=True)
    # ramas paralelo
    c.box(600, y2 - 45, 230, 90, fill=(255, 240, 225), outline=RED)
    c.text((715, y2), "Rfe", 14, bold=True, fill=RED)
    c.text((715, y2 + 25), "(perd. hierro)", 11, fill=RED)
    c.box(890, y2 - 45, 230, 90, fill=(225, 240, 235), outline=GREEN)
    c.text((1005, y2), "jXm", 14, bold=True, fill=GREEN)
    c.text((1005, y2 + 25), "(magnetización)", 11, fill=GREEN)
    # conexiones
    c.arrow((270, y1), (330, y1))
    c.arrow((540, y1), (600, y1))
    c.arrow((940, y1), (1000, y1))
    c.arrow((1210, y1), (1270, y1))
    c.arrow((770, y1 + 55), (770, y2 - 45))
    c.arrow((770, y2 + 45), (770, y1 + 60), dash=True)
    c.save("diagrama-transformador.png")


# ---------------------------------------------------------------------------
# 8. Motor de continua (04)
# ---------------------------------------------------------------------------
def motor_dc():
    c = Canvas(1700, 620)
    y = 240
    c.box(60, y - 45, 150, 90, fill=(255, 238, 205), outline=GOLD)
    c.text((135, y), "V aliment.", 13, bold=True)
    c.box(270, y - 45, 150, 90)
    c.text((345, y), "Ia", 15, bold=True, italic=True)
    c.text((345, y + 28), "(armadura)", 11)
    c.box(480, y - 45, 190, 90, fill=(235, 240, 250))
    c.text((575, y), "E = K·φ·ω", 14, bold=True)
    c.box(730, y - 45, 200, 90, fill=(235, 240, 250))
    c.text((830, y), "T = K·φ·Ia", 14, bold=True)
    c.box(990, y - 45, 150, 90)
    c.text((1065, y), "n", 15, bold=True, italic=True)
    c.text((1065, y + 28), "(velocidad)", 11)
    # rama flujo
    c.box(730, y + 180, 200, 90, fill=(225, 240, 235), outline=GREEN)
    c.text((830, y + 225), "φ (flujo)", 14, bold=True, fill=GREEN)
    c.arrow((210, y), (270, y))
    c.arrow((420, y), (480, y))
    c.arrow((670, y), (730, y))
    c.arrow((930, y), (990, y))
    c.arrow((830, y + 45), (830, y + 90), dash=True)
    c.arrow((830, y + 135), (830, y + 180))
    c.save("diagrama-motor-dc.png")


# ---------------------------------------------------------------------------
# 9. Esquema TT de puesta a tierra (05)
# ---------------------------------------------------------------------------
def instalacion_tt():
    c = Canvas(1500, 820)
    y1 = 200
    c.box(60, y1 - 45, 160, 90, fill=(240, 235, 225), outline=NAVY)
    c.text((140, y1), "Transf.", 13, bold=True)
    c.box(280, y1 - 45, 130, 90)
    c.text((345, y1), "Fase", 14, bold=True)
    c.box(470, y1 - 45, 150, 90, fill=(255, 240, 225), outline=RED)
    c.text((545, y1), "Defecto", 13, bold=True, fill=RED)
    c.box(680, y1 - 45, 130, 90)
    c.text((745, y1), "Masa", 14, bold=True)
    c.box(870, y1 - 45, 110, 90, fill=(235, 240, 250))
    c.text((925, y1), "RA", 14, bold=True)
    # tierra / RB
    c.box(680, y1 + 170, 130, 90)
    c.text((745, y1 + 215), "Tierra", 12, bold=True)
    c.box(870, y1 + 170, 110, 90, fill=(235, 240, 250))
    c.text((925, y1 + 215), "RB", 14, bold=True)
    # neutro
    c.box(280, y1 + 320, 130, 90)
    c.text((345, y1 + 365), "Neutro", 13, bold=True)
    # flechas
    c.arrow((220, y1), (280, y1))
    c.arrow((410, y1), (470, y1))
    c.arrow((620, y1), (680, y1))
    c.arrow((810, y1), (870, y1))
    c.arrow((745, y1 + 45), (745, y1 + 170))
    c.arrow((925, y1 + 45), (925, y1 + 125), dash=True)
    c.arrow((980, y1 + 215), (980, y1 + 365 - 90), dash=True)
    c.arrow((925, y1 + 170), (925, y1 + 320 - 0), dash=True)
    c.text((545, y1 - 85), "Corriente de defecto", 12, italic=True, fill=RED)
    c.text((745, y1 + 290), "Ud = Id · (RA + RB)", 12, bold=True)
    c.save("diagrama-instalacion-tt.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for f in (divisor_tension, carga_rl, triangulo_impedancias,
              triangulo_potencias, conexion_estrella, conexion_delta,
              transformador, motor_dc, instalacion_tt):
        f()
    print("Listo.")