import pandas as pd
import numpy as np

data = pd.read_csv("./Downloads/u.user")
data
cols = ["User_id", "Age", "Gender", "Occupation", "Zipcode"]
data = pd.read_csv("./Downloads/u.user", sep="|", names=cols)
print(data)
data.info()
