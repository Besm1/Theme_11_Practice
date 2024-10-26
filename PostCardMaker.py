from PIL import Image, ImageDraw, ImageOps, ImageFont

class PostCardMaker:
    def __init__(self, substrate_picture:str, smile_picture:str, text:str, max_card_size=None, smile_coord=None, text_coord=None):
        self.substrate_picture = substrate_picture
        self.smile_picture = smile_picture
        self.text = text
        self.smile_coord = smile_coord
        self.text_coord = text_coord
        self.max_card_size = max_card_size

    def make_postcard(self, text_color):
        base = Image.open(self.substrate_picture)
        base = ImageOps.contain(base, base.size if self.max_card_size is None else self.max_card_size)
        base_w, base_h = base.size
        # print(base.size)
        # base.show()

        icon = Image.open(self.smile_picture)
        # print(icon.size)

        icon = self._fit_one_im_into_another(base, icon, 0.5)

        base.paste(icon, (int(base_w * 0.2), int(0)) if self.smile_coord is None else self.smile_coord)  # base_h * 0.66)))

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (0, 0, 0, 0))

        # get a font
        fnt = ImageFont.truetype("C:\\Windows\\Fonts\\segoesc.ttf", 40)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text((base_w * 0.25, base_h * .6) if self.text_coord is None else self.text_coord, self.text, font=fnt
               , fill=(255, 255, 255, 128) if text_color is None else text_color)

        return Image.alpha_composite(base.convert('RGBA'), txt)

    def _fit_one_im_into_another(self, big_im:Image, small_im: Image, factor:float) -> Image:
        max_w, max_h = big_im.size
        max_w *= factor
        max_h *= factor

        small_w, small_h = small_im.size
        fact_w = max_w / small_w
        fact_h = max_h / small_h
        fact = fact_w if fact_w < fact_h else fact_h

        return ImageOps.contain(small_im, (int(small_w * fact), int(small_h * fact)))

if __name__ == '__main__':
    pic = PostCardMaker(substrate_picture="orig.webp", max_card_size=(720, 540), smile_picture='sun.png',
                        text='Привет,\nдорогой!\nМ-ррр...')

    pic.make_postcard(text_color='red').show()

