# -*- coding:utf-8 -*-
# 生成字母验证码图
import random, string
from PIL import Image, ImageFont, ImageDraw, ImageFilter


def random_color():
    return tuple([random.randint(50, 100) for _ in range(3)])  # 获取随机颜色


def verify_picture():
    letters = [random.choice(string.letters) for i in range(4)]  # 获取四个随机字符
    font = ImageFont.truetype('simsun.ttc', 50)
    width, height = 240, 60
    pic = Image.new('RGB', (width, height), (200, 200, 200))
    draw = ImageDraw.Draw(pic)
    for i, letter in enumerate(letters):
        draw.text((60 * i + random.randrange(0, 20), random.randrange(0, 20)), letter, font=font, fill=random_color())
    for i in xrange(5000):
        # draw.point 图片上描一个点
        draw.point((random.randint(0, width), random.randint(0, height)), fill=random_color())
    pic = pic.filter(ImageFilter.BLUR)
    # ImageFilter.BLUR为模糊滤波，处理之后的图像会整体变得模糊
    # http://blog.csdn.net/icamera0/article/details/50708888 可见更多介绍
    pic.save('pic_save.png', 'png')


if __name__ == '__main__':
    verify_picture()
