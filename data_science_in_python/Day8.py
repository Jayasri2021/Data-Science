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
