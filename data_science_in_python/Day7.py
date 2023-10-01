import numpy as np
import pandas as pd

cols = ["user_id", "age", "gender", "occupation", "zipcode"]
dt = pd.read_csv("u.user", sep="|", names=cols)
print(dt.head(10))
grp_gen = dt.groupby("gender").count()
print(grp_gen)
AV = pd.read_csv("city-of-chicago-salaries.csv")
print(AV)
data = AV.groupby("Department").count()
print(data)
dep_sal = AV.groupby("Department")["Employee Annual Salary"].count()
print(dep_sal)
plant_data = pd.read_csv("PlantGrowth.csv")
print(plant_data)
pv = plant_data.pivot(index="observation", columns="group", values="weight")
print(pv)
pd1 = plant_data.pivot_table(index="group", values="weight")
print(pd1)
IPL = pd.read_csv("odi-batting.csv")
print(IPL)
x = IPL[IPL["Country"] == "India"]
y = x.groupby("Player")["Runs"].count()
print(y.head())
da = IPL[IPL["Country"] == "India"]
da.pivot_table(index="Player", values="Runs", aggfunc=np.sum).sort_values(
    by="Runs", ascending=False
).head(10)
x = IPL[IPL["Runs"] == 0]
y = x.groupby("Player")["Runs", "Country"].value_counts()
y.sort_values(ascending=False).head(10)
y = x.groupby("Player")["Runs", "Country"].value_counts()
x = IPL[(IPL["Country"] == "India") & (IPL["Player"] == "Sachin R Tendulkar")]
y = x.groupby("MatchDate")["Runs"].sum()
print(y.head(10))
IPL["date"] = pd.to_datetime(IPL["MatchDate"])
IPL["date"].head(IPL)["Year"] = IPL["date"].dt.year
IPL["Day"] = IPL["date"].dt.day
IPL["Month"] = IPL["date"].dt.month
IPL[["date", "Year", "Month", "Day"]].head()
IPL["Month_Name"] = IPL["date"].dt.strftime("%B")
IPL["Weekday"] = IPL["date"].dt.strftime("%a")
IPL[["date", "Year", "Month", "Month_Name", "Day", "Weekday"]].head()
x = IPL[(IPL["Country"] == "India") & (IPL["Player"] == "Sachin R Tendulkar")]
IPL = sachin = x.groupby("Year")["Runs"].sum()
print(IPL)
