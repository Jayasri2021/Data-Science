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
