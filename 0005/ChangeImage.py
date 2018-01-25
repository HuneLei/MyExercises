# -*- coding:utf-8 -*-
import os
from PIL import Image

ext = ['.jpg', '.jpeg', '.png']


def Mod_Image(Root='MyImg', Dest='MyImgTest', walk_file='MyImg'):
    file = os.walk(walk_file)
    for (root, dirs, files) in file:
        New_Root = root.replace(Root, Dest, 1)
        if not os.path.exists(New_Root):
            os.mkdir(New_Root)
        for f in files:
            (image_name, image_type) = os.path.splitext(f)
            if image_type in ext:
                old_path = os.path.join(root, f)
                new_path = os.path.join(New_Root, 'new' + f)
                im = Image.open(old_path)
                im_w, im_h = im.size
                mew_im = im.resize((int(im_w / 2), int(im_h / 2)), Image.ANTIALIAS)
                mew_im.save(new_path)
                im.close()
                mew_im.close()


if __name__ == '__main__':
    Mod_Image()
