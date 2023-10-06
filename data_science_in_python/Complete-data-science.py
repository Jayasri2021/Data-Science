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
