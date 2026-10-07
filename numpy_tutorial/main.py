import numpy as np

def sin_cos_tan_angles():
    angle = np.array([45,90,135])
    sin_angle = np.sin(angle)
    cos_angle = np.cos(angle)
    tan_angle = np.tan(angle)
    print('sin angle: ',sin_angle)
    print('cos angle: ',cos_angle)
    print('tan angle: ',tan_angle)

def basic_operation():
    arr = np.array([(1,2,3),(4,5,6)])
    print('arr type: ',arr.dtype)
    print('arr ndim: ',arr.ndim)






def tutorial():
    # arr = np.array([[1,2,3]]) #ndmin
    # print(arr.ndim)

    # arr = np.array([
    #     [
    #         [1,2,3], [4,5,6],
    #         [7,8,9], [10,11,12]
    #     ],
    #     [
    #         [1,2,3], [4,5,6],
    #         [7,8,9], [10,11,12]
    #     ]
    #     ])
    # print(arr)
    # A1 = np.arange(5)
    # A2 = np.arange(5,10)
    
    # print(A1+A2)

    A3 = np.array([[1,2,3], [4,5,6]])
    print(A3[1, 1:])

tutorial()

