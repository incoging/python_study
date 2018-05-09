#coding = utf-8
#2017年8月17日22:15:14

#更改图片具体位置的像素值
from PIL import Image
import random

x = 136
y = 76

c = Image.new("RGB", (x, y))

for i in range(0, x):
    for j in range(0, y):
        c.putpixel([i, j], (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

c.show()
c.save("c.png")