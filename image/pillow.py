# coding = utf-8
# 安装pillow包，安装过程参考OpenCV包的安装
#
# import os
# import sys
# from PIL import Image
from PIL import ImageDraw
#
#
#导入Image模块，并利用其中的open函数打开一张图片：
from PIL import Image
im = Image.open("./data/cool.jpg")

"""
Image.open() 打开的图像下标从0，开始。
"""

# 如果打开成功，返回一个Image对象，可以通过对象属性检查文件内容：
# print(im.format, im.size, im.mode)
# format属性定义了图像的格式，如果图像不是从文件打开的，那么该属性值为None；
# size属性是一个tuple，表示图像的宽和高（单位为像素）；
# mode属性为表示图像的模式，常用的模式为：L为灰度图，RGB为真彩色，CMYK为pre-press图像。

w, h = im.size
print(w, h)
# 显示图片
# im.show()


# 转换图片格式
# 将图片转换成png格式
# from PIL import Image
# import os
# import sys
#
# for infile in sys.argv[1:]:  # 从传入的第一个参数开始一直到最后
#     f, e = os.path.splitext(infile)  # 拆分文件名和扩展名，以最后一个点为分界
#     outfile = f + ".png"
#     if infile != outfile:
#         try:
#             Image.open(infile).save(outfile)
#         except IOError:
#             print("Cannot convert", infile)
#             pass
#         pass
#     pass


# 创建缩略图
# from PIL import Image
# import os
# import glob
# size  = (128, 128)
# for infile in glob.glob("./ipiut2/*.tif"):
#     f, ext = os.path.splitext(infile)
#     print("111")
#     img = Image.open(infile)
#     img.thumbnail(size, Image.ANTIALIAS)
#     img.save(f + ".thumbnail"+".tif")
# 上段代码对当前文件下的jpg图像文件全部创建缩略图，并保存，
# glob模块是一种智能化的文件名匹配技术，在批图像处理中经常会用到。
# 注意：Pillow库不会直接解码或者加载图像栅格数据。
# 当你打开一个文件，只会读取文件头信息用来确定格式，颜色模式，大小等等，文件的剩余部分不会主动处理。
# 这意味着打开一个图像文件的操作十分快速，跟图片大小和压缩方式无关。


# 图像的剪切、粘贴与合并操作
# im = Image.open("7.jpg")
# box = (100, 100, 300, 300)
# region = im.crop(box)
# region.show()
# 矩形选区有一个4元素定义，分别表示左上角，右下角的坐标。
# 这个库以左上角为坐标原点，单位是px，所以上述代码复制了一个 200×200 pixels 的矩形选区。
# 这个区域是从下标的100，开始，到299结束。共299 - 100 + 1 = 200个像素

# 粘贴
# 从上面剪切出来的图片可以粘贴回原图像中（这里添加一个旋转操作）
# region = region.transpose(Image.ROTATE_180)
# im.paste(region, box)
# im.show()


# 分离和合并颜色通道
# im = Image.open("7.jpg")
# r, g, b = im.split()   #分离各个通道
# im = Image.merge("RGB", (r, g, b))      #合并各个通道


# 几何变换
# im = Image.open("7.jpg")
# out1 = im.resize((256, 128))   #改变图像大小，参数为一个元组，新图像的（宽，高）
# out1.show()
# out2 = im.rotate(45)    #对图像进行旋转，参数为顺时针的旋转角度。
# out2.show()
# 在Pillow中，对于一些常见的旋转作了专门的定义：
# out = im.transpose(Image.FLIP_LEFT_RIGHT)  #左右镜像旋转
# out = im.transpose(Image.FLIP_TOP_BOTTOM)  #上下镜像旋转
# out = im.transpose(Image.ROTATE_90)   #顺时针旋转90度
# out = im.transpose(Image.ROTATE_180)  #顺时针旋转180度
# out = im.transpose(Image.ROTATE_270)  #顺时针旋转270度


# 颜色空间变换
# cmyk = im.convert("CMYK")
# gray = im.convert("L")

# 返回(x,y)处的像素值
# im.getpixel((x,y))


# 图像增强
# Filter    ImageFilter模块包含很多预定义的增强filters，通过filter()方法使用
# from PIL import ImageFilter
# out = im.filter(ImageFilter.DETAIL)
# out.show()


# 画一个多边形
# from PIL import ImageDraw
# ImageDraw.Draw(im) --返回一个绘图对象，使以后的绘图操作发生在im上
# Draw对象方法(draw=ImageDraw.Draw(im)):
# draw.polygon(xy,fill=None,outline=None) --画一个多边形
# 注:无特殊说明，参数box类型默认为[x,y,x,y]或[(x,y),(x,y)];xy参数类型默认为[x,y,x,y,x,y...]或者[(x,y),(x,y),(x,y),...]

# img = Image.open("X:\jet_python\study\study_python\image\data\cool.jpg")
# draw = ImageDraw.Draw(img)
# draw.polygon([(3,5),(60,80),(80,100),(6, 50)],fill=(255,0,0))
# img.show()
