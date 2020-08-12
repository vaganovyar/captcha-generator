from PIL import Image, ImageDraw, ImageFont
from random import randint
import numpy as np

def make_capthcha(src, text, color, size=30, resolution=(120, 60), step=30, noize=0):
    img = Image.new('RGBA', resolution, 'white')
    idraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size=size)
    now = 1
    for symbol in text:
        idraw.text((now, randint(1, resolution[1] - size)), symbol, font=font, fill=color)
        now += randint(step, 2 * step)
    img = np.asarray(img)
    img = img.copy()
    img.setflags(write=1)
    for line in img:
        for pixel in line:
            pixel[0] = (pixel[0] + randint(-noize, noize)) % 256
            pixel[1] = (pixel[1] + randint(-noize, noize)) % 256
            pixel[2] = (pixel[2] + randint(-noize, noize)) % 256
    img = Image.fromarray(img)
    img.save(src)

    return np.asarray(img)

"""debugging"""
"""
print(make_capthcha("test.png", "test", "green", 30, (120, 60), 15, 2))
"""
