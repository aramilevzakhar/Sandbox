import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)



arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])




