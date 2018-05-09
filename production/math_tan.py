import math
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 100)
kk = []
for i in range(5, 85, 5):
    k = math.tan(i * math.pi / 180)
    kk.append(k)

plt.figure()
plt.plot(x, kk[0] * x, x, kk[1] * x, x, kk[2] * x, x, kk[3] * x, x, kk[4] * x, x, kk[5] * x, x, kk[6] * x, x, kk[7] * x,
         x, kk[8] * x, x, kk[9] * x, x, kk[10] * x, x, kk[11] * x, x, kk[12] * x, x, kk[13] * x, x, kk[14] * x, x, kk[15] * x)
plt.ylim(-10,10)
plt.show()