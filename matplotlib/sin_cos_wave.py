import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi, 0.1)
plt.subplot(2,1,2)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.title("Sine")
plt.plot(x,y_sin)

plt.subplot(2,1,1)
plt.title("consine")
plt.plot(x,y_cos)

plt.show()