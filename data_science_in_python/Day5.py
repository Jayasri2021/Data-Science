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
AV.dtypes
AV.head()
AV.tail()
AV.nunique()
AV["Player"].value_counts()
AV["Player"].unique()
AV[AV["Runs"] > 22]
AV.loc[100:110, "Country":"URL"]
AV.iloc[100:110, 3]
AV["MatchDate"].value_counts()
min(AV["MatchDate"])
max(AV["MatchDate"])
AV["MatchDate"].min()
AV["MatchDate"].max()
AV["Country"].nunique()
AV["Player"].nunique()
import matplotlib.pyplot as plt

AV["ScoreRate"].value_counts().head(10).plot(kind="pie")
AV["ScoreRate"].value_counts().head(10).plot(kind="hist")
AV["ScoreRate"].value_counts().head(10).plot(kind="line")
AV[(AV["Country"] == "India") & (AV["Player"] == "Sachin R Tendulkar")].shape
AV[
    (AV["Country"] == "India") & (AV["Player"] == "Sachin R Tendulkar")
].value_counts().head()
AV[(AV["Player"] == "Sachin R Tendulkar") & (AV["Runs"] >= 100)]
AV.isna().sum()
