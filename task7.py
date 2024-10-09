import numpy as np


x = np.linspace(0, 10, 101)
print(x)

sinx = np.sin(x)

cosx = np.cos(x)

np.save('task7_sin.npy', sinx)

np.save('task7_cos.npy', cosx)