Tugas Analisis 1: Basic Data Checking & Summary
Kategori Produk dengan Rata-rata Nilai Transaksi (Total) Tertinggi:
Kategori Elektronik memiliki rata-rata nilai transaksi tertinggi, yaitu sekitar Rp 363.541,67 per transaksi (disusul ketat oleh Fashion sebesar Rp 353.900,00).

Pengecekan Missing Value dari Output df.info():
Tidak ada data kosong (seluruh kolom memiliki 220 data non-null dari total 220 baris).
Cara mengeceknya: Perhatikan kolom Non-Null Count. Jika jumlah non-null pada setiap kolom sama dengan total RangeIndex (220 entries), berarti tidak ada missing value.

Perbandingan Mean dan Median Kolom Total:

Mean (Rata-rata): Rp 238.486,36

Median (Nilai Tengah): Rp 125.000,00

Kesimpulan Sebaran Data: Nilai mean jauh lebih besar daripada median (
Mean>Median). Ini menunjukkan bahwa sebaran data total transaksi bersifat miring ke kanan (skewed to the right) akibat adanya beberapa transaksi bernilai sangat besar (outlier) yang menarik nilai rata-rata ke atas.

Tugas Analisis 2: Barplot & Rekomendasi Bisnis
Penyumbang Penjualan Tertinggi dan Terendah:

Penjualan Tertinggi: Kategori Fashion (Rp 17,695,000) dan Elektronik (Rp 17,450,000).

Penjualan Terendah: Kategori Makanan & Minuman (Rp 3,029,000).

Rekomendasi Bisnis untuk Manajer Nusantara Mart:

Fokus pada Top Performer: Jaga ketersediaan stok (inventory management) untuk kategori Fashion dan Elektronik karena keduanya merupakan penyumbang pendapatan terbesar.

Evaluasi Produk Makanan & Minuman: Lakukan variasi produk, promosi paket bundling, atau perbaiki strategi pemasaran untuk mendongkrak penjualan Makanan & Minuman yang masih jauh tertinggal.

Cross-Selling: Buat penawaran kombinasi, misalnya memberi diskon produk Makanan & Minuman setiap pembelian barang Fashion atau Elektronik.

Tugas Analisis 3: Line Plot Tren Bulanan
Bulan Penjualan Tertinggi & Kemungkinan Penyebabnya:

Bulan Tertinggi: Mei 2026 (mencapai Rp 13,585,000).

Kemungkinan Penyebab: Adanya lonjakan belanja musiman (seperti belanja persiapan Hari Raya/Gaji ke-13/promo tengah tahun Mid-Year Sale) yang mendorong konsumen berbelanja dalam jumlah besar.

Tren Penjualan Overall:
Tren penjualan bersifat fluktuatif dengan kecenderungan naik di awal hingga pertengahan tahun, lalu turun drastis pada bulan Juni (mengalami kenaikan konsisten dari Januari hingga Mei, lalu anjlok pada bulan Juni 2026).

Tugas Analisis 4: Scatter Plot Hubungan Jumlah & Total
Pola Hubungan Jumlah Barang dan Total Nilai Transaksi:
Terlihat hubungan positif. Semakin banyak jumlah barang yang dibeli, nilai total transaksinya cenderung makin besar.

Titik Data Outlier:
Ya, terdapat titik data outlier (titik yang berada jauh di sebelah kanan atas hingga mencapai jumlah 25–40 barang). Berdasarkan warna hue, titik outlier tersebut berasal dari kategori Elektronik, Olahraga, dan Kesehatan.

Tugas Analisis 5: Histplot & Boxplot
Bentuk Distribusi Rating Pelanggan:
Distribusi rating cenderung tinggi (skewed left). Mayoritas pelanggan memberikan nilai tinggi (skor 4 dan 5), sedangkan nilai rendah (skor 2 dan 3) frekuensinya sangat sedikit. Ini mengindikasikan kepuasan pelanggan secara umum sudah sangat baik.

Kategori Produk dengan Outlier pada Boxplot:
Kategori Elektronik, Olahraga, dan Kesehatan memiliki titik-titik di luar batas atas boxplot (outliers).

Kemungkinan Penyebab: Pembelian grosir oleh reseller, pembelian oleh instansi/perusahaan, atau adanya pesanan khusus dalam jumlah borongan yang jauh di atas rata-rata konsumsi perorangan.

Tugas Analisis 6: Subplots / Visualisasi Dashboard
Keuntungan Menyajikan Beberapa Grafik dalam Satu Dashboard:

Efisiensi & Pemahaman Menyeluruh (Holistik): Memudahkan pengambilan keputusan karena dapat melihat berbagai sudut pandang data (total omzet, tren waktu, distribusi rating, dan sebaran kuantitas) secara bersamaan tanpa perlu berpindah-pindah dokumen/layar.

Analisis Korelasi Lebih Mudah: Membantu mengaitkan hubungan antar variabel secara langsung (misalnya: menghubungkan lonjakan omzet di bulan tertentu dengan kategori produk penyumbang terbanyak).