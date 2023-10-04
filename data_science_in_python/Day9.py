import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

am = pd.read_csv("./Downloads/automobile.csv")
print(am)
auto_temp1 = am[["make", "price"]]
group1 = auto_temp1.groupby(["make"]).mean().sort_values(ascending=False, by="price")
print(group1)
group1.plot.bar()
