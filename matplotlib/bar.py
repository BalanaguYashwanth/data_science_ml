import numpy as np
import matplotlib.pyplot as plt

x = [5,8,10]
x1 = [12,16,2]

y = [6,9,11]
y1 = [6,15,7]

plt.bar(x,y, align='center')
plt.bar(x1,y1, color='g',align='center')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()