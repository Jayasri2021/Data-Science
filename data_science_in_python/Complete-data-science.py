import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Reading and working with file: student.csv
std = pd.read_csv("./student.csv")
print(std)
std.info()
std.describe
std.shape
std.head()
std.head(10)
std.tail()
std.tail(10)
std.loc[10:30]
std.iloc[10:30]
std.loc[10:30, "mark"]
std.iloc[10:15, 1]
std.nunique()
std["gender"].count()
std["class"].value_counts()
std[std["mark"].isna()] = 20
print(std)
std.isna().sum()
std[(std["mark"] > 85) & (std["gender"] == "female")].value_counts()
# Plot
std["gender"].value_counts().plot(kind="bar")
std["class"].value_counts().plot(kind="pie")
# Indexing
std.set_index("mark", inplace=True)
print(std)
std.reset_index(inplace=True)
print(std)
# Minimum and Maximum
min(std["mark"])
max(std["mark"])
# DataFrames
std1 = std[std["mark"] == 88]
print(std1)
# Groupby:
std2 = std.groupby("id")["class"].count()
print(std2)
# Pivot
std3 = std.pivot(index="id", columns="class", values="mark")
print(std3)
# Box Plot
sns.boxplot(x="mark", y="id", data=std)
# Scatter Plot
plt.scatter(std["id"], std["mark"])
plt.xlabel("mark")
plt.ylabel("id")
plt.show()
# Histogam
count, bin_edges = np.histogram(std["mark"])
std["mark"].plot(kind="hist", xticks=bin_edges)
plt.xlabel("mark")
plt.ylabel("id")
plt.show()
# Grouping of data:
std_temp = std[["name", "class", "mark"]]
std_group = std_temp.groupby(["name", "mark"], as_index=False).mean()
std_group
std_pivot = std_group.pivot(index="name", columns="mark")
std_pivot
# Catplot:
sns.catplot(x="id", y="mark", hue="class", data=std)
# Violin plot
sns.violinplot(x="id", y="mark", hue="class", data=std)
# Handling missing values
std.isna().sum()
sns.heatmap(std.isnull())
std["mark"].dtype
std1 = std["mark"].mean()
print(std1)
std["mark"].value_counts()
std["mark"].fillna("88", inplace=True)
# Correlation
std_temp = std[["mark", "name"]]
std_group = std_temp.groupby(["mark"]).mean().sort_values(ascending=False, by="mark")
print(std_group)
std.plot.bar()
temp = std[["mark", "class"]].groupby(["mark"])
temp.head()
correlation_matrix = std.corr()
plt.subplots(figsize=(20, 15))
sns.heatmap(correlation_matrix, annot=True)
plt.show()
sns.regplot(x="id", y="mark", data=std)
sns.regplot(x="index", y="mark", data=std)
