import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

am = pd.read_csv("automobile.csv")
print(am)
auto_temp1 = am[["make", "price"]]
group1 = auto_temp1.groupby(["make"]).mean().sort_values(ascending=False, by="price")
print(group1)
group1.plot.bar()
temp_df = am[["make", "price"]].groupby(["make"])
temp_df.head()
stats.f_oneway(temp_df.get_group("audi")["price"], temp_df.get_group("volvo")["price"])
stats.f_oneway(
    temp_df.get_group("jaguar")["price"], temp_df.get_group("honda")["price"]
)
auto = pd.read_csv("automobile.csv")
auto.head()
