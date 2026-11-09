import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('penjualan_nusantaramart - penjualan_nusantaramart.csv')
print('data checking')
print(df.head())
print(df.info())
print(df.describe)

print('data sorting')
rata_kategori = df.groupby('kategori_produk')['total'].mean()
print(rata_kategori.sort_values(ascending=False))

print('data visualize')
total_kategori = df.groupby('kategori_produk')['total'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=total_kategori.values, y=total_kategori.index, palette='Blues_r')
plt.title('Total penjualn per kategori produk')
plt.xlabel('total penjualan(RP)')
plt.ylabel('Kategori produk')
plt.tight_layout()
plt.show()
