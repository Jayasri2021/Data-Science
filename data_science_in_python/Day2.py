import numpy as np

# Copy() Vs View()
a = np.array([1, 2, 3, 4, 5])
print(a)
a = np.array([1, 2, 3, 4, 5])
print(a)
b = a.copy()  # copies the value from one array to another
print(b)
a[0] = 12
print(a)
print(b)
a = np.array([1, 2, 3, 4, 5])
print(a)
b = a.view()  # share the memory address
print(b)
a[0] = 12
print(a)
print(b)
# Shape of an array
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 5, 3]])
print(a)
print(a.shape)  # shape - no.of rows and columns in a given array
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[2, 4], [6, 8]]])
print(b)
print(b.shape)
# Reshape of an array
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a)
print(a.reshape(2, 4))
print(a.reshape(2, 2, 2))
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 7, 9]])
print(b)
print(b.shape)
print(b.reshape(-1))
print(b.reshape(3, 2, 2))
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c)
print(c.shape)
print(b.reshape(-1))
# Number Sorting
a = np.array([2, 1, 3, 5, 7, 8, 4, 6, 10, 9])
print(a)
print(np.sort(a))
b = np.array([[3, 2, 1], [6, 5, 4], [8, 7, 9]])
print(b)
print(np.sort(b))
# Reverse of an Array
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a)
print(np.sort(a))
print(np.sort(a)[::-1])
