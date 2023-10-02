Exploratory data analysis¶
Descriptive Statistics¶
In [48]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
In [50]:
am=pd.read_csv("./Downloads/automobile.csv")
am.head()
Out[50]:
symboling	normalized-losses	make	aspiration	num-of-doors	body-style	drive-wheels	engine-location	wheel-base	length	...	compression-ratio	horsepower	peak-rpm	city-mpg	highway-mpg	price	city-L/100km	horsepower-binned	diesel	gas
0	3	122	alfa-romero	std	two	convertible	rwd	front	88.6	0.811148	...	9.0	111.0	5000.0	21	27	13495.0	11.190476	Medium	0	1
1	3	122	alfa-romero	std	two	convertible	rwd	front	88.6	0.811148	...	9.0	111.0	5000.0	21	27	16500.0	11.190476	Medium	0	1
2	1	122	alfa-romero	std	two	hatchback	rwd	front	94.5	0.822681	...	9.0	154.0	5000.0	19	26	16500.0	12.368421	Medium	0	1
3	2	164	audi	std	four	sedan	fwd	front	99.8	0.848630	...	10.0	102.0	5500.0	24	30	13950.0	9.791667	Medium	0	1
4	2	164	audi	std	four	sedan	4wd	front	99.4	0.848630	...	8.0	115.0	5500.0	18	22	17450.0	13.055556	Medium	0	1
5 rows Ã 29 columns

In [39]:
am.columns
Out[39]:
Index(['symboling', 'normalized-losses', 'make', 'aspiration', 'num-of-doors',
       'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length',
       'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders',
       'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio',
       'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price',
       'city-L/100km', 'horsepower-binned', 'diesel', 'gas'],
      dtype='object')
In [40]:
am.shape
Out[40]:
(201, 29)
In [41]:
am.describe()
Out[41]:
symboling	normalized-losses	wheel-base	length	width	height	curb-weight	engine-size	bore	stroke	compression-ratio	horsepower	peak-rpm	city-mpg	highway-mpg	price	city-L/100km	diesel	gas
count	201.000000	201.00000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000	197.000000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000
mean	0.840796	122.00000	98.797015	0.837102	0.915126	53.766667	2555.666667	126.875622	3.330692	3.256904	10.164279	103.405534	5117.665368	25.179104	30.686567	13207.129353	9.944145	0.099502	0.900498
std	1.254802	31.99625	6.066366	0.059213	0.029187	2.447822	517.296727	41.546834	0.268072	0.319256	4.004965	37.365700	478.113805	6.423220	6.815150	7947.066342	2.534599	0.300083	0.300083
min	-2.000000	65.00000	86.600000	0.678039	0.837500	47.800000	1488.000000	61.000000	2.540000	2.070000	7.000000	48.000000	4150.000000	13.000000	16.000000	5118.000000	4.795918	0.000000	0.000000
25%	0.000000	101.00000	94.500000	0.801538	0.890278	52.000000	2169.000000	98.000000	3.150000	3.110000	8.600000	70.000000	4800.000000	19.000000	25.000000	7775.000000	7.833333	0.000000	1.000000
50%	1.000000	122.00000	97.000000	0.832292	0.909722	54.100000	2414.000000	120.000000	3.310000	3.290000	9.000000	95.000000	5125.369458	24.000000	30.000000	10295.000000	9.791667	0.000000	1.000000
75%	2.000000	137.00000	102.400000	0.881788	0.925000	55.500000	2926.000000	141.000000	3.580000	3.410000	9.400000	116.000000	5500.000000	30.000000	34.000000	16500.000000	12.368421	0.000000	1.000000
max	3.000000	256.00000	120.900000	1.000000	1.000000	59.800000	4066.000000	326.000000	3.940000	4.170000	23.000000	262.000000	6600.000000	49.000000	54.000000	45400.000000	18.076923	1.000000	1.000000
In [42]:
am["num-of-doors"].value_counts()
Out[42]:
four    115
two      86
Name: num-of-doors, dtype: int64
Box Plot¶
In [43]:
sns.boxplot(x="num-of-cylinders",y="price",data=am)
Out[43]:
<Axes: xlabel='num-of-cylinders', ylabel='price'>

Scatter Plots¶
In [51]:
am["engine-size"].unique()
Out[51]:
array([130, 152, 109, 136, 131, 108, 164, 209,  61,  90,  98, 122, 156,
        92,  79, 110, 111, 119, 258, 326,  91,  70,  80, 140, 134, 183,
       234, 308, 304,  97, 103, 120, 181, 151, 194, 132, 121, 146, 171,
       161, 141, 173, 145], dtype=int64)
In [52]:
plt.scatter(am["engine-size"],am["price"])
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.show()

Histogram¶
In [57]:
count,bin_edges=np.histogram(am["peak-rpm"])
am["peak-rpm"].plot(kind="hist",xticks=bin_edges)
plt.xlabel("value pf peak-rpm")
plt.ylabel("number of cars")
plt.show()

Grouping of data¶
In [61]:
auto_temp=am[["num-of-doors","body-style","price"]]
auto_group=auto_temp.groupby(["num-of-doors","body-style"],as_index=False).mean()
auto_group
Out[61]:
num-of-doors	body-style	price
0	four	hatchback	8372.000000
1	four	sedan	14490.687500
2	four	wagon	12371.960000
3	two	convertible	21890.500000
4	two	hardtop	22208.500000
5	two	hatchback	10230.793103
6	two	sedan	14283.000000
In [62]:
auto_pivot=auto_group.pivot(index="body-style",columns="num-of-doors")
auto_pivot
Out[62]:
price
num-of-doors	four	two
body-style		
convertible	NaN	21890.500000
hardtop	NaN	22208.500000
hatchback	8372.0000	10230.793103
sedan	14490.6875	14283.000000
wagon	12371.9600	NaN
In [67]:
pg=pd.read_csv("./Downloads/automobile.csv")
pg
Out[67]:
symboling	normalized-losses	make	aspiration	num-of-doors	body-style	drive-wheels	engine-location	wheel-base	length	...	compression-ratio	horsepower	peak-rpm	city-mpg	highway-mpg	price	city-L/100km	horsepower-binned	diesel	gas
0	3	122	alfa-romero	std	two	convertible	rwd	front	88.6	0.811148	...	9.0	111.0	5000.0	21	27	13495.0	11.190476	Medium	0	1
1	3	122	alfa-romero	std	two	convertible	rwd	front	88.6	0.811148	...	9.0	111.0	5000.0	21	27	16500.0	11.190476	Medium	0	1
2	1	122	alfa-romero	std	two	hatchback	rwd	front	94.5	0.822681	...	9.0	154.0	5000.0	19	26	16500.0	12.368421	Medium	0	1
3	2	164	audi	std	four	sedan	fwd	front	99.8	0.848630	...	10.0	102.0	5500.0	24	30	13950.0	9.791667	Medium	0	1
4	2	164	audi	std	four	sedan	4wd	front	99.4	0.848630	...	8.0	115.0	5500.0	18	22	17450.0	13.055556	Medium	0	1
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
196	-1	95	volvo	std	four	sedan	rwd	front	109.1	0.907256	...	9.5	114.0	5400.0	23	28	16845.0	10.217391	Medium	0	1
197	-1	95	volvo	turbo	four	sedan	rwd	front	109.1	0.907256	...	8.7	160.0	5300.0	19	25	19045.0	12.368421	High	0	1
198	-1	95	volvo	std	four	sedan	rwd	front	109.1	0.907256	...	8.8	134.0	5500.0	18	23	21485.0	13.055556	Medium	0	1
199	-1	95	volvo	turbo	four	sedan	rwd	front	109.1	0.907256	...	23.0	106.0	4800.0	26	27	22470.0	9.038462	Medium	1	0
200	-1	95	volvo	turbo	four	sedan	rwd	front	109.1	0.907256	...	9.5	114.0	5400.0	19	25	22625.0	12.368421	Medium	0	1
201 rows Ã 29 columns

In [68]:
pg.describe()
Out[68]:
symboling	normalized-losses	wheel-base	length	width	height	curb-weight	engine-size	bore	stroke	compression-ratio	horsepower	peak-rpm	city-mpg	highway-mpg	price	city-L/100km	diesel	gas
count	201.000000	201.00000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000	197.000000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000	201.000000
mean	0.840796	122.00000	98.797015	0.837102	0.915126	53.766667	2555.666667	126.875622	3.330692	3.256904	10.164279	103.405534	5117.665368	25.179104	30.686567	13207.129353	9.944145	0.099502	0.900498
std	1.254802	31.99625	6.066366	0.059213	0.029187	2.447822	517.296727	41.546834	0.268072	0.319256	4.004965	37.365700	478.113805	6.423220	6.815150	7947.066342	2.534599	0.300083	0.300083
min	-2.000000	65.00000	86.600000	0.678039	0.837500	47.800000	1488.000000	61.000000	2.540000	2.070000	7.000000	48.000000	4150.000000	13.000000	16.000000	5118.000000	4.795918	0.000000	0.000000
25%	0.000000	101.00000	94.500000	0.801538	0.890278	52.000000	2169.000000	98.000000	3.150000	3.110000	8.600000	70.000000	4800.000000	19.000000	25.000000	7775.000000	7.833333	0.000000	1.000000
50%	1.000000	122.00000	97.000000	0.832292	0.909722	54.100000	2414.000000	120.000000	3.310000	3.290000	9.000000	95.000000	5125.369458	24.000000	30.000000	10295.000000	9.791667	0.000000	1.000000
75%	2.000000	137.00000	102.400000	0.881788	0.925000	55.500000	2926.000000	141.000000	3.580000	3.410000	9.400000	116.000000	5500.000000	30.000000	34.000000	16500.000000	12.368421	0.000000	1.000000
max	3.000000	256.00000	120.900000	1.000000	1.000000	59.800000	4066.000000	326.000000	3.940000	4.170000	23.000000	262.000000	6600.000000	49.000000	54.000000	45400.000000	18.076923	1.000000	1.000000
In [69]:
pg.shape
Out[69]:
(201, 29)
In [70]:
pg.nunique()
Out[70]:
symboling              6
normalized-losses     51
make                  22
aspiration             2
num-of-doors           2
body-style             5
drive-wheels           3
engine-location        2
wheel-base            52
length                73
width                 43
height                49
curb-weight          169
engine-type            6
num-of-cylinders       7
engine-size           43
fuel-system            8
bore                  39
stroke                36
compression-ratio     32
horsepower            59
peak-rpm              23
city-mpg              29
highway-mpg           30
price                186
city-L/100km          29
horsepower-binned      3
diesel                 2
gas                    2
dtype: int64
In [71]:
from matplotlib import pyplot as plt
In [72]:
pg["stroke"].value_counts().head().plot(kind="bar")
Out[72]:
<Axes: >

In [73]:
import seaborn as sns
In [74]:
sns.boxplot(x="body-style",y="price",data=pg)
Out[74]:
<Axes: xlabel='body-style', ylabel='price'>

Handling missing values¶
In [75]:
sns.catplot(x="body-style",y="price",hue="engine-type",data=pg)
Out[75]:
<seaborn.axisgrid.FacetGrid at 0x24adae1d9f0>

In [76]:
sns.violinplot(x="engine-type",y="price",hue="num-of-doors",data=pg)
Out[76]:
<Axes: xlabel='engine-type', ylabel='price'>

Handling missing values¶
In [77]:
pg.isna().sum()
Out[77]:
symboling            0
normalized-losses    0
make                 0
aspiration           0
num-of-doors         0
body-style           0
drive-wheels         0
engine-location      0
wheel-base           0
length               0
width                0
height               0
curb-weight          0
engine-type          0
num-of-cylinders     0
engine-size          0
fuel-system          0
bore                 0
stroke               4
compression-ratio    0
horsepower           0
peak-rpm             0
city-mpg             0
highway-mpg          0
price                0
city-L/100km         0
horsepower-binned    1
diesel               0
gas                  0
dtype: int64
In [78]:
sns.heatmap(pg.isnull())
Out[78]:
<Axes: >

In [79]:
pg["stroke"].dtype
Out[79]:
dtype('float64')
In [80]:
pg["horsepower-binned"].dtype
Out[80]:
dtype('O')
In [82]:
mn=pg["stroke"].mean()
mn
Out[82]:
3.256903553299492
In [84]:
pg["stroke"].fillna(mn,inplace=True)
In [85]:
pg["horsepower-binned"].value_counts()
Out[85]:
Low       115
Medium     62
High       23
Name: horsepower-binned, dtype: int64
In [86]:
pg["horsepower-binned"].fillna("Low",inplace=True)
In [89]:
sns.heatmap(pg.isnull())
Out[89]:
<Axes: >

In [90]:
pg.isna().sum()
Out[90]:
symboling            0
normalized-losses    0
make                 0
aspiration           0
num-of-doors         0
body-style           0
drive-wheels         0
engine-location      0
wheel-base           0
length               0
width                0
height               0
curb-weight          0
engine-type          0
num-of-cylinders     0
engine-size          0
fuel-system          0
bore                 0
stroke               0
compression-ratio    0
horsepower           0
peak-rpm             0
city-mpg             0
highway-mpg          0
price                0
city-L/100km         0
horsepower-binned    0
diesel               0
gas                  0
dtype: int64