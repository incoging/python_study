# 输入是一个已经通过Image.open打开的文件对象。输出也是同种类型

from PIL import Image
import math
import numpy as np


def thresHold(img):
    # img = Image.open()
    R_level = np.zeros(256)
    G_level = np.zeros(256)
    B_level = np.zeros(256)
    # print(gray_level)

    lowCut = 0.005
    highCut = 0.005

    for i in range(img.size[0]):  # 统计R,G,B三个通道的像素信息
        for j in range(img.size[1]):  # print(img.getpixel((i,j))[0])
            value_r = img.getpixel((i, j))[0]
            R_level[value_r] += 1

            value_g = img.getpixel((i, j))[1]
            G_level[value_g] += 1

            value_b = img.getpixel((i, j))[2]
            B_level[value_b] += 1

    # 求出RGB各个通道的对应lowCut和highCut的最小最大像素值
    pixelAmount = img.size[0] * img.size[1]

    minRed = 0
    minGreen = 0
    minBlue = 0
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    sum1_r = 0
    for index in range(256):
        sum1_r = sum1_r + R_level[index]
        if sum1_r >= pixelAmount * lowCut * 0.01:
            minRed = index
            break

    sum1_g = 0
    for index in range(256):
        sum1_g = sum1_g + G_level[index]
        if sum1_g >= pixelAmount * lowCut * 0.01:
            minGreen = index
            break

    sum1_b = 0
    for index in range(256):
        sum1_b = sum1_b + B_level[index]
        if sum1_b >= pixelAmount * lowCut * 0.01:
            minBlue = index
            break

    sum2_r = 0
    for index in range(255, -1, -1):
        sum2_r += R_level[index]
        if float(sum2_r) >= pixelAmount * highCut * 0.01:
            maxRed = index
            break

    sum2_g = 0
    for index in range(255, -1, -1):
        sum2_g += R_level[index]
        if float(sum2_g) >= pixelAmount * highCut * 0.01:
            maxGreen = index
            break

    sum2_b = 0
    for index in range(255, -1, -1):
        sum2_b += R_level[index]
        if float(sum2_b) >= pixelAmount * highCut * 0.01:
            maxBlue = index
            break

    # 映射变换
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixel_value_r = img.getpixel((i, j))[0]
            if pixel_value_r <= minRed:
                red = 0
            elif pixel_value_r >= maxRed:
                red = 255
            else:
                red = int((pixel_value_r - minRed) / (maxRed - minRed) * 255)

            pixel_value_g = img.getpixel((i, j))[1]
            if pixel_value_g <= minGreen:
                green = 0
            elif pixel_value_g >= maxGreen:
                green = 255
            else:
                green = int((pixel_value_g - minGreen) / (maxGreen - minGreen) * 255)

            pixel_value_b = img.getpixel((i, j))[2]
            if pixel_value_b <= minBlue:
                blue = 0
            elif pixel_value_b >= maxBlue:
                blue = 255
            else:
                blue = int((pixel_value_b - minBlue) / (maxBlue - minBlue) * 255)
            img.putpixel([i, j], (red, green, blue))
    # img.show()
    return img


if __name__ == '__main__':
    img = Image.open("./threshold/123.jpg")
    img.show()
    thresHold(img)
    img.show()
