#coding=utf-8
#此文档记录opencv2处理图像

#读取并显示图像
import cv2
img_cv = cv2.imread("./data/cool.jpg")
print(img_cv.shape)
#output: (667, 1000, 3)
print(img_cv.shape[0],"0000000")

for x in range(img_cv.shape[0]):
    for y in range(img_cv.shape[1]):
        img_cv[x, y, :] = [255, 255, 255]
    pass
cv2.imshow("abc",img_cv)
cv2.waitKey(0)

img_cv = cv2.line(img_cv,(0, 0), (998, 665),(255, 0, 0),3)     #画一条线宽度为3个像素
cv2.imshow("abc",img_cv)
cv2.waitKey(0)
'''
 总结： opencv打开的图片显示shape信息是(高，长，通道)
 对像素点进行操作时是向右x为正方向，向下为y的正方向
'''
#
# from PIL import Image
# img_pil = Image.open("./data/cool.jpg")
# print(img_pil.size)
# # output:(1000, 667)
# img_array = img_pil.load()
# for i in range(100):
#     img_pil.putpixel([i,i*2],(255, 0, 0))
# img_pil.show()
'''
pillow打开图片时size显示(长，高)，对像素点进行操作时向右x为正方向，向下为y的正方向
'''
