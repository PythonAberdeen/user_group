import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3, 1, figsize=(5, 10))

x = np.arange(-2.0, 2.0, 0.01)
y = x ** 2
ax[0].plot(x, y)
ax[0].set_title(r'y = $x^2$')

x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
y = np.sin(x)
ax[1].plot(x, y)
ax[1].set_title(r'y = $\sin(x)$')

x = np.arange(0.0, 10.0, 0.01)
y = np.exp(-x / 8) * np.cos(x)
ax[2].plot(x, y)
ax[2].set_title(r'y = $e^{\frac{-x}{8}}\cos(x)$')
plt.show()
