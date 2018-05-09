### chapter 1 读入，显示，存储图片
##### 读入图片：
 opencv打开的图片显示shape信息是(高，长，通道)
对像素点进行操作时是向右为x正方向，向下为y的正方向
读入后的图片为 BRG 排列，而不是像PIL为RGB
```
img = imread(filename, flags=None)
```
* flags:<br/>
  cv2.IMREAD_COLOR：读入一副彩色图像。图像的透明度会被忽略，这是默认参数。<br/>
  cv2.IMREAD_GRAYSCALE：以灰度模式读入图像（也可以直接写 0）<br/>
  cv2.IMREAD_UNCHANGED：读入一幅图像，并且包括图像的alpha 通道

> Notice: 就算图像的路径是错的，OpenCV 也不会提醒你的，但是当你使用命
令print img时得到的结果是None。

##### 显示图片
```
cv2.imshow(winname, mat)
```
* winname -- 窗口名字
* mat -- 要显示的图片矩阵

实例：
```
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
> 解释：<br/>
cv2.waitKey() 是一个键盘绑定函数。需要指出的是它的时间尺度是毫
秒级。函数等待特定的几毫秒，看是否有键盘输入。特定的几毫秒之内，如果
按下任意键，这个函数会返回按键的ASCII 码值，程序将会继续运行。如果没
有键盘输入，返回值为-1，如果我们设置这个函数的参数为0，那它将会无限
期的等待键盘输入。<br/>
cv2.destroyAllWindows() 可以轻易删除任何我们建立的窗口。如果
你想删除特定的窗口可以使用cv2.destroyWindow()，在括号内输入你想删
除的窗口名。

也可以先创建一个窗口，再加载图像：<br/>
> 这种情况下， 你可以决定窗口是否可以调整
大小。使用到的函数是cv2.namedWindow()。初始设定函数
标签是cv2.WINDOW_AUTOSIZE。但是如果你把标签改成
cv2.WINDOW_NORMAL，你就可以调整窗口大小了。当图像维度太大，
或者要添加轨迹条时，调整窗口大小将会很有用

实例：
```
import numpy as np
import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

##### 保存图像
```
imwrite(filename, img, params=None)
```
* filename -- 文件名
* img -- 要保存的文件

### chapter 2 绘制几何图形
##### 画线
```
cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
```
* img -- 要画线的图片
* pt1 -- 线段的起始点 (6, 8)
* pt2 -- 线段的终止点 (18, 32)
* color -- 以RGB 为例，需要传入一个元组，例如：（255,0,0）代表蓝色。对于灰度图只需要传入灰度值。
* thickness -- 线条的粗细。如果给一个闭合图形设置为-1，那么这个图形就会被填充。默认值是1.
* lineType -- 线条的类型，8 连接，抗锯齿等。默认情况是8 连接。cv2.LINE_AA为抗锯齿，
这样看起来会非常平滑。
* shift Number of fractional bits in the point coordinates.


##### 矩形
```
cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
```
* pt1 -- 矩形左上角的坐标 (36,32)
* pt2 -- 矩形右下角的坐标 (60,80)


##### 圆
```
circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
```
* center -- 中心点坐标  (23, 26)
* radius  -- 半径大小 30

##### 椭圆
```
ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=None, lineType=None, shift=None)
```
* center -- 椭圆的中心(256,256)
* axes -- 长轴和短轴的长度(100,50)
* angle -- 椭圆沿逆时针方向旋转的角度
* startAngle, endAngle --  椭圆弧沿顺时针方向起始的角度和结束角度，如果是0 很360，就是整个椭圆。

##### 多边形




















