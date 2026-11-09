import pandas as pd

df = pd.read_csv('final_student_dataset.csv')

print(df.head())
print(df.info())
print(df.shape)
print(df.describe())