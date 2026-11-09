import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('final_student_dataset.csv')

# Menghitung nilai statistik per kolom
print(df['final_score_pct'].mean())         # Rata-rata
print(df['final_score_pct'].median())       # Median
print(df['final_score_pct'].std())          # Standar deviasi
print(df['final_score_pct'].quantile(0.25)) # Q1 (Kuartil 1)
print(df['final_score_pct'].quantile(0.75)) # Q3 (Kuartil 3)

# Ringkasan statistik statistik untuk SELURUH kolom numerik dataset:
print(df.describe())


# 2. Atur gaya dan ukuran grafik
sns.set_style('whitegrid')
plt.figure(figsize=(8, 5))

# 3. Hitung rata-rata nilai akhir berdasarkan kategori bantuan
avg_score = df.groupby('needs_help_band')['final_score_pct'].mean().reset_index()

# 4. Perintah membuat bar plot
sns.barplot(data=avg_score, x='needs_help_band', y='final_score_pct', palette='viridis')

# 5. Label dan Judul
plt.title('Rata-rata Nilai Akhir Berdasarkan Kategori Bantuan')
plt.xlabel('Kategori Bantuan (needs_help_band)')
plt.ylabel('Rata-rata Nilai Akhir (%)')

# 6. Tampilkan grafik
plt.show()