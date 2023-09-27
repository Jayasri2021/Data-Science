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
data.nunique()
data["Gender"].value_counts()
data.dtypes
data.head()
data.set_index("User_id", inplace=True)
data.head()
data.reset_index(inplace=True)
data.head()
AV = pd.read_csv("./Downloads/odi-batting.csv")
AV
AV.info()
AV.describe()
# In[ 24 ] to be entered
