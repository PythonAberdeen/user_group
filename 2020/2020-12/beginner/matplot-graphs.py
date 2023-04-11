import math
import numpy as np
import matplotlib.pyplot as plt

def square(x):
    return x**2

def exp_dec(x):
    return math.e ** (x/-8) * math.cos(x)

x = []
for loop in np.arange(-2, 2.1, .1):
    x.append(loop)

y = [square(v) for v in x]

plt.figure()
plt.plot(x, y)
plt.title("Square")
# plt.y_lable("y")
plt.show()
