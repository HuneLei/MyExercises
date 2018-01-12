# -*- coding: cp936 -*-
import argparse  # ����������ģ��
from PIL import Image, ImageDraw, ImageFont  # ����ͼƬ����ģ��

parser = argparse.ArgumentParser()

parser.add_argument('file')  # �����ļ�
parser.add_argument('--num', type=int)  # Ҫд������ֱ���������
parser.add_argument('--msg', type=str)  # Ҫд������ֱ���������
parser.add_argument('--type', default='png')  # Ҫд���ͼƬ�ĸ�ʽ


# ͼƬ����
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
    test_w, test_h = imDraw.textsize(strmsg, font=imFont) # ��ȡ��������Ŀ�Ⱥͳ���
    imDraw.text(((w - test_w), 0), strmsg, fill=(255, 10, 10), font=imFont)
    try:
        im.save('test.' + type)
    except ValueError as error:
        print error
        print 'ͼƬ��ʽ����'


try:
    args = parser.parse_args()
    manage_image(args)
except IOError as error:
    print error
