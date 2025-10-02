import pandas as pd
import os

# --- Konfigurasi dan Persiapan ---
NAMA_ANDA = "Nama Lengkap Anda"
DESKRIPSI_PROFIL = "Saya adalah seorang data enthusiast yang tertarik dengan web crawling, natural language processing, dan visualisasi data. Proyek ini adalah salah satu eksplorasi saya dalam mengumpulkan dan membersihkan data dari web."

# Pastikan folder output ada
os.makedirs('output', exist_ok=True)

# Muat data dari CSV
try:
    # Kita asumsikan file ini memiliki semua kolom yang dibutuhkan
    df = pd.read_csv('berita_final_bersih.csv') 
except FileNotFoundError:
    print("Pastikan file 'berita_final_bersih.csv' ada di folder yang sama.")
    exit()

# Template HTML dasar dengan Bootstrap dan navigasi
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style> 
        body {{ padding: 2rem; }} 
        .project-card {{ margin-bottom: 1.5rem; }}
    </style>
</head>
<body>
    <div class="container">
        <nav class="mb-4">
            <a href="index.html" class="btn btn-dark">🏠 Kembali ke Halaman Utama</a>
        </nav>
        <h1 class="mb-4">{title}</h1>
        {content}
    </div>
</body>
</html>
"""

# --- 1. Membuat Halaman Utama (index.html) ---
print("Membuat halaman utama (index.html)...")
halaman_utama_content = f"""
<div class="card mb-4">
    <div class="card-body text-center">
        <h2 class="card-title">{NAMA_ANDA}</h2>
        <p class="card-text">{DESKRIPSI_PROFIL}</p>
    </div>
</div>

<h3 class="mt-5 border-bottom pb-2 mb-3">Daftar Proyek</h3>

<div class="card project-card">
    <div class="card-header">
        <strong>Proyek 1: Crawling & Preprocessing Berita Detik.com</strong>
    </div>
    <div class="card-body">
        <p>Proyek ini mencakup pengambilan data berita dari portal Detik.com dan pembersihan data teks menggunakan teknik NLP.</p>
        <a href="berita_crawl.html" class="btn btn-outline-primary">Lihat Data Crawling Mentah</a>
        <a href="berita_preprocessing.html" class="btn btn-outline-success">Lihat Hasil Preprocessing</a>
    </div>
</div>

<div class="card project-card">
    <div class="card-header">
        <strong>Proyek 2: Crawling Web Lain (Segera Hadir)</strong>
    </div>
    <div class="card-body">
        <p>Deskripsi singkat tentang proyek crawling kedua Anda akan muncul di sini.</p>
        <a href="#" class="btn btn-outline-primary disabled">Lihat Data Crawling Mentah</a>
        <a href="#" class="btn btn-outline-success disabled">Lihat Hasil Preprocessing</a>
    </div>
</div>
"""

# Menghapus navigasi "Kembali" khusus untuk halaman utama
halaman_utama_html = html_template.replace('<nav class="mb-4"> ... </nav>', '', 1).format(
    title="Portofolio Proyek Data", content=halaman_utama_content
).replace('<a href="index.html" class="btn btn-dark">🏠 Kembali ke Halaman Utama</a>', '')


with open('output/index.html', 'w', encoding='utf-8') as f:
    f.write(halaman_utama_html)

# --- 2. Membuat Halaman Data Crawling Mentah (berita_crawl.html) ---
print("Membuat halaman data mentah (berita_crawl.html)...")
df_crawl = df[['id', 'Judul Berita', 'Kategori Berita']]
tabel_crawl_html = df_crawl.to_html(classes='table table-bordered table-striped', index=False, justify='left')
halaman_crawl_html = html_template.format(title="Hasil Crawling Berita Mentah", content=tabel_crawl_html)

with open('output/berita_crawl.html', 'w', encoding='utf-8') as f:
    f.write(halaman_crawl_html)

# --- 3. Membuat Halaman Data Preprocessing (berita_preprocessing.html) ---
print("Membuat halaman data preprocessing (berita_preprocessing.html)...")
# Memilih kolom asli dan hasil akhirnya untuk perbandingan
df_preprocessing = df[['Judul Berita', 'text_cleaned']]
df_preprocessing.rename(columns={'text_cleaned': 'Judul Hasil Preprocessing (Stemmed)'}, inplace=True)
tabel_preprocessing_html = df_preprocessing.to_html(classes='table table-bordered table-striped', index=False, justify='left')
halaman_preprocessing_html = html_template.format(title="Hasil Preprocessing Teks Berita", content=tabel_preprocessing_html)

with open('output/berita_preprocessing.html', 'w', encoding='utf-8') as f:
    f.write(halaman_preprocessing_html)

print("\nWebsite statis dengan struktur baru berhasil dibuat di dalam folder 'output'!")