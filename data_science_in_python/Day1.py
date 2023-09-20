import numpy as np

print(np.__version__)
# O dimensional array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
a = np.array(10)
print(a)
print(a.ndim)
# 1 dimensional array
b = np.array([1, 2, 3])
print(b)
print(b.ndim)
# 2 dimensional array
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a)
print(a.ndim)
print(a.shape)
# 3 dimensional array
a = np.array(
    [
        [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
        [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
    ]
)
print(a)
print(a.ndim)
print(a.shape)
# higher dimensional array
a = np.array(12, ndmin=2)
print(a)
print(a.ndim)
# indexing
a = np.array([1, 2, 3])
print(a)
print(a[2])
print(a[1] + a[2])
# 2D indexing
b = np.array([[1, 2], [3, 4]])
print(b)
print(b[1][0])
print(b[0][1])
print(b[0][0])
# 3D indexing
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c)
print(c[0][1][1])
print(c[1][0][1])
# slicing
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a)
print(a[2:8])
print(a[2:8:3])
# 2D slicing
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print(b[2, 0:1])
print(b[2, :])
print(b[:, 2])
print(b[2, 0:2])
