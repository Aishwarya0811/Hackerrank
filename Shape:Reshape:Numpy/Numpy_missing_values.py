
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
df.groupby(['native-country', 'Salary']).get_group((' United-States', 'Salary <=50K'))/df.groupby(['native-country', 'Salary']).get_group((' United-States', 'Salary >50K'))
