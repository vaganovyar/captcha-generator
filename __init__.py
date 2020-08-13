from PIL import Image, ImageDraw, ImageFont
from random import randint
import numpy as np

def make_capthca(src, text, color, size=30, resolution=(120, 60), step=30, noize=255, chance=0.5):
    img = Image.new("RGBA", resolution,"white")
    font = ImageFont.truetype("arial.ttf", size=size)
    now = 1

    for symbol in text:

        width, height = font.getsize(symbol)
        img2 = Image.new("RGBA", (width, height), "white")
        draw2 = ImageDraw.Draw(img2)
        draw2.text((0, 0), text=symbol, font=font, fill=color)
        img2 = img2.rotate(randint(-90, 90), expand=1)
        y = randint(0, resolution[1] - height)
        sx, sy = img2.size
        img.paste(img2, (now, y, now + sx, y + sy), img2)

        now += randint(height, height + step)

    width, height = img.size
    for i in range(randint(1, 5)):
        draw = ImageDraw.Draw(img)
        draw.line((randint(1, width), randint(1, height), randint(1, width), randint(1, height)), width=randint(1, 5), fill=color)

    img = np.asarray(img)
    img = img.copy()
    img.setflags(write=1)
    for line in img:
        for pixel in line:
            if randint(0, 100) < chance:
                pixel[0] = (pixel[0] + randint(-noize, noize)) % 256
                pixel[1] = (pixel[1] + randint(-noize, noize)) % 256
                pixel[2] = (pixel[2] + randint(-noize, noize)) % 256

    img = Image.fromarray(img)
    img.save(src)

    return np.asarray(img)

"""debugging"""
"""
print(make_capthcha("test.png", "test", "green", 30, (120, 60), 5, 255, 10))
"""
