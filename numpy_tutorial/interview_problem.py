#Differnce between fast of numpy array vs python list
import numpy as np
import sys
import time

def vanilla_python_list_operation():
    s = range(1000)
    return (sys.getsizeof(s) * len(s))

def numpy_array_operation():
    np.array([1,2,3])
    s = np.arange(1000)
    return (s.size*s.itemsize)

def difference():
    start_time = time.time()
    vanilla_python_list_operation()
    end_time = time.time()
    print('vanilla python list operation: ', (end_time-start_time)*1000)

    start_time = time.time()
    numpy_array_operation()
    end_time = time.time()
    print('numpy array operation: ', (end_time - start_time)*1000)


if __name__ == "__main__":
    difference()
