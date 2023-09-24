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
import pandas as pd

data = pd.read_csv("./Downloads/city-of-chicago-salaries.csv")
data
data.info()
