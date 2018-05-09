import numpy as np
import cv2

# Create a black image
img=np.zeros((600,600,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(240,18),(360,18),(255,0,0),1)

#draw rectangle
# cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#draw circle
cv2.circle(img,(300,300), 288, (0,0,255))

#draw ellipse
cv2.ellipse(img,(300,19),(60,6),0,0,360,255,1)


# cv2.imshow('opencv',img)
# cv2.waitKey(0)
# cv2.imwrite("./the_pic3.bmp",img)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
# cv2.waitKey(1)
# cv2.waitKey(1)
# cv2.waitKey(1)

import numpy as np
import math

the_x = np.linspace(-60, 60, 120)

y1 = [math.sqrt(82944 - math.pow(x, 2)) for x in the_x]

a = 60
b = 5.4
y2 = [math.sqrt((b**2 * (a**2 - x**2) / a**2)) + 281.68 for x in the_x]

y1 = np.asarray(y1)
y2 = np.asarray(y2)
diff = y2 - y1
the_max = np.max(diff)
the_min = np.min(diff)
print(diff)
print("max:", the_max)
print("min:", the_min)
