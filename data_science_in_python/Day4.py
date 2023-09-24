import numpy as np
import pandas as pd

dt = pd.read_csv("u.user.csv")
cols = ["User_id", "Age", "Gender", "Occupation", "Zipcode"]
dt = pd.read_csv("u.user.csv", sep="|", names=cols)
print(dt)
dt.info()
dt.describe  # numerics
dt["Gender"]
dt.nunique()
dt["Gender"].value_counts()
dt[(dt["Age"] > 30) & (dt["Gender"] == "F")]
dt[(dt["Age"] > 30) & (dt["Gender"] == "M")]
dt.loc[100:110]
dt.iloc[100:110]
dt.loc[100:110, "Gender"]
dt.iloc[100:110, 3]
dt.iloc[100:110, 0:3]

# Converters

data = pd.read_csv("city-of-chicago-salaries.csv")
data
data.info()
data.describe
data.head()
data.tail()
data.nunique()
data["Department"].value_counts()
data["Department"].unique()  # shows only the fields and not the count
# remove the dollar symbols
data = pd.read_csv(
    "city-of-chicago-salaries.csv",
    converters={"Employee Annual Salary": lambda x: float(x.replace("$", " "))},
)
data
