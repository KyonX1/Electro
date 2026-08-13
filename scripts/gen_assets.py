#!/usr/bin/env python3
"""Genera portada artistica y hojas de formula PNG de alta resolucion."""
import os, math, random
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/texmf/fonts/opentype/public/tex-gyre"
REG  = f"{FONT_DIR}/texgyretermes-regular.otf"
BOLD = f"{FONT_DIR}/texgyretermes-bold.otf"
ITAL = f"{FONT_DIR}/texgyretermes-italic.otf"
OUT = os.path.join(os.path.dirname(__file__), "..", "img")
os.makedirs(OUT, exist_ok=True)

NAVY   = (26, 42, 74)
NAVY2  = (44, 68, 118)
GOLD   = (212, 175, 55)
WHITE  = (255, 255, 255)
CREAM  = (247, 244, 235)


def font(sz, bold=False, italic=False):
    return ImageFont.truetype(BOLD if bold else (ITAL if italic else REG),
                              int(sz))


def vgradient(w, h, top, bottom):
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        t = y / (h - 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        for x in range(w):
            px[x, y] = (r, g, b)
    return img


def paper_texture(img, strength=1):
    """Grano sutil (estilo papel) que aumenta el peso PNG de forma natural."""
    w, h = img.size
    px = img.load()
    rnd = random.Random(2026)
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            dr = rnd.randint(-strength, strength)
            r, g, b = px[x, y]
            px[x, y] = (max(0, min(255, r + dr)),
                        max(0, min(255, g + dr)),
                        max(0, min(255, b + dr)))
    return img


def circles(draw, w, h, center, maxr, color=(60, 85, 135), alpha_step=2):
    cx, cy = center
    r = maxr
    while r > 0:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                     outline=color, width=1)
        r -= maxr // 16


def portada():
    W, H = 2067, 2923  # A4 @ 250 dpi
    img = vgradient(W, H, (22, 34, 62), (38, 62, 108))
    d = ImageDraw.Draw(img)
    # redes de círculos (estilo circuito/onda)
    random.seed(7)
    for cx in range(200, W + 300, 460):
        for cy in range(200, H + 300, 460):
            circles(d, W, H, (cx, cy), 190, color=(58, 84, 136))
    # franja dorada
    d.rectangle([0, int(H * 0.60), W, int(H * 0.60) + 8], fill=GOLD)
    d.rectangle([0, int(H * 0.60) + 34, W, int(H * 0.60) + 37], fill=GOLD)
    # título
    t1 = "ELECTROTECNIA"
    t2 = "INDUSTRIAL"
    f1 = font(158, bold=True)
    f2 = font(158, bold=True)
    t1w = d.textlength(t1, font=f1)
    t2w = d.textlength(t2, font=f2)
    d.text(((W - t1w) / 2, 1000), t1, font=f1, fill=WHITE)
    d.text(((W - t2w) / 2, 1210), t2, font=f2, fill=GOLD)
    # subtítulo
    sub = "Desde fundamentos hasta máquinas e instalaciones"
    fs = font(60)
    sw = d.textlength(sub, font=fs)
    d.text(((W - sw) / 2, 1520), sub, font=fs, fill=(214, 222, 238))
    # fórmulas decorativas
    fm = ["V = I · R", "P = V · I", "Z = R + jX", "S = P + jQ",
          "E = K·φ·ω", "Ud = Id · RA"]
    ff = font(48, italic=True)
    for i, f in enumerate(fm):
        fw = d.textlength(f, font=ff)
        col = (168, 186, 220)
        if i % 2 == 0:
            d.text((200, 1960 + i * 108), f, font=ff, fill=col)
        else:
            d.text((W - 200 - fw, 1960 + i * 108), f, font=ff, fill=col)
    # pie
    pie1 = "KyonX1 · 2026"
    fp = font(55, bold=True)
    pw = d.textlength(pie1, font=fp)
    d.text(((W - pw) / 2, 2540), pie1, font=fp, fill=(232, 236, 246))
    pie2 = "Texto de referencia para nivel intermedio-avanzado (C/D)"
    fp2 = font(35)
    pw2 = d.textlength(pie2, font=fp2)
    d.text(((W - pw2) / 2, 2640), pie2, font=fp2, fill=(180, 194, 218))
    pie3 = "Publicado bajo CC BY-SA 4.0"
    fp3 = font(35)
    pw3 = d.textlength(pie3, font=fp3)
    d.text(((W - pw3) / 2, 2730), pie3, font=fp3, fill=(150, 168, 200))
    path = os.path.join(OUT, "portada.png")
    paper_texture(img, strength=1)
    img.save(path, "PNG")
    print(f"  portada.png: {os.path.getsize(path)//1024} KB")


def hoja_formula(name, titulo, formulas):
    """Hoja de repaso: marco azul + formulas por capitulo (~1600x2200)."""
    W, H = 1300, 1788
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([40, 40, W - 40, H - 40], outline=NAVY, width=8)
    # cabecera
    d.rectangle([40, 40, W - 40, 240], fill=NAVY)
    fh = font(68, bold=True)
    hw = d.textlength(titulo, font=fh)
    d.text(((W - hw) / 2, 130), titulo, font=fh, fill=GOLD,
           anchor="mm")
    fsub = font(39)
    sw = d.textlength("Hoja de fórmulas", font=fsub)
    d.text(((W - sw) / 2, 300), "Hoja de fórmulas", font=fsub,
           fill=NAVY, anchor="mm")
    d.line([120, 370, W - 120, 370], fill=GOLD, width=5)
    y = 400
    ff = font(47)
    for lab, f in formulas:
        if y > H - 200:
            break
        # etiqueta
        d.rectangle([110, y, 400, y + 90], fill=(232, 237, 247))
        d.text((255, y + 45), lab, font=font(36, bold=True),
               fill=NAVY, anchor="mm")
        # formula
        fw = d.textlength(f, font=ff)
        d.text((W - 160 - fw, y + 45), f, font=ff, fill=NAVY, anchor="mm")
        y += 145
    path = os.path.join(OUT, name)
    paper_texture(img, strength=2)
    img.save(path, "PNG")
    print(f"  {name}: {os.path.getsize(path)//1024} KB")


def portadilla(numero, titulo, subtitulo):
    """Pagina A4 ~210dpi de separacion de capitulo (estilo portada)."""
    W, H = 1754, 2480
    img = vgradient(W, H, (24, 38, 68), (40, 66, 114))
    d = ImageDraw.Draw(img)
    random.seed(100 + numero)
    for cx in range(150, W + 300, 520):
        for cy in range(150, H + 300, 520):
            circles(d, W, H, (cx, cy), 170, color=(58, 84, 136))
    # numero grande
    fn = font(210, bold=True)
    nw = d.textlength(f"0{numero}", font=fn)
    d.text(((W - nw) / 2, 800), f"0{numero}", font=fn, fill=GOLD)
    # titulo
    ft = font(105, bold=True)
    tw = d.textlength(titulo, font=ft)
    if tw > W - 300:
        ft = font(77, bold=True)
        tw = d.textlength(titulo, font=ft)
    d.text(((W - tw) / 2, 1200), titulo, font=ft, fill=WHITE)
    # lineas
    d.rectangle([int(W * 0.30), 1400, int(W * 0.70), 1404], fill=GOLD)
    # subtitulo
    fst = font(35)
    stw = d.textlength(subtitulo, font=fst)
    d.text(((W - stw) / 2, 1520), subtitulo, font=fst, fill=(200, 212, 236))
    path = os.path.join(OUT, f"portadilla-{numero:02d}.png")
    paper_texture(img, strength=1)
    img.save(path, "PNG")
    print(f"  portadilla-{numero:02d}.png: {os.path.getsize(path)//1024} KB")


if __name__ == "__main__":
    portada()
    portadillas = [
        (1, "Fundamentos", "Carga, campo, potencial y energía eléctrica"),
        (2, "Corriente Directa", "Leyes de Kirchhoff, Thévenin y Norton"),
        (3, "Corriente Alterna", "Fasores, impedancia, potencia y trifásica"),
        (4, "Máquinas Eléctricas", "Transformadores, motores DC e inducción"),
        (5, "Instalaciones Eléctricas", "Esquemas TT/TN, protección y puesta a tierra"),
        (6, "Ejercicios Resueltos", "Problemas resueltos y propuestos"),
        (7, "Apéndice", "Tablas, constantes y fórmulas"),
    ]
    for n, t, s in portadillas:
        portadilla(n, t, s)
    hoja_formula(
        "hoja-f01.png", "Cap. 1 · Fundamentos",
        [("Carga", "q = n·e"), ("Coulomb", "F = k·q1·q2 / r²"),
         ("E = F/q", "E = k·Q / r²"), ("Potencial", "V = k·Q / r"),
         ("Capacitor", "Q = C·V"), ("Energía cap.", "W = ½·C·V²"),
         ("E en cap.", "E = V / d"), ("Campo cond.", "ρ = R·S / L")])
    hoja_formula(
        "hoja-f02.png", "Cap. 2 · Corriente Directa",
        [("Ohm", "V = I·R"), ("Potencia", "P = V·I = I²·R = V²/R"),
         ("Resistencias serie", "Req = R1 + R2 + …"),
         ("Resistencias paralelo", "1/Req = 1/R1 + 1/R2 + …"),
         ("Divisor tensión", "Vx = V·Rx / Req"),
         ("Divisor corriente", "Ix = I·Req / Rx"),
         ("KCL nodos", "Σ Ientra = Σ Isale"),
         ("KVL mallas", "Σ V = 0")])
    hoja_formula(
        "hoja-f03.png", "Cap. 3 · Corriente Alterna",
        [("Fasor", "v = Vm·cos(ωt + φ)"), ("Reactancia L", "XL = ω·L"),
         ("Reactancia C", "XC = 1 / (ω·C)"), ("Impedancia", "Z = R + jX"),
         ("Ley Ohm AC", "V = I·Z"), ("Pot. activa", "P = V·I·cos φ"),
         ("Pot. reactiva", "Q = V·I·sin φ"), ("Pot. aparente", "S = V·I"),
         ("Triángulo", "S² = P² + Q²"), ("Resonancia", "fr = 1 / (2π√(LC))")])
    hoja_formula(
        "hoja-f04.png", "Cap. 4 · Máquinas Eléctricas",
        [("Transformador", "V2/V1 = N2/N1 = a"),
         ("Corrientes trans.", "N1·I1 = N2·I2"),
         ("Potencia ideal", "V1·I1 = V2·I2"),
         ("Motor DC", "E = K·φ·ω"), ("Par motor", "T = K·φ·Ia"),
         ("Velocidad DC", "n = (V − Ia·Ra) / (K·φ)"),
         ("Motor induc. sinc.", "ns = 120·f / p"),
         ("Deslizamiento", "s = (ns − n) / ns")])
    hoja_formula(
        "hoja-f05.png", "Cap. 5 · Instalaciones Eléctricas",
        [("Esquema TT", "Ud = Id·(RA + RB)"),
         ("Limite TT", "RA ≤ 50 V / Id"), ("Caída tensión", "ΔV = I·R"),
         ("Sección (DC)", "S = 2·L·I / (γ·ΔV máx)"),
         ("Pot. trifásica", "P = √3·VL·IL·cos φ"),
         ("Resist. tierra", "RA = ρ / (2·π·r)"),
         ("Tiempo RCD", "t ≤ 0.2 s (TT)"),
         ("Disparo RCD", "Ia ≤ Id")])
    hoja_formula(
        "hoja-f06.png", "Cap. 6 · Ejercicios",
        [("Estrategia 1", "Dibujar circuito y sentidos"),
         ("Estrategia 2", "Aplicar KCL en nodos"),
         ("Estrategia 3", "Aplicar KVL en mallas"),
         ("Estrategia 4", "Thévenin: Vth, Rth"),
         ("Estrategia 5", "Norton: In, Rn"),
         ("Estrategia 6", "Verificar unidades SI"),
         ("Estrategia 7", "Comprobar signos y orden"),
         ("Estrategia 8", "Revisar con simulación")])
    print("Listo.")