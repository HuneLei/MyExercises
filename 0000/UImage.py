#-*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
# ImageDraw在原来的图像上绘制
# ImageFont设置字体

im = Image.open('ascii_dora.png')
w, h = im.size
font = ImageFont.truetype('simsun.ttc', 30)
imDraw = ImageDraw.Draw(im)
imDraw.text((w-20, 0), '5', fill=(255, 10, 10), font=font)
im.save('0.0.png', 'png')
