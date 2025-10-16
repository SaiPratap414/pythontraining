import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
arr1 =np.array([[1,2,3],[4,5,6]])
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size )
print(arr1.dtype)
print(arr1.itemsize)
print(arr1.nbytes)
print(arr1[0,0])
print(arr1[1,2])

arr = np.zeros((3,3))
print(arr)
arr = np.ones((2,3))
print(arr)

arr = np.random.randint(1, 7, (2, 3))
print(arr)

arr = np.random.randint(1,3, size=(2,5))
print(arr)