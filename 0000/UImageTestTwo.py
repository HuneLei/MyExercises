# -*- coding: cp936 -*-

from PIL import Image, ImageFont, ImageDraw

image = 'two_blue.jpg'
test = '100'
font = 'simsun.ttc'
color = (255, 10, 10)


def image_test(image, test, font, color):
    try:
        im = Image.open(image)
        im_w, im_h = im.size
        im_font = ImageFont.truetype(font, im_h // 4)
        im_draw = ImageDraw.Draw(im)
        test_w, test_h = im_draw.textsize(test, font=im_font)
        im_draw.text(((im_w - test_w), 0), test, fill=color, font=im_font)
        im.save('test_two.png')
    except:
        print 'Modify the failure!'


if __name__ == '__main__':
    image_test(image, test, font, color)
