import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

a = np.array([3.41, 4.68, 5.88, 6.03, 6.7, 7.38, 7.56, 7.86, 7.66, 7.64, 7.15, 5.77, 5.62, 4.82, 3.88, 3.71, 2.4, 1.75, 1.72, 1.55, 1.78, 1.97, 2.79, 3.41])
b = np.array([7.84, 8.02, 7.86, 7.93, 8.37, 8.48, 8.39, 7.29, 6.17, 6.02, 4.71, 4.17, 4.14, 3.98, 4.13, 4.14, 4.57, 5.9, 6.11, 7.39, 8.29, 8.43, 8.29, 7.84])

x = np.arange(len(a))
x_new = np.arange(0, len(a), 0.1)

splx = CubicSpline(x, a)
sply = CubicSpline(x, b)

x_splx = splx(x_new)
y_sply = sply(x_new)
plt.plot(x_splx,y_sply,color=(0,0,0))
plt.fill(x_splx, y_sply, color=(0.9, 0.6, 0.2))
plt.show()





