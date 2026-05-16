# ♻️ Dashboard Klasifikasi Sampah

Dashboard interaktif berbasis **Streamlit** untuk melakukan analisis dataset gambar sampah, visualisasi distribusi data, serta menjawab pertanyaan bisnis pada project klasifikasi sampah.

---

# 📌 Deskripsi Project

Project ini dibuat sebagai bagian dari **Capstone Project Data Science** yang berfokus pada analisis dataset gambar sampah untuk mendukung pengembangan sistem klasifikasi sampah berbasis Artificial Intelligence (AI).

Dashboard ini digunakan untuk:

- Analisis distribusi dataset
- Visualisasi gambar dataset
- Mengetahui keseimbangan dataset
- Menjawab pertanyaan bisnis
- Menampilkan insight data secara interaktif

Kategori sampah yang dianalisis:

- 🟢 Organik
- 🔵 Anorganik
- 🔴 B3

---

# 🎯 Tujuan Project

Tujuan utama project ini adalah:

1. Menganalisis apakah dataset sudah cukup seimbang untuk proses training model AI.
2. Mengetahui kategori sampah yang paling dominan pada dataset.
3. Membuat dashboard interaktif untuk visualisasi data klasifikasi sampah.
4. Membantu proses monitoring dataset sebelum digunakan pada model Machine Learning / Deep Learning.

---

# 🧠 Pertanyaan Bisnis

Dashboard ini dibuat untuk menjawab beberapa pertanyaan bisnis:

### 1️⃣ Apakah dataset gambar sampah sudah cukup berkualitas dan seimbang?

Analisis dilakukan dengan:
- menghitung jumlah data setiap kategori
- membandingkan distribusi dataset
- melihat selisih jumlah data antar kategori

---

### 2️⃣ Kategori sampah apa yang paling sering muncul?

Analisis dilakukan dengan:
- menghitung total dataset per kategori
- visualisasi kategori dominan
- menentukan kategori dengan jumlah data terbanyak

---

# 🗂️ Struktur Dataset

Dataset disusun dengan format:

```bash
Dataset_Final_Cleaned/
│
├── train/
│   ├── Organik/
│   ├── Anorganik/
│   └── B3/
│
├── validation/
│   ├── Organik/
│   ├── Anorganik/
│   └── B3/
│
└── test/
    ├── Organik/
    ├── Anorganik/
    └── B3/
```

---

# 📊 Fitur Dashboard

## 🏠 Home
Menampilkan:
- deskripsi project
- informasi dashboard
- total dataset
- jumlah kategori

---

## 📊 Dataset Overview
Menampilkan:
- tabel dataset
- grafik distribusi dataset
- pie chart persentase kategori

Visualisasi:
- Bar Chart
- Pie Chart

---

## 🖼️ Visualisasi Gambar
Menampilkan contoh gambar dataset dari masing-masing kategori:
- Organik
- Anorganik
- B3

---

## 📈 Business Insight
Menampilkan hasil analisis bisnis:
- keseimbangan dataset
- kategori paling dominan
- insight distribusi data

Visualisasi:
- Balance Chart
- Funnel Chart
- Metric Analysis

---

# 🛠️ Library yang Digunakan

| Library | Fungsi |
|---|---|
| Streamlit | Framework dashboard |
| Pandas | Pengolahan data |
| Plotly | Visualisasi interaktif |
| Pillow | Membaca gambar |
| Matplotlib | Visualisasi data |
| Seaborn | Visualisasi statistik |
| Scikit-learn | Utility data science |

---

# 🚀 Cara Menjalankan Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/username/repository.git
```

---

## 2️⃣ Masuk ke Folder Project

```bash
cd repository
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Jalankan Streamlit

```bash
streamlit run app.py
```

---

# 📦 Requirements

```txt
streamlit
pandas
plotly
Pillow
matplotlib
seaborn
scikit-learn
```

---

# 📷 Tampilan Dashboard

Dashboard memiliki:
- Dark Mode UI
- Sidebar Navigation
- Interactive Charts
- Responsive Layout
- Dataset Preview

---

# 📈 Hasil Analisis

Berdasarkan hasil analisis:

✅ Dataset sudah melalui proses balancing  
✅ Distribusi data antar kategori lebih seimbang  
✅ Dataset siap digunakan untuk proses training model AI  
✅ Kategori dominan dapat diketahui melalui visualisasi dashboard  

---

# 👨‍💻 Teknologi yang Digunakan

- Python
- Streamlit
- Plotly
- Pandas
- Data Visualization

---

# 📚 Project Capstone

Project ini dibuat untuk kebutuhan:
- Capstone Project
- Data Science Portfolio
- Visualisasi Dataset AI
- Analisis Data Sampah

---

# ✨ Author

Developed by:
**Data Science Capstone Team**

# Buat_Datasience