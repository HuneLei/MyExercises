# -*- coding: cp936 -*-
import argparse  # 引入命令行模块
from PIL import Image, ImageDraw, ImageFont  # 引入图片处理模块

parser = argparse.ArgumentParser()

parser.add_argument('file')  # 输入文件
parser.add_argument('--num', type=int)  # 要写入的文字必须是数字
parser.add_argument('--msg', type=str)  # 要写入的文字必须是文字
parser.add_argument('--type', default='png')  # 要写入的图片的格式


# 图片处理
def manage_image(args):
    file, msg, type = args.file, args.msg, args.type
    im = Image.open(file)
    w, h = im.size
    imFont = ImageFont.truetype('simsun.ttc', 30)
    imDraw = ImageDraw.Draw(im)
    lenth = len(msg)
    strmsg = ''
    for i in range(lenth):
        if (i + 1) % 9 == 0:
            strmsg = strmsg + msg[i - 8:i + 1] + '\n'
        elif (i + 1) == lenth:
            strmsg = strmsg + msg[lenth - 8:i + 1] + '\n'
    test_w, test_h = imDraw.textsize(strmsg, font=imFont) # 获取输入字体的宽度和长度
    imDraw.text(((w - test_w), 0), strmsg, fill=(255, 10, 10), font=imFont)
    try:
        im.save('test.' + type)
    except ValueError as error:
        print error
        print '图片格式错误！'


try:
    args = parser.parse_args()
    manage_image(args)
except IOError as error:
    print error
