---

# SOLO (Sortir & Olah Limbah Online)

Dashboard interaktif berbasis **Streamlit** untuk melakukan analisis dataset gambar sampah, visualisasi distribusi data, serta menjawab pertanyaan bisnis pada *project* klasifikasi sampah.

---

## Deskripsi Project

Project ini dibuat sebagai bagian dari **Capstone Project Data Science** yang berfokus pada analisis dataset gambar sampah untuk mendukung pengembangan sistem klasifikasi sampah berbasis *Artificial Intelligence* (AI).

Dashboard ini digunakan untuk:

* Analisis distribusi dataset
* Visualisasi gambar dataset
* Mengetahui keseimbangan dataset
* Menjawab pertanyaan bisnis
* Menampilkan *insight* data secara interaktif

Kategori sampah yang dianalisis:

* Organik
* Anorganik
* B3

---

## Tujuan Project

Tujuan utama *project* ini adalah:

1. Menganalisis apakah dataset sudah cukup seimbang untuk proses *training* model AI.
2. Mengetahui kategori sampah yang paling dominan pada dataset.
3. Membuat dashboard interaktif untuk visualisasi data klasifikasi sampah.
4. Membantu proses monitoring dataset sebelum digunakan pada model *Machine Learning* / *Deep Learning*.

---

## Pertanyaan Bisnis

Dashboard ini dibuat untuk menjawab beberapa pertanyaan bisnis:

### 1️. Apakah dataset gambar sampah sudah cukup berkualitas dan seimbang?

Analisis dilakukan dengan:

* Menghitung jumlah data setiap kategori
* Membandingkan distribusi dataset
* Melihat selisih jumlah data antar kategori

### 2️. Kategori sampah apa yang paling sering muncul?

Analisis dilakukan dengan:

* Menghitung total dataset per kategori
* Visualisasi kategori dominan
* Menentukan kategori dengan jumlah data terbanyak

---

## Analisis Data Tabular (Lokasi Bank Sampah)

Berdasarkan analisis data sampah yang telah dilakukan, ada beberapa kesimpulan:

1. **Kecamatan Penyumbang Sampah Terbesar:** Kecamatan **Cilandak** teridentifikasi sebagai penyumbang berat sampah tertinggi, diikuti oleh Pasar Minggu dan Cengkareng. Hal ini menunjukkan perlunya fokus dan strategi pengelolaan sampah yang lebih intensif di wilayah-wilayah tersebut.
2. **Jenis Sampah Dominan dan Pengelolaan:** Sampah **organik** adalah jenis sampah yang paling dominan dalam dataset. Untuk mengelola sampah organik secara efektif, metode seperti pengomposan atau produksi biogas sangat direkomendasikan. Selain itu, proporsi sampah anorganik seperti kertas dan plastik yang signifikan menekankan pentingnya program daur ulang yang terstruktur dan edukasi masyarakat mengenai pemilahan sampah di sumbernya.
3. **Pengaruh Cuaca:** Analisis menunjukkan bahwa kondisi cuaca (cerah, hujan, mendung) memiliki **pengaruh yang tidak signifikan** terhadap jumlah berat sampah yang dihasilkan. Fluktuasi berat sampah cenderung stabil terlepas dari kondisi cuaca, menunjukkan bahwa faktor lain mungkin lebih berpengaruh terhadap volume sampah harian.

Secara keseluruhan, temuan ini memberikan dasar bagi pemerintah daerah dan pemangku kepentingan lainnya untuk merancang kebijakan dan program pengelolaan sampah yang lebih tepat sasaran, dengan memprioritaskan area dan jenis sampah tertentu, serta mengoptimalkan strategi berdasarkan karakteristik data yang ada.

---

## Kesimpulan Akhir: Dataset Klasifikasi Gambar

Proses penyiapan dataset untuk model *Convolutional Neural Network* (CNN) telah berhasil dilakukan dengan hasil sebagai berikut:

1. **Integritas & Kualitas Data:** Seluruh citra telah melewati proses normalisasi dan standarisasi ukuran. Penghapusan duplikasi dan penanganan *missing values* pada direktori penyimpanan memastikan bahwa model AI akan belajar dari pola visual yang bersih, unik, dan tidak bias.
2. **Keseimbangan & Representasi Kelas:** Dengan pembagian dataset yang distratifikasi (*stratified split*), setiap subset (train, validation, test) kini memiliki representasi proporsional dari ketiga kategori utama (Organik, Anorganik, B3). Hal ini krusial untuk mencegah model mengalami *overfitting* pada kelas mayoritas dan memastikan akurasi yang konsisten di semua jenis sampah.
3. **Kesiapan Infrastruktur Pelatihan:** Struktur folder yang terorganisir dengan baik—berdasarkan pembagian subset dan label kategori—memungkinkan integrasi langsung dengan *data generator* pada *framework* Deep Learning (seperti TensorFlow/Keras atau PyTorch). Dataset ini sekarang berada dalam kondisi optimal, siap untuk dieksekusi dalam tahap pelatihan (*training phase*) guna menghasilkan model klasifikasi sampah yang presisi dan andal.

---

## Struktur Dataset

Dataset disusun dengan format berikut:

Dataset_Final_Cleaned/
│
├── content/
│   └── Dataset_Final_Cleaned/
│       ├── train/
│       │   ├── Anorganik/
│       │   ├── B3/
│       │   └── Organik/
│       │
│       ├── validation/
│       │   ├── Anorganik/
│       │   ├── B3/
│       │   └── Organik/
│       │
│       └── test/
│           ├── Anorganik/
│           ├── B3/
│           └── Organik/
│
├── venv/
├── app.py
├── Dataset_Sampah_Cleaned_2018_2025.csv
└── Project_capstone_baru.ipynb
---

## Fitur Dashboard

* **Home:** Deskripsi project, informasi dashboard, total dataset, dan jumlah kategori.
* **Dataset Overview:** Tabel dataset, grafik distribusi, dan *pie chart* persentase kategori.
* **Visualisasi Gambar:** Menampilkan contoh gambar dari setiap kategori (Organik, Anorganik, B3).
* **Business Insight:** Hasil analisis bisnis, keseimbangan dataset, dan *metric analysis*.

---

## Library yang Digunakan

| Library | Fungsi |
| --- | --- |
| Streamlit | Framework dashboard |
| Pandas | Pengolahan data |
| Plotly | Visualisasi interaktif |
| Pillow | Membaca gambar |
| Matplotlib | Visualisasi data |
| Seaborn | Visualisasi statistik |
| Scikit-learn | Utility data science |

---

## Cara Menjalankan Project

1. **Clone Repository:** `git clone https://github.com/username/repository.git`
2. **Masuk ke Folder:** `cd repository`
3. **Install Requirements:** `pip install -r requirements.txt`
4. **Jalankan Streamlit:** `streamlit run app.py`

---

## Author

**Data Science Capstone Team**
