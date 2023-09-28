import numpy as np
import pandas as pd

x = pd.DataFrame({"key": range(0, 5), "leftval": [10, 20, 30, 40, 50]})
print(x)
y = pd.DataFrame({"key": range(2, 7), "rightval": [60, 70, 80, 90, 100]})
print(y)
z = pd.merge(x, y)
print(z)
z = pd.merge(x, y, how="inner")
print(z)
z1 = pd.merge(x, y, how="left")
print(z1)
z2 = pd.merge(x, y, how="right")
print(z2)
z3 = pd.merge(x, y, how="outer")
print(z3)
x3 = pd.DataFrame({"s_no": [1, 2, 3, 4], "value1": [20, 30, 40, 50]})
print(x3)
x4 = pd.DataFrame({"serial_no": [1, 2, 3, 4], "value2": [20, 30, 40, 50]})
print(x4)
x5 = pd.merge(x3, x4, left_on="s_no", right_on="serial_no", how="inner")
print(x5)
cols1 = ["movie_id", "movie_name", "release_data", "video_release_date", "imdb_url"]
movies = pd.read_csv(
    "u.item", sep="|", encoding="latin-1", names=cols1, usecols=range(5)
)
u_data = pd.read_csv(
    "u.data", sep="\t", names=["user_id", "movie_id", "ratings", "timestamp"]
)
movie_ratings = pd.merge(movies, u_data)
movie_ratings.head(5)
cols = ["user_id", "age", "gender", "occupation", "zip_code"]
users = pd.read_csv(".u.user", sep="|", names=cols)
users.head(5)
AV = pd.merge(movie_ratings, users)
AV.head()
data = AV[AV["user_id"] == 100]
print(data)
data.set_index("user_id", inplace=True)
data.head(10)
x1 = {"x": [21, 22, 23, 34, 25], "y": [31, 32, 33, 34, 35]}
print(x1)
x = pd.DataFrame(x1)
print(x)
y1 = {"a": [41, 42, 43, 44, 45], "b": [51, 52, 53, 54, 55]}
y = pd.DataFrame(y1)
print(y)
z = pd.concat([x, y])
print(z)
z = pd.concat([x, y], axis=1)
print(z)
