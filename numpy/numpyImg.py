# coding=utf-8
import numpy as np
from PIL import Image
from PIL import ImageDraw

img_path = "X:\jet_python\study\python_study\image\data\cool.jpg"
img = Image.open(img_path)
draw = ImageDraw.Draw(img)
draw.line((0, 0, 300, 500),"yellow")
img_array = np.array(img)
for i in range(100):
    img_array[i, i * 2] = (255, 0, 0)

img_new = Image.fromarray(img_array)
img_new.show()
'''
image.open()打开的图片，方向是向右为x正方向，向下为y正方向.
转化为nparray后，向下为x的正方向，向右为y的正方向.
'''

# img_path = "X:\jet_python\study\python_study\image\data\cool.jpg"
# im = Image.open(img_path)
# # res = im.getpixel((999, 66 ))
# # print(res)
# box = (100, 100, 200, 300)
# region = im.crop(box)
# region.show()