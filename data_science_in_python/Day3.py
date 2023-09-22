import pandas as pd

print(pd.__version__)
# Series
list = [1, 2, 3, 4, 5]
print(list)
print(type(list))

ser = pd.Series(list)
print(ser)
print(type(ser))
print(ser[3])
print(ser[1:4])
ser_1 = pd.Series(list, index=["A", "B", "C", "D", "E"])
print(ser_1)
print(ser_1["C"])
print(ser_1["A"])
# DICTIONARY
dt = {"General-Knowledge": 98, "English": 89, "Maths": 85, "Science": 96, "Social": 98}
print(dt)
ser_2 = pd.Series(dt)
print(ser_2)
ser_3 = pd.Series(dt, index=["Maths", "Science", "Social"])
print(ser_3)
