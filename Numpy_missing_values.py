
import numpy as np
import pandas as pd

##Read csv with delimiter
data = pd.read_csv("adult.csv",delimiter=",")
data

## Replacing NaN 
df = data.replace(" ?",np.NaN)
df

## Take the columns which were replaced by NaN
df.columns[df.isna().any()].tolist()

##groupby and find Ratio
df.groupby(['native-country','Salary'])[["native-country"]].get_group((' United-States',' <=50K')).count()/df.groupby(['native-country','Salary'])[["native-country"]].get_group((' United-States',' >50K')).count()



## groupby cars by cylinders. What is the average horsepower for 4 and 6 cylinders vehicles
df.horsepower = df.horsepower.astype(float)
df.groupby('cylinders').mean()
