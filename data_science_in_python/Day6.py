import numpy as np
import pandas as pd

x = pd.DataFrame({"key": range(0, 5), "leftval": [10, 20, 30, 40, 50]})
print(x)
y = pd.DataFrame({"key": range(2, 7), "rightval": [60, 70, 80, 90, 100]})
print(y)
z = pd.merge(x, y)
print(z)
z = pd.merge(x, y, how="inner")
print(z)
z1 = pd.merge(x, y, how="left")
print(z1)
z2 = pd.merge(x, y, how="right")
print(z2)
z3 = pd.merge(x, y, how="outer")
print(z3)
x3 = pd.DataFrame({"s_no": [1, 2, 3, 4], "value1": [20, 30, 40, 50]})
print(x3)
