import numpy as np
import matplotlib.pyplot as plt

sinx = np.load('/home/pi/ee347/lab-4-advanced-python-group-10/task7_sin.npy')
cosx = np.load('/home/pi/ee347/lab-4-advanced-python-group-10/task7_cos.npy')

x = np.linspace(0, 10, 101)

plt.plot(x, sinx, label='sin(x)')

plt.plot(x, cosx, label='cos(x)')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')

plt.show()