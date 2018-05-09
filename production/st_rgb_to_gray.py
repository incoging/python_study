# coding=utf-8
# 此文档是把RGG图像转化为灰度图
import numpy
from PIL import Image
from skimage import color
import cv2
import os
from pylab import *

# 方法一：利用公式计算
imgpath = "X:\jet_python\ipiut2\\1_1_cut/1_1.bmp"
# f, ext = os.path.splitext(imgpath)
lena = cv2.imread(imgpath)
img = lena
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
value = [0] * 3
gray_img = numpy.zeros([height, width], numpy.uint8)

for row in range(height):
    for column in range(width):
        for chan in range(channels):
            value[chan] = img[row, column, chan]
        R = value[2]
        G = value[1]
        B = value[0]
        # new_value = 0.2989 * R + 0.5870 * G + 0.1140 * B
        new_value = 0.2989 * R + 0.5870 * G + 0.1140 * B  # 转为灰度像素
        gray_img[row, column] = new_value

gray_img = Image.fromarray(uint8(gray_img))
gray_img.save("./data/1_22222.bmp")


# 方法二：利用python自带的方法。
# imgpath = "X:\jet_python\ipiut2\\1_1_cut/1_1.bmp"
# img = Image.open(imgpath)
# img = img.convert("L")
# img.save("./data/1_11111.bmp")
