from PIL import Image, ImageDraw, ImageFont
from random import randint
import numpy as np


def make_capthca(text, color="green", src=None, size=30, resolution=(120, 60), step=30, noise=255, chance=10):

    # Make image for drawing on it
    img = Image.new("RGBA", resolution, "white")
    now = 1

    # Make data
    data = {}
    positions = {}

    # Draw symbol and update data
    end_text = ""
    for symbol in text:
        font = ImageFont.truetype("arial.ttf", size=randint(size - 10, size))
        width, height = font.getsize(symbol)
        img2 = Image.new("RGBA", (width, height), "white")
        draw2 = ImageDraw.Draw(img2)
        draw2.text((0, 0), text=symbol, font=font, fill=color)
        img2 = img2.rotate(randint(-90, 90), expand=1)
        y = randint(0, resolution[1] - height)
        sx, sy = img2.size

        if now + sx <= resolution[0] and y + sy <= resolution[1]:
            img.paste(img2, (now, y, now + sx, y + sy), img2)
            end_text += symbol

            try:
                positions[symbol].append([now, y, now + sx, y + sy])
            except:
                positions[symbol] = [[now, y, now + sx, y + sy]]

            now += randint(height, height + step)

    text = end_text
    data["label"] = text

    # Draw lines
    width, height = img.size
    for i in range(randint(1, 5)):
        draw = ImageDraw.Draw(img)
        draw.line((randint(1, width), randint(1, height), randint(1, width), randint(1, height)), width=randint(1, 5),
                  fill=color)

    # Make some noize
    img = np.asarray(img)
    img = img.copy()
    img.setflags(write=1)
    for line in img:
        for pixel in line:
            if randint(0, 100) < chance:
                pixel[0] = (pixel[0] + randint(-noise, noise)) % 256
                pixel[1] = (pixel[1] + randint(-noise, noise)) % 256
                pixel[2] = (pixel[2] + randint(-noise, noise)) % 256

    # Update data
    img = Image.fromarray(img)
    if src:
        img.save(src)
    data["symbols"] = positions
    data["image"] = np.asarray(img)

    return data


"""debugging"""
"""
print(make_capthca("test012",
                   "green",
                   "test.png",
                   size=30,
                   resolution=(120, 60),
                   step=1,
                   noise=255,
                   chance=10))
"""
