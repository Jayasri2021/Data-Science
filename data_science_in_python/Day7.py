import numpy as np
import pandas as pd

cols = ["user_id", "age", "gender", "occupation", "zipcode"]
dt = pd.read_csv("./Downloads/u.user", sep="|", names=cols)
print(dt.head(10))
grp_gen = dt.groupby("gender").count()
grp_gen
AV = pd.read_csv("./Downloads/city-of-chicago-salaries.csv")
AV
