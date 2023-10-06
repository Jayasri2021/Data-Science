import numpy as np
import pandas as pd

dt = pd.read_csv("./u.user.csv")
cols = ["User_id", "Age", "Gender", "Occupation", "Zipcode"]
dt = pd.read_csv("u.user.csv", sep="|", names=cols)
print(dt)
print(dt.info())
print(dt.describe)  # numerics
print(dt["Gender"])
print(dt.nunique())
print(dt["Gender"].value_counts())
print(dt[(dt["Age"] > 30) & (dt["Gender"] == "F")])
print(dt[(dt["Age"] > 30) & (dt["Gender"] == "M")])
print(dt.loc[100:110])
print(dt.iloc[100:110])
print(dt.loc[100:110, "Gender"])
print(dt.iloc[100:110, 3])
print(dt.iloc[100:110, 0:3])

# Converters

data = pd.read_csv("./city-of-chicago-salaries.csv")
print(data)
print(data.info())
print(data.describe)
print(data.head())
print(data.tail())
print(data.nunique())
print(data["Department"].value_counts())
print(data["Department"].unique())  # shows only the fields and not the count
# remove the dollar symbols
data = pd.read_csv(
    "./city-of-chicago-salaries.csv",
    converters={"Employee Annual Salary": lambda x: float(x.replace("$", " "))},
)
print(data)
data = pd.read_csv(
    "./city-of-chicago-salaries.csv",
    converters={"Department": lambda x: (x.replace("POLICE", "TRAINER"))},
)
print(data)
# Plots
from matplotlib import pyplot as plt

data["Department"].value_counts().head().plot(kind="bar")
dt = pd.read_csv("./u.user.csv")
cols = ["User_id", "Age", "Gender", "Occupation", "Zipcode"]
dt = pd.read_csv("./u.user.col", sep="|", names=cols)
dt["Gender"].value_counts().head().plot(kind="bar")
