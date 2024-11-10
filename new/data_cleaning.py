import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import MinMaxScaler, StandardScaler

file_path = r"C:\Users\arpit\Desktop\Book1.csv"
df = pd.read_csv(file_path)

print("Initial DataFrame: ")
print(df.head())

# replace NaN with mean for numerical columns
df.fillna(df.mean(numeric_only=True), inplace=True)

# drop duplicate rows
df.drop_duplicates(inplace=True)

# drop rows with missing values in specific columns
miss = ['age', 'weight']
df.dropna(subset=miss, inplace=True)

# replace Nan with Unknown
column_fill = ['category']
df[column_fill] = df[column_fill].fillna('Unknown')

df['age'] = df['age'].astype(int)
df['weight'] = df['weight'].astype(int)
df['visit_count'] = df['visit_count'].astype(int)
df['value'] = df['value'].astype(int)
df['registration_date'] = pd.to_datetime(df['registration_date'])

print(df)