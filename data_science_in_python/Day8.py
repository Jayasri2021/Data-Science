# Exploratory data analysis¶
# Descriptive Statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

am = pd.read_csv("automobile.csv")
print(am.head())
print(am.columns)
print(am.shape)
print(am.describe())
print(am["num-of-doors"].value_counts())
sns.boxplot(x="num-of-cylinders", y="price", data=am)

# Scatter Plots
am["engine-size"].unique()
plt.scatter(am["engine-size"], am["price"])
plt.xlabel("Engine Size")
plt.ylabel("Price")
print(plt.show())

# Histogram
count, bin_edges = np.histogram(am["peak-rpm"])
am["peak-rpm"].plot(kind="hist", xticks=bin_edges)
plt.xlabel("value pf peak-rpm")
plt.ylabel("number of cars")
plt.show()

auto_temp = am[["num-of-doors", "body-style", "price"]]
auto_group = auto_temp.groupby(["num-of-doors", "body-style"], as_index=False).mean()
auto_group

auto_pivot = auto_group.pivot(index="body-style", columns="num-of-doors")
auto_pivot

pg = pd.read_csv("automobile.csv")
print(pg)

print(pg.describe())

print(pg.shape)

print(pg.nunique())
