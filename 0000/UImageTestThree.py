# -*- coding: cp936 -*-
from PIL import Image, ImageDraw, ImageFont


class Modify_image_test:
    def __init__(self):
        self.image = None
        self.font = None

    def open(self, file):
        self.image = Image.open(file)

    def setFint(self, font='simsun.ttc', size=-1):
        if size < 0: size = self.image.size[1] // 4
        self.font = ImageFont.truetype(font, size)

    def modTest(self, test=1, color=(255, 10, 10), name='today_test.png'):
        im_Draw = ImageDraw.Draw(self.image)
        test_w, test_h = im_Draw.textsize(str(test), self.font)
        im_Draw.text(((self.image.size[0] - test_w), 0), str(test), fill=color, font=self.font)
        self.image.save(name)


if __name__ == '__main__':
    im = Modify_image_test()
    im.open('two_blue.jpg')
    im.setFint('ahronbd.ttf', 100)
    im.modTest('ABC', (10, 10, 10), '0000.png')
