# -*- coding:utf-8 -*-
import os
from PIL import Image


class Image_Change:
    def __init__(self, type=['.jpg', '.jpeg', '.png'], size=[640, 1136]):
        self.new_path = ''
        self.old_path = ''
        self.img_type = type
        self.iphone5 = size

    def cope_path(self, path, root, new_root='ImgTest'):
        self.old_path = root
        self.new_path = root.replace(path, new_root, 1)
        if not os.path.exists(self.new_path):
            os.mkdir(self.new_path)

    def mod_image(self, files):
        for f in files:
            im_name, im_type = os.path.splitext(f)
            if im_type in self.img_type:
                im = Image.open(os.path.join(self.old_path, f))
                im_w, im_h = im.size
                if im_w < self.iphone5[0] and im_h < self.iphone5[1]:
                    new_im = im.resize((im_w, im_h), Image.ANTIALIAS)
                elif (im_w / self.iphone5[0]) > (im_h / self.iphone5[1]):
                    new_im = im.resize((self.iphone5[0], int(im_h * self.iphone5[0] / im_w)), Image.ANTIALIAS)
                else:
                    new_im = im.resize((int(im_w * self.iphone5[1] / im_h), self.iphone5[1]), Image.ANTIALIAS)
                new_im.save(os.path.join(self.new_path, 'new_' + f))
                im.close()


if __name__ == '__main__':
    im_mod = Image_Change()
    path = 'MyImg'
    for (root, dirs, files) in os.walk(path):
        im_mod.cope_path(path, root)
        im_mod.mod_image(files)
