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
# Data Frames
import pandas as pd

dt = {"Elakiya": [34, 67, 89, 45], "vivi": [56, 87, 74, 67]}
print(dt)
df = pd.DataFrame(dt)
print(dt)
print(type(df))
print(df.loc[2])
df1 = pd.DataFrame(dt, index=["Tamil", "English", "Maths", "Science"])
print(df1)
print(df1.loc["Maths"])
df1.loc["Maths", "Elakiya"]
Data = pd.read_csv("./Downloads/DS CSV FILE.csv")
print(Data)
print(Data.info())
print(Data.describe)
print(Data.shape)
print(Data.head())
print(Data.head(10))
print(Data.tail())
print(Data.tail(20))
print(Data.loc[100:110])
print(Data.iloc[100:110])
print(Data.loc[100:105, "Calories"])
print(Data.iloc[100:105, 1])
