import pandas as pd

df = pd.read_csv('final_student_dataset.csv')

# Menghitung nilai statistik per kolom
print(df['final_score_pct'].mean())         # Rata-rata
print(df['final_score_pct'].median())       # Median
print(df['final_score_pct'].std())          # Standar deviasi
print(df['final_score_pct'].quantile(0.25)) # Q1 (Kuartil 1)
print(df['final_score_pct'].quantile(0.75)) # Q3 (Kuartil 3)

# Ringkasan statistik statistik untuk SELURUH kolom numerik dataset:
print(df.describe())