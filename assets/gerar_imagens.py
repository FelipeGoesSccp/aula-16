from PIL import Image, ImageDraw
import os

os.makedirs(r"C:\Users\Aluno\Desktop\atividade 16\assets", exist_ok=True)
os.chdir(r"C:\Users\Aluno\Desktop\atividade 16\assets")

# ============================================================
# ICON.PNG - 1024x1024 pixels
# Fundo sólido opaco, sem cantos arredondados manuais
# Tema: Joystick Retro - paleta roxa/neon
# ============================================================
icon_size = 1024
icon = Image.new('RGBA', (icon_size, icon_size), (26, 10, 46, 255))
draw = ImageDraw.Draw(icon)

# Gradiente de fundo (linhas horizontais)
for i in range(icon_size):
    ratio = i / icon_size
    r = int(26 + ratio * 18)
    g = int(10 + ratio * 5)
    b = int(46 + ratio * 28)
    draw.line([(0, i), (icon_size, i)], fill=(r, g, b, 255))

cx, cy = icon_size // 2, icon_size // 2

# Circulo externo (moldura)
draw.ellipse([cx-320, cy-320, cx+320, cy+320], fill=(45, 27, 78, 255), outline=(139, 92, 246, 255), width=14)
# Circulo interno
draw.ellipse([cx-240, cy-240, cx+240, cy+240], fill=(26, 10, 46, 255), outline=(168, 85, 247, 255), width=8)

# D-pad (cruz direcional)
pad_color = (109, 40, 217, 255)
pad_outline = (139, 92, 246, 255)
# horizontal
draw.rectangle([cx-130, cy-50, cx+130, cy+50], fill=pad_color, outline=pad_outline, width=4)
# vertical
draw.rectangle([cx-50, cy-130, cx+50, cy+130], fill=pad_color, outline=pad_outline, width=4)
# centro do d-pad
draw.rectangle([cx-50, cy-50, cx+50, cy+50], fill=(88, 28, 135, 255))

# Botao B (vermelho) - direita
draw.ellipse([cx+150, cy-45, cx+220, cy+25], fill=(239, 68, 68, 255), outline=(252, 165, 165, 255), width=4)
draw.text((cx+185, cy-10), 'B', fill=(255,255,255,255), anchor='mm')

# Botao A (verde) - abaixo de B
draw.ellipse([cx+100, cy+40, cx+170, cy+110], fill=(34, 197, 94, 255), outline=(134, 239, 172, 255), width=4)
draw.text((cx+135, cy+75), 'A', fill=(255,255,255,255), anchor='mm')

# Ponto central (analogico)
draw.ellipse([cx-30, cy-30, cx+30, cy+30], fill=(196, 181, 253, 255), outline=(167, 139, 250, 255), width=3)

# Faixa inferior com texto RETRO
draw.rectangle([cx-200, cy+175, cx+200, cy+250], fill=(76, 29, 149, 255), outline=(139, 92, 246, 255), width=4)
draw.text((cx, cy+212), 'RETRO', fill=(233, 213, 255, 255), anchor='mm')

# Estrelas pixel art nos cantos
for sx, sy in [(80,80), (944,80), (80,944), (944,944)]:
    star_c = (251, 191, 36, 255)
    draw.rectangle([sx-8, sy-8, sx+8, sy+8], fill=star_c)
    draw.rectangle([sx-3, sy-16, sx+3, sy+16], fill=star_c)
    draw.rectangle([sx-16, sy-3, sx+16, sy+3], fill=star_c)

# Converter para RGB (sem alpha) para salvar como PNG opaco
icon_rgb = Image.new('RGB', (icon_size, icon_size), (26, 10, 46))
icon_rgb.paste(icon, mask=icon.split()[3])
icon_rgb.save('icon.png', 'PNG')
print(f"icon.png salvo: {icon_size}x{icon_size}")

# ============================================================
# SPLASH.PNG - 2732x2732 pixels
# Logo centralizada na Safe Zone (centro 1152x1152)
# ============================================================
splash_size = 2732
splash = Image.new('RGB', (splash_size, splash_size), (26, 10, 46))
draw2 = ImageDraw.Draw(splash)

# Gradiente de fundo
for i in range(splash_size):
    ratio = i / splash_size
    r = int(26 + ratio * 12)
    g = int(10 + ratio * 6)
    b = int(46 + ratio * 35)
    draw2.line([(0, i), (splash_size, i)], fill=(r, g, b))

# Grade pixel decorativa (fora da safe zone - ok)
grid_color = (38, 18, 65)
for x in range(0, splash_size, 100):
    draw2.line([(x, 0), (x, splash_size)], fill=grid_color, width=1)
for y in range(0, splash_size, 100):
    draw2.line([(0, y), (splash_size, y)], fill=grid_color, width=1)

scx, scy = splash_size // 2, splash_size // 2
# Safe zone aprox: centro 1152x1152 => raio 576

# Circulo principal (dentro da safe zone)
draw2.ellipse([scx-500, scy-500, scx+500, scy+500], fill=(45, 27, 78), outline=(139, 92, 246), width=20)
draw2.ellipse([scx-460, scy-460, scx+460, scy+460], fill=(26, 10, 46), outline=(168, 85, 247), width=12)

# D-pad grande centralizado
pw = 190
draw2.rectangle([scx-pw, scy-70, scx+pw, scy+70], fill=(109,40,217), outline=(139,92,246), width=5)
draw2.rectangle([scx-70, scy-pw, scx+70, scy+pw], fill=(109,40,217), outline=(139,92,246), width=5)
draw2.rectangle([scx-70, scy-70, scx+70, scy+70], fill=(88,28,135))

# Botoes ABXY
buttons = [
    (scx+260, scy-60, (239,68,68), (252,165,165), 'B'),
    (scx+310, scy-160, (34,197,94), (134,239,172), 'A'),
    (scx+210, scy-160, (59,130,246), (147,197,253), 'X'),
    (scx+260, scy-260, (245,158,11), (252,211,77), 'Y'),
]
for bx, by, fill, outline, label in buttons:
    draw2.ellipse([bx-50, by-50, bx+50, by+50], fill=fill, outline=outline, width=5)
    draw2.text((bx, by), label, fill=(255,255,255), anchor='mm')

# Centro analogico
draw2.ellipse([scx-40, scy-40, scx+40, scy+40], fill=(196,181,253), outline=(167,139,250), width=4)

# Titulo acima (dentro safe zone)
draw2.rectangle([scx-520, scy-640, scx+520, scy-520], fill=(76,29,149), outline=(139,92,246), width=6)
draw2.text((scx, scy-580), 'RETRO GAMES', fill=(233,213,255), anchor='mm')

# Subtitulo abaixo (dentro safe zone)
draw2.rectangle([scx-420, scy+520, scx+420, scy+610], fill=(49,46,129), outline=(129,140,248), width=4)
draw2.text((scx, scy+565), 'Catalogo & Coleccionaveis', fill=(199,210,254), anchor='mm')

# Estrelas decorativas nos 4 cantos (fora safe zone - decorativo)
for px, py in [(250,250), (2482,250), (250,2482), (2482,2482)]:
    for sz, col in [(50,(251,191,36)), (25,(245,158,11))]:
        draw2.ellipse([px-sz, py-sz, px+sz, py+sz], fill=col)

splash.save('splash.png', 'PNG')
print(f"splash.png salvo: {splash_size}x{splash_size}")
print("Ambas as imagens geradas com sucesso!")
