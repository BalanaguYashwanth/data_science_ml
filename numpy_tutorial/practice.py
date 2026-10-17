import numpy as np
arr = np.array([[1,2,3], [4,5,6]])
print('\n ndim:',arr.ndim)

arr = np.array([
        [2,3,4], [6,7,8]
    ])
print('\n slicing row & column',arr[1,1:])


linearr = np.linspace(1, 2, 30)
print(linearr)

A1 = np.arange(1,21)
A2 = np.arange(20,40)
print(A1+A2)
# np.min
# np.max
# np.sum