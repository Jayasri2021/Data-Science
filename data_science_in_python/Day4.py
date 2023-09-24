import numpy as np
import pandas as pd

dt = pd.read_csv("./Downloads/u.user")
cols = ["User_id", "Age", "Gender", "Occupation", "Zipcode"]
dt = pd.read_csv("./Downloads/u.user", sep="|", names=cols)
print(dt)
dt.info()
dt.describe  # numerics
dt["Gender"]
dt.nunique()
dt["Gender"].value_counts()
dt[(dt["Age"] > 30) & (dt["Gender"] == "F")]
