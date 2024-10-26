from PIL import Image, ImageDraw, ImageOps, ImageFont



def fit_one_im_into_another(big_im:Image, small_im: Image, factor:float) -> Image:
    max_w, max_h = big_im.size
    max_w *= factor
    max_h *= factor

    small_w, small_h = small_im.size
    fact_w = max_w / small_w
    fact_h = max_h / small_h
    fact = fact_w if fact_w < fact_h else fact_h

    return ImageOps.contain(small_im, (int(small_w * fact), int(small_h * fact)))

base = ImageOps.contain(Image.open("orig.webp"), (720, 540))
base_w, base_h = base.size
# print(base.size)
# base.show()

icon = Image.open('sun.png')
# print(icon.size)

icon = fit_one_im_into_another(base, icon, 0.5)
# print(icon.size)

# base.show()
# icon.show()

base.paste(icon, (int(base_w * 0.2), int(0)))  # base_h * 0.66)))
# base.show()

# make a blank image for the text, initialized to transparent text color
txt = Image.new("RGBA", base.size, (0, 0, 0, 0))

# get a font
fnt = ImageFont.truetype("C:\\Windows\\Fonts\\segoesc.ttf", 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((base_w * 0.25, base_h * .6), "Привет,", font=fnt, fill=(255, 255, 255, 128))
# draw text, full opacity
d.text((base_w * 0.25, base_h * .6 + 50), "дорогой!", font=fnt, fill=(255, 255, 255, 255))
# draw text, half opacity
d.text((base_w * 0.25 - 30, base_h * .6 + 100), "Мр-ррррр...", font=fnt, fill= 'yellow') # (255, 255, 255, 128))


out = Image.alpha_composite(base.convert('RGBA'), txt)
out.show()

