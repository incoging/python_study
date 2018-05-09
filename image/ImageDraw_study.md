##### ImageDraw 几何图形绘制
* line(xy, fill=None, width=0)：直线的绘制，第一个参数指定的是直线的端点坐标，
形式为（x0, y0, x1, y1），第二个参数指定直线的颜色；

* rectangle(xy, fill=None, outline=None)：矩形绘制，第一个参数指定矩形的对角线顶点（左上和右下），
形式为（x0, y0, x1, y1），第二个指定填充颜色，第三个参数指定边界颜色；

* arc( xy, start, end, fill=None)：（椭）圆弧的绘制，第一个参数指定弧所在椭圆的外切矩形，
第二、三两个参数分别是弧的起始和终止角度，第四个参数是填充颜色，第五个参数是线条颜色；

* chord(xy, start, end, fill=None, outline=None): 弦的绘制，和弧类似，只是将弧的起始和终止点通过直线连接起来；

* pieslice(self, xy, start, end, fill=None, outline=None): 圆饼图的绘制，和弧与弦类似，
只是分别将起始和终止点与所在（椭）圆中心相连；

* ellipse(self, xy, fill=None, outline=None): 椭圆的绘制，第一个参数指定椭圆的外切矩形， 
第二、三两个参数分别指定填充颜色和线条颜色，当外切矩形是正方形时，椭圆即为圆；

* polygon(self, xy, fill=None, outline=None): 绘制多边形，第一个参数为多边形的端点，
形式为（x0, y0, x1, y1, x2, y2,……），第二、三两个参数分别指定填充颜色和线条颜色；

* text(self, xy, text, fill=None, font=None, anchor=None, *args, **kwargs): 文字的绘制，
第一个参数指定绘制的起始点（文本的左上角所在位置），第二个参数指定文本内容，第三个参数指定文本的颜色，
第四个参数指定字体（通过ImageFont类来定义）。

```
import numpy as np  
from PIL import Image  
from PIL import ImageDraw  
from PIL import ImageFont  
  
  
def draw_test():  
  
    #生成深蓝色绘图画布  
    array = np.ndarray((480, 640, 3), np.uint8)  
  
    array[:, :, 0] = 0  
    array[:, :, 1] = 0  
    array[:, :, 2] = 100  
  
    image = Image.fromarray(array)  
  
    #创建绘制对象  
    draw = ImageDraw.Draw(image)  
      
    #绘制直线  
    draw.line((20, 20, 150, 150), 'cyan')  
  
    #绘制矩形  
    draw.rectangle((100, 200, 300, 400), 'black', 'red')  
  
    #绘制弧  
    draw.arc((100, 200, 300, 400), 0, 180, 'yellow')  
    draw.arc((100, 200, 300, 400), -90, 0, 'green')  
  
    #绘制弦  
    draw.chord((350, 50, 500, 200), 0, 120, 'khaki', 'orange')  
  
    #绘制圆饼图  
    draw.pieslice((350, 50, 500, 200), -150, -30, 'pink', 'crimson')  
      
    #绘制椭圆  
    draw.ellipse((350, 300, 500, 400), 'yellowgreen', 'wheat')  
    #外切矩形为正方形时椭圆即为圆  
    draw.ellipse((550, 50, 600, 100), 'seagreen', 'skyblue')   
  
    #绘制多边形  
    draw.polygon((150, 180, 200, 180, 250, 120, 230, 90, 130, 100), 'olive', 'hotpink')  
  
    #绘制文本  
    font = ImageFont.truetype("consola.ttf", 40, encoding="unic")#设置字体  
    draw.text((100, 50), u'Hello World', 'fuchsia', font)  
  
    image.show()  
```
> 补充python中所支持的颜色：   

>>颜色也可以使用"#"加上6位16进制字符串表示如“#ff0000”,则和“red”等价，前两位表示R通道的值，
中间两位表示G通道的值，最后两位表示B通道的值。