import pandas as pd
import numpy as np

data = pd.read_csv("u.user.csv")
data
cols = ["User_id", "Age", "Gender", "Occupation", "Zipcode"]
data = pd.read_csv("u.user.csv", sep="|", names=cols)
print(data)
data.info()
data.head()
data.tail()
