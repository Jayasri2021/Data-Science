import pandas as pd

print(pd.__version__)
# Series
list = [1, 2, 3, 4, 5]
print(list)
print(type(list))

ser = pd.Series(list)
print(ser)
print(type(ser))
