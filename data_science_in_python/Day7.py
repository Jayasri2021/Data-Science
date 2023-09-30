import numpy as np
import pandas as pd

cols = ["user_id", "age", "gender", "occupation", "zipcode"]
dt = pd.read_csv("./Downloads/u.user", sep="|", names=cols)
print(dt.head(10))
grp_gen = dt.groupby("gender").count()
print(grp_gen)
AV = pd.read_csv("./Downloads/city-of-chicago-salaries.csv")
print(AV)
data = AV.groupby("Department").count()
print(data)
dep_sal = AV.groupby("Department")["Employee Annual Salary"].count()
print(dep_sal)
plant_data = pd.read_csv("./Downloads/PlantGrowth.csv")
print(plant_data)

pv = plant_data.pivot(index="observation", columns="group", values="weight")
pv
