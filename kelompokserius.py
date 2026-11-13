import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Atur gaya visualisasi
sns.set_style('whitegrid')

# Memuat dataset
df = pd.read_csv('final_student_dataset.csv')

print("=== 1. EKSPLORASI & PEMBERSIHAN DATA ===")
print("Jumlah Data Kosong   :", df.isnull().sum().sum())
print("Jumlah Data Duplikat :", df.duplicated().sum())
print("\nRingkasan Statistik Kolom Utama:")
print(df[['final_score_pct', 'gpa_score_avg', 'study_hours_per_week', 'attendance_rate']].describe())

print("\n=== 2. ANALISIS 5 STATISTIK DESKRIPTIF KUNCI ===")
total_students = len(df)
avg_final_score = df['final_score_pct'].mean()
avg_study_hours = df['study_hours_per_week'].mean()
at_risk_pct = (df['at_risk'].sum() / total_students) * 100
most_common_band = df['needs_help_band'].mode()[0]
print(f"Total siswa: {total_students}")
print(f"average final score: {avg_final_score}")
print(f"average study hours: {avg_study_hours}")
print(f"at risk: {at_risk_pct}")
print(f"most comman band: {most_common_band}")

# Grafik 1: Bar Plot (Rata-rata Nilai Akhir per Kategori Bantuan)
avg_band = df.groupby('needs_help_band')['final_score_pct'].mean().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(data=avg_band, x='needs_help_band', y='final_score_pct', palette='viridis')
plt.title('Rata-rata Nilai Akhir Berdasarkan Kategori Bantuan')
plt.xlabel('Kategori Bantuan (needs_help_band)')
plt.ylabel('Rata-rata Nilai Akhir (%)')
plt.show()

# Grafik 2: Line Plot (Jam Belajar vs Rata-rata GPA)
df_sample = df.sample(1000, random_state=42).sort_values('study_hours_per_week')
plt.figure(figsize=(8, 5))
sns.lineplot(data=df_sample, x='study_hours_per_week', y='gpa_score_avg', color='#2ecc71')
plt.title('Hubungan Tren Jam Belajar per Minggu terhadap Rata-rata GPA')
plt.xlabel('Jam Belajar per Minggu')
plt.ylabel('Rata-rata GPA')
plt.show()

# Grafik 3: Scatter Plot (Kehadiran vs Nilai Akhir dipisah Status At-Risk)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df.sample(2000, random_state=42), x='attendance_rate', y='final_score_pct', hue='at_risk', alpha=0.6, palette='coolwarm')
plt.title('Sebaran Tingkat Kehadiran vs Nilai Akhir Siswa')
plt.xlabel('Tingkat Kehadiran (%)')
plt.ylabel('Nilai Akhir (%)')
plt.legend(title='Status At-Risk')
plt.show()

# Grafik 4: Histogram (Distribusi Jam Belajar)
plt.figure(figsize=(8, 5))
sns.histplot(df['study_hours_per_week'], bins=20, kde=True, color='#3498db')
plt.title('Distribusi Jam Belajar Siswa per Minggu')
plt.xlabel('Jam Belajar per Minggu')
plt.ylabel('Jumlah Siswa')
plt.show()

# Grafik 5: Boxplot (Deteksi Outlier Ketidakaktifan LMS)
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['longest_inactivity_gap_days'], color='#e74c3c')
plt.title('Deteksi Outlier Jarak Hari Ketidakaktifan Terlama di LMS')
plt.xlabel('Jarak Hari Tidak Aktif (Hari)')
plt.show()

print("\n=== 4. ANALISIS DETEKSI OUTLIER (METODE IQR) ===")
Q1 = df['longest_inactivity_gap_days'].quantile(0.25)
Q3 = df['longest_inactivity_gap_days'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR

outliers = df[df['longest_inactivity_gap_days'] > upper_bound]
print(f"Kuartil 1 (Q1)             : {Q1} hari")
print(f"Kuartil 3 (Q3)             : {Q3} hari")
print(f"Interquartile Range (IQR)  : {IQR} hari")
print(f"Batas Atas Outlier         : {upper_bound} hari")
print(f"Jumlah Outlier Terdeteksi  : {len(outliers)} siswa")

print("\n=== 5. DASHBOARD RINGKAS (4 SUBPLOT) ===")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1: Bar Plot
sns.barplot(data=avg_band, x='needs_help_band', y='final_score_pct', ax=axes[0, 0], palette='viridis')
axes[0, 0].set_title('Rata-rata Nilai per Kategori Bantuan')
axes[0, 0].set_xlabel('Kategori Bantuan')
axes[0, 0].set_ylabel('Nilai Akhir (%)')

# Subplot 2: Histogram
sns.histplot(df['study_hours_per_week'], bins=20, kde=True, ax=axes[0, 1], color='#3498db')
axes[0, 1].set_title('Distribusi Jam Belajar per Minggu')
axes[0, 1].set_xlabel('Jam Belajar (Jam)')
axes[0, 1].set_ylabel('Jumlah Siswa')

# Subplot 3: Scatter Plot
sns.scatterplot(data=df.sample(2000, random_state=42), x='attendance_rate', y='final_score_pct', hue='at_risk', ax=axes[1, 0], alpha=0.6, palette='coolwarm')
axes[1, 0].set_title('Kehadiran vs Nilai Akhir Siswa')
axes[1, 0].set_xlabel('Kehadiran (%)')
axes[1, 0].set_ylabel('Nilai Akhir (%)')

# Subplot 4: Boxplot Outlier
sns.boxplot(x=df['longest_inactivity_gap_days'], ax=axes[1, 1], color='#e74c3c')
axes[1, 1].set_title('Outlier Hari Tidak Aktif di LMS')
axes[1, 1].set_xlabel('Jarak Hari Tidak Aktif (Hari)')

plt.tight_layout()
plt.show()