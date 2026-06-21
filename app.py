import streamlit as st
import pandas as pd
import os
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import base64
import io
import tensorflow as tf

def get_base64_of_image(rel_path):
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, rel_path)
        with open(full_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except Exception:
        return ""

@st.cache_resource
def load_classification_model():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, 'model_solo_final.keras')
        model = tf.keras.models.load_model(model_path)
        return model, None
    except Exception as e:
        return None, str(e)

klasifikasi_model, error_msg = load_classification_model()

st.set_page_config(
    page_title="SOLO",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    .stApp { 
        background: linear-gradient(135deg, #0a0e17 0%, #111827 50%, #0a0e17 100%);
        font-family: 'Inter', sans-serif;
    }

    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 20% 80%, rgba(76, 175, 80, 0.03) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(33, 150, 243, 0.03) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }

    .main-header { 
        font-size: 3.2rem; 
        font-weight: 900; 
        background: linear-gradient(135deg, #4CAF50 0%, #81C784 50%, #4CAF50 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        text-align: center;
        letter-spacing: -1px;
    }

    .sub-header {
        font-size: 1.4rem;
        color: #9CA3AF;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 300;
    }

    .info-card {
        background: linear-gradient(145deg, rgba(30, 30, 30, 0.9) 0%, rgba(20, 20, 20, 0.95) 100%);
        padding: 28px;
        border-radius: 20px;
        border: 1px solid rgba(76, 175, 80, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }

    .info-card:hover {
        border-color: rgba(76, 175, 80, 0.5);
        box-shadow: 0 12px 40px rgba(76, 175, 80, 0.1);
        transform: translateY(-2px);
    }

    .info-card h3 {
        color: #4CAF50;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .info-card p, .info-card li {
        color: #D1D5DB;
        line-height: 1.7;
        font-size: 0.95rem;
    }

    [data-testid="metric-container"] {
        background: linear-gradient(145deg, #1a1f2e 0%, #161b22 100%) !important;
        border: 1px solid rgba(76, 175, 80, 0.15) !important;
        padding: 20px !important;
        border-radius: 16px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="metric-container"]:hover {
        border-color: rgba(76, 175, 80, 0.4) !important;
        transform: translateY(-2px);
    }

    [data-testid="metric-container"] label {
        color: #9CA3AF !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
    }

    [data-testid="metric-container"] .metric-value {
        color: #4CAF50 !important;
        font-weight: 800 !important;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #F3F4F6;
        margin: 2rem 0 1.5rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(76, 175, 80, 0.3);
    }

    .section-subtitle {
        font-size: 1.1rem;
        color: #9CA3AF;
        margin-bottom: 2rem;
        font-weight: 300;
    }

    .cat-card-organik {
        background: linear-gradient(145deg, rgba(76, 175, 80, 0.1) 0%, rgba(20, 20, 20, 0.95) 100%);
        border-left: 4px solid #4CAF50;
    }

    .cat-card-anorganik {
        background: linear-gradient(145deg, rgba(33, 150, 243, 0.1) 0%, rgba(20, 20, 20, 0.95) 100%);
        border-left: 4px solid #2196F3;
    }

    .cat-card-b3 {
        background: linear-gradient(145deg, rgba(244, 67, 54, 0.1) 0%, rgba(20, 20, 20, 0.95) 100%);
        border-left: 4px solid #F44336;
    }

    .css-1d391kg {
        background: linear-gradient(180deg, #0f1419 0%, #1a1f2e 100%);
    }

    .stButton>button {
        background: linear-gradient(135deg, #4CAF50 0%, #388E3C 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(76, 175, 80, 0.3);
    }

    .image-container {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }

    .image-container:hover {
        transform: scale(1.02);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
    }

    .stDataFrame {
        border-radius: 16px;
        overflow: hidden;
    }

    .stSelectbox>div>div {
        background: #1a1f2e;
        border-radius: 12px;
        border: 1px solid rgba(76, 175, 80, 0.2);
    }

    .stRadio>div {
        background: transparent;
    }

    .stRadio>div>label {
        color: #D1D5DB;
        font-weight: 500;
        padding: 8px 12px;
        border-radius: 8px;
        transition: all 0.2s ease;
    }

    .stRadio>div>label:hover {
        background: rgba(76, 175, 80, 0.1);
    }

    hr {
        border-color: rgba(76, 175, 80, 0.2) !important;
        margin: 2rem 0 !important;
    }

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #0a0e17;
    }

    ::-webkit-scrollbar-thumb {
        background: #4CAF50;
        border-radius: 4px;
    }

    .stAlert {
        border-radius: 16px !important;
        border: none !important;
        padding: 20px !important;
    }

    .stSuccess {
        background: linear-gradient(145deg, rgba(76, 175, 80, 0.15) 0%, rgba(20, 20, 20, 0.9) 100%) !important;
        border-left: 4px solid #4CAF50 !important;
    }

    .stWarning {
        background: linear-gradient(145deg, rgba(255, 152, 0, 0.15) 0%, rgba(20, 20, 20, 0.9) 100%) !important;
        border-left: 4px solid #FF9800 !important;
    }

    .caption-text {
        color: #6B7280;
        font-size: 0.85rem;
        font-style: italic;
        text-align: center;
        margin-top: 8px;
    }

    .tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
    }

    .tag-green {
        background: rgba(76, 175, 80, 0.2);
        color: #81C784;
        border: 1px solid rgba(76, 175, 80, 0.3);
    }

    .tag-blue {
        background: rgba(33, 150, 243, 0.2);
        color: #64B5F6;
        border: 1px solid rgba(33, 150, 243, 0.3);
    }

    .tag-red {
        background: rgba(244, 67, 54, 0.2);
        color: #E57373;
        border: 1px solid rgba(244, 67, 54, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    
    logo_b64 = get_base64_of_image("foto/logo.png")
    if not logo_b64:
        logo_b64 = get_base64_of_image("logo.png")
        
    if logo_b64:
        img_html = f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{logo_b64}" width="100" height="100" style="border-radius: 50%; object-fit: cover; border: 2px solid #4CAF50;"></div>'
    else:
        img_html = '<div style="text-align: center;"><span style="font-size: 4rem;">♻️</span></div>'
        
    st.markdown(f"""
        {img_html}
        <h2 style="font-size: 1.2rem; color: #4CAF50; font-weight: 700; text-align:center; margin-top: 0.5rem;">
            SOLO
        </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    menu = st.radio("Navigasi", ["Beranda", "Dataset Overview", "Eksplorasi Gambar", "Business Insight", "Evaluasi Model", "Uji Model AI"])

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<p style='color: #6B7280; font-size: 0.75rem; font-weight: 600;'>QUICK METRICS</p>", unsafe_allow_html=True)

    sidebar_metric_1 = st.empty()
    sidebar_metric_2 = st.empty()

DATASET_PATH = "Dataset_Final_Cleaned/content/Dataset_Final_Cleaned"

@st.cache_data
def load_data(path):
    data = []
    if not os.path.exists(path): return pd.DataFrame()
    for subset in ["train", "validation", "test"]:
        p = os.path.join(path, subset)
        if os.path.exists(p):
            for cat in os.listdir(p):
                cat_p = os.path.join(p, cat)
                if os.path.isdir(cat_p):
                    data.append({"Subset": subset, "Kategori": cat, "Jumlah": len(os.listdir(cat_p))})
    return pd.DataFrame(data)

df = load_data(DATASET_PATH)

if not df.empty:
    total_data = df["Jumlah"].sum()
    total_classes = df["Kategori"].nunique()
    sidebar_metric_1.markdown(f"""
        <div style="background: #161b22; padding: 10px; border-radius: 8px; margin-bottom: 8px;">
            <p style="margin: 0; color: #9CA3AF; font-size: 0.7rem;">TOTAL SAMPLES</p>
            <p style="margin: 0; color: #4CAF50; font-size: 1.2rem; font-weight: 800;">{total_data:,}</p>
        </div>
    """, unsafe_allow_html=True)
    sidebar_metric_2.markdown(f"""
        <div style="background: #161b22; padding: 10px; border-radius: 8px;">
            <p style="margin: 0; color: #9CA3AF; font-size: 0.7rem;">CLASSES</p>
            <p style="margin: 0; color: #2196F3; font-size: 1.2rem; font-weight: 800;">{total_classes}</p>
        </div>
    """, unsafe_allow_html=True)

if menu == "Beranda":
    st.markdown("""
        <h1 class="main-header">SOLO : Sortir & Olah Limbah Online</h1>
        <p class="sub-header">Sistem Klasifikasi Sampah Otomatis Berbasis Computer Vision</p>
    """, unsafe_allow_html=True)

    col_img = st.columns([1, 3, 1])[1]
    with col_img:
        st.markdown("""
            <div class="image-container">
                <img src="https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?w=1200&q=80" 
                     style="width: 100%; border-radius: 16px;" />
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align: center; max-width: 800px; margin: 0 auto 3rem auto;">
            <h2 style="color: #F3F4F6; font-size: 1.8rem; font-weight: 700; margin-bottom: 1rem;">
                Transformasi Pengelolaan Limbah
            </h2>
            <p style="color: #9CA3AF; font-size: 1.1rem; line-height: 1.8;">
                Dashboard ini merupakan instrumen analisis canggih untuk memantau integritas data pada model klasifikasi sampah. 
                Dengan memisahkan sampah secara presisi sejak awal, kita dapat meningkatkan angka daur ulang dan menekan polusi lingkungan secara signifikan.
            </p>
        </div>
    """, unsafe_allow_html=True)

    if not df.empty:
        st.markdown("<h2 class='section-title'>Metrik Utama</h2>", unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric("Total Dataset", f"{df['Jumlah'].sum():,}")
        with m2:
            st.metric("Jumlah Kelas", f"{df['Kategori'].nunique()}")
        with m3:
            train_pct = (df[df['Subset']=='train']['Jumlah'].sum() / df['Jumlah'].sum() * 100)
            st.metric("Data Training", f"{train_pct:.1f}%")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<h2 class='section-title'>Tujuan Utama Sistem</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="info-card cat-card-organik">
                <h3>Sampah Organik</h3>
                <p style="color: #D1D5DB; line-height: 1.7;">
                    Identifikasi sampah organik secara akurat untuk kebutuhan pengolahan pupuk cair maupun padat. 
                    Sistem membedakan sisa sayuran segar dengan yang sudah layu untuk klasifikasi presisi.
                </p>
                <div style="margin-top: 15px;">
                    <span class="tag tag-green">Biogas</span>
                    <span class="tag tag-green">Kompos</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="info-card cat-card-anorganik">
                <h3>Sampah Anorganik</h3>
                <p style="color: #D1D5DB; line-height: 1.7;">
                    Memilah sampah anorganik agar dapat masuk kembali ke rantai ekonomi sirkular melalui industri daur ulang. 
                    Meningkatkan efisiensi bank sampah dengan pemilahan otomatis yang cepat.
                </p>
                <div style="margin-top: 15px;">
                    <span class="tag tag-blue">Daur Ulang</span>
                    <span class="tag tag-blue">Ekonomi Sirkular</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="info-card cat-card-b3">
                <h3>Sampah B3</h3>
                <p style="color: #D1D5DB; line-height: 1.7;">
                    Memisahkan limbah B3 untuk memastikan zat kimia berbahaya tidak mencemari tanah dan sumber air. 
                    Kategori dengan risiko tertinggi yang memerlukan penanganan khusus dan terpisah.
                </p>
                <div style="margin-top: 15px;">
                    <span class="tag tag-red">Berbahaya</span>
                    <span class="tag tag-red">Penanganan Khusus</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

elif menu == "Dataset Overview":
    st.markdown("<h1 class='section-title'>Analisis Distribusi Dataset</h1>", unsafe_allow_html=True)
    st.markdown("<p class='section-subtitle'>Visualisasi komprehensif untuk memahami struktur dan keseimbangan data training</p>", unsafe_allow_html=True)

    if not df.empty:
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            total = df["Jumlah"].sum()
            st.metric("Total Samples", f"{total:,}")
        with col_m2:
            avg_per_class = df.groupby("Kategori")["Jumlah"].sum().mean()
            st.metric("Rata-rata per Kelas", f"{avg_per_class:.0f}")
        with col_m3:
            max_class = df.loc[df["Jumlah"].idxmax(), "Kategori"]
            st.metric("Kelas Dominan", max_class)

        st.markdown("<br>", unsafe_allow_html=True)

        fig_dist = px.bar(
            df, 
            x="Kategori", 
            y="Jumlah", 
            color="Subset",
            barmode="group", 
            template="plotly_dark",
            color_discrete_sequence=["#4CAF50", "#2196F3", "#FF9800"],
            title="Distribusi Dataset per Kelas dan Subset",
            labels={"Jumlah": "Jumlah Sampel", "Kategori": "Kategori Sampah"}
        )
        fig_dist.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter, sans-serif", color="#D1D5DB"),
            title_font=dict(size=20, color="#F3F4F6"),
            legend_title_font=dict(size=12),
            legend_font=dict(size=11),
            xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
            height=500
        )
        st.plotly_chart(fig_dist, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col_pie, col_table = st.columns([1, 1])

        with col_pie:
            subset_summary = df.groupby("Subset")["Jumlah"].sum().reset_index()
            fig_pie = px.pie(
                subset_summary,
                values="Jumlah",
                names="Subset",
                title="Proporsi Data per Subset",
                template="plotly_dark",
                color_discrete_sequence=["#4CAF50", "#2196F3", "#FF9800"]
            )
            fig_pie.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Inter, sans-serif", color="#D1D5DB"),
                title_font=dict(size=16, color="#F3F4F6"),
                height=400
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        with col_table:
            st.markdown("<h3 style='color: #F3F4F6; font-size: 1.2rem; margin-bottom: 1rem;'>📋 Rincian Tabel Data</h3>", unsafe_allow_html=True)
            st.dataframe(
                df.sort_values(["Kategori", "Subset"]).reset_index(drop=True),
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Subset": st.column_config.TextColumn("Subset", width="medium"),
                    "Kategori": st.column_config.TextColumn("Kategori", width="medium"),
                    "Jumlah": st.column_config.NumberColumn("Jumlah", format="%d", width="small")
                }
            )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("<h2 class='section-title'>Analisis Keseimbangan Kelas</h2>", unsafe_allow_html=True)

        summary = df.groupby("Kategori", as_index=False)["Jumlah"].sum()
        fig_balance = px.bar(
            summary.sort_values("Jumlah", ascending=True),
            x="Jumlah",
            y="Kategori",
            orientation="h",
            color="Jumlah",
            color_continuous_scale=["#4CAF50", "#81C784", "#FFB74D", "#FF9800"],
            title="Total Sampel per Kelas (Horizontal View)",
            template="plotly_dark",
            text_auto=True
        )
        fig_balance.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter, sans-serif", color="#D1D5DB"),
            title_font=dict(size=18, color="#F3F4F6"),
            xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
            height=350,
            coloraxis_showscale=False
        )
        st.plotly_chart(fig_balance, use_container_width=True)

        diff = summary["Jumlah"].max() - summary["Jumlah"].min()
        if diff < 300:
            st.success(f"**Dataset Seimbang** — Selisih antar kelas hanya {diff} sampel. Model AI akan belajar secara adil tanpa bias terhadap kelas mayoritas.")
        else:
            st.warning(f"**Ketimpangan Terdeteksi** — Selisih {diff} sampel antar kelas. Disarankan augmentasi data atau teknik resampling untuk menyeimbangkan distribusi.")

    else:
        st.error("Path dataset tidak ditemukan. Pastikan direktori `Dataset_Final_Cleaned` tersedia di lokasi yang benar.")

elif menu == "Eksplorasi Gambar":
    st.markdown("<h1 class='section-title'>Eksplorasi Karakteristik Visual</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p class='section-subtitle'>
            Pemahaman fitur visual sangat krusial dalam pengembangan Convolutional Neural Network (CNN). 
            Model AI akan belajar mengenali pola berdasarkan bentuk, warna, dan tekstur yang kita berikan melalui dataset.
        </p>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='color: #F3F4F6; font-size: 1.5rem; margin: 2rem 0 1.5rem 0;'>Karakteristik Visual per Kategori</h2>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
            <div class="info-card cat-card-organik">
                <div style="text-align: center; margin-bottom: 15px;">
                    <span style="font-size: 3rem;"></span>
                </div>
                <h3 style="text-align: center; color: #4CAF50;">Sampah Organik</h3>
                <hr style="border-color: rgba(76, 175, 80, 0.2); margin: 15px 0;">
                <p style="color: #D1D5DB; font-size: 0.9rem; line-height: 1.7;">
                    <strong style="color: #81C784;">Fitur Visual Utama:</strong><br>
                    • Tidak memiliki bentuk geometris konsisten<br>
                    • Tekstur serat yang khas<br>
                    • Warna alami cenderung kusam (hijau ke cokelat)<br>
                    • Pantulan cahaya minim (kelembapan)<br><br>
                    <strong style="color: #81C784;">Nilai Strategis:</strong><br>
                    Akurasi tinggi memungkinkan pemisahan limbah dapur otomatis untuk biogas. AI membedakan sayuran segar vs layu.
                </p>
                <div style="margin-top: 15px;">
                    <span class="tag tag-green">Biogas</span>
                    <span class="tag tag-green">Pupuk Organik</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
            <div class="info-card cat-card-anorganik">
                <div style="text-align: center; margin-bottom: 15px;">
                    <span style="font-size: 3rem;"></span>
                </div>
                <h3 style="text-align: center; color: #2196F3;">Sampah Anorganik</h3>
                <hr style="border-color: rgba(33, 150, 243, 0.2); margin: 15px 0;">
                <p style="color: #D1D5DB; font-size: 0.9rem; line-height: 1.7;">
                    <strong style="color: #64B5F6;">Fitur Visual Utama:</strong><br>
                    • Bentuk presisi buatan manusia<br>
                    • Lengkungan botol, sudut kardus<br>
                    • Refleksi cahaya (specular reflection)<br>
                    • Permukaan datar kaleng & plastik<br><br>
                    <strong style="color: #64B5F6;">Nilai Strategis:</strong><br>
                    Pemilahan otomatis cepat meningkatkan efisiensi bank sampah. Data membantu industri manufaktur mendapatkan bahan baku bersih.
                </p>
                <div style="margin-top: 15px;">
                    <span class="tag tag-blue">Daur Ulang</span>
                    <span class="tag tag-blue">Bank Sampah</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
            <div class="info-card cat-card-b3">
                <div style="text-align: center; margin-bottom: 15px;">
                    <span style="font-size: 3rem;"></span>
                </div>
                <h3 style="text-align: center; color: #F44336;">Sampah B3</h3>
                <hr style="border-color: rgba(244, 67, 54, 0.2); margin: 15px 0;">
                <p style="color: #D1D5DB; font-size: 0.9rem; line-height: 1.7;">
                    <strong style="color: #E57373;">Fitur Visual Utama:</strong><br>
                    • Kemasan silinder (baterai/semprotan)<br>
                    • Wadah plastik tebal<br>
                    • Label warna kontras tinggi<br>
                    • Simbol peringatan khas<br><br>
                    <strong style="color: #E57373;">Nilai Strategis:</strong><br>
                    Kategori risiko tertinggi. Kegagalan klasifikasi B3 dapat menyebabkan kontaminasi beracun. Penanganan khusus wajib.
                </p>
                <div style="margin-top: 15px;">
                    <span class="tag tag-red">Berbahaya</span>
                    <span class="tag tag-red">Kontaminasi</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<h2 class='section-title'>Preview Sampel Gambar</h2>", unsafe_allow_html=True)

    path_train = os.path.join(DATASET_PATH, "train")
    if os.path.exists(path_train):
        cat_list = [c for c in os.listdir(path_train) if os.path.isdir(os.path.join(path_train, c))]

        target = st.selectbox(
            "Pilih Kategori untuk Preview Sampel:",
            cat_list,
            index=0
        )

        full_p = os.path.join(path_train, target)
        imgs = os.listdir(full_p)[:8]

        def img_to_base64_local(img):
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode()

        if imgs:
            for row in range(0, len(imgs), 4):
                cols = st.columns(4)
                for i in range(4):
                    idx = row + i
                    if idx < len(imgs):
                        with cols[i]:
                            try:
                                img = Image.open(os.path.join(full_p, imgs[idx]))
                                st.markdown(f"""
                                    <div class="image-container">
                                        <img src="data:image/png;base64,{img_to_base64_local(img)}" 
                                             style="width: 100%; border-radius: 16px;" />
                                    </div>
                                    <p class="caption-text">Sample {idx+1} — {target}</p>
                                """, unsafe_allow_html=True)
                            except:
                                st.image(img, caption=f"Sample {idx+1} — {target}", use_container_width=True)
        else:
            st.info("Tidak ada gambar tersedia di kategori ini.")
    else:
        st.error("Direktori training tidak ditemukan.")

elif menu == "Business Insight":
    st.markdown("<h1 class='section-title'>Analisis Pertanyaan Bisnis</h1>", unsafe_allow_html=True)
    st.markdown("<p class='section-subtitle'>Insight data-driven untuk pengambilan keputusan strategis dalam pengelolaan sampah</p>", unsafe_allow_html=True)

    st.markdown("""
        <div style="background: linear-gradient(145deg, rgba(33, 150, 243, 0.05) 0%, rgba(20, 20, 20, 0.9) 100%); 
                    padding: 25px; border-radius: 20px; border: 1px solid rgba(33, 150, 243, 0.15);
                    margin-bottom: 2rem;">
            <h2 style="color: #F3F4F6; font-size: 1.5rem; margin-bottom: 1rem;">
                Analisis Volume & Pengelolaan Sampah (EDA)
            </h2>
        </div>
    """, unsafe_allow_html=True)

    try:
        df_vol = pd.read_csv('Dataset_Sampah_Cleaned_2018_2025.csv')

        with st.expander("Lihat Statistik Deskriptif (Describe Data)", expanded=False):
            st.dataframe(df_vol.describe(include='all'), use_container_width=True)

        st.markdown("<h3 style='color: #4CAF50; margin-top: 20px;'>1. Kecamatan Penghasil Sampah Paling Banyak</h3>", unsafe_allow_html=True)
        q1_vol = df_vol.groupby('kecamatan')['berat_kg'].sum().sort_values(ascending=False).reset_index().head(10)
        fig_q1_v = px.bar(
            q1_vol, x="berat_kg", y="kecamatan", orientation='h',
            title="Top 10 Kecamatan Penyumbang Sampah Terbesar",
            labels={"berat_kg": "Total Berat Sampah (Kg)", "kecamatan": "Kecamatan"},
            template="plotly_dark", color="berat_kg", color_continuous_scale="Reds"
        )
        fig_q1_v.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_q1_v, use_container_width=True)

        st.markdown("<h3 style='color: #4CAF50; margin-top: 20px;'>2. Jenis Sampah & Metode Pengelolaannya</h3>", unsafe_allow_html=True)
        col_eda1, col_eda2 = st.columns(2)
        with col_eda1:
            jenis_freq = df_vol['jenis_sampah'].value_counts().reset_index()
            jenis_freq.columns = ['jenis_sampah', 'jumlah']
            fig_q2a_v = px.bar(
                jenis_freq, x="jenis_sampah", y="jumlah",
                title="Distribusi Jenis Sampah",
                labels={"jumlah": "Frekuensi Kemunculan", "jenis_sampah": "Jenis Sampah"},
                template="plotly_dark", color="jenis_sampah", color_discrete_sequence=px.colors.qualitative.Pastel
            )
            st.plotly_chart(fig_q2a_v, use_container_width=True)
            
        with col_eda2:
            jenis_terbanyak = jenis_freq.iloc[0]['jenis_sampah']
            pengelolaan_top = df_vol[df_vol['jenis_sampah'] == jenis_terbanyak]['metode_pengelolaan'].value_counts().reset_index()
            fig_q2b_v = px.bar(
                pengelolaan_top, x="metode_pengelolaan", y="count",
                title=f"Metode Pengelolaan Sampah {jenis_terbanyak.title()}",
                labels={"count": "Jumlah Kasus", "metode_pengelolaan": "Metode Pengelolaan"},
                template="plotly_dark", color="metode_pengelolaan", color_discrete_sequence=px.colors.sequential.Greens_r
            )
            st.plotly_chart(fig_q2b_v, use_container_width=True)

        st.markdown("<h3 style='color: #4CAF50; margin-top: 20px;'>3. Pengaruh Cuaca Terhadap Berat Sampah</h3>", unsafe_allow_html=True)
        berat_cuaca = df_vol.groupby('cuaca')['berat_kg'].mean().sort_values(ascending=False).reset_index()
        fig_q3_v = px.bar(
            berat_cuaca, x="cuaca", y="berat_kg", text_auto='.1f',
            title="Rata-rata Berat Sampah Berdasarkan Kondisi Cuaca",
            labels={"berat_kg": "Rata-rata Berat Sampah (Kg)", "cuaca": "Kondisi Cuaca"},
            template="plotly_dark", color="cuaca", color_discrete_sequence=px.colors.qualitative.Set2
        )
        mean_berat_all = df_vol['berat_kg'].mean()
        fig_q3_v.add_hline(y=mean_berat_all, line_dash="dash", line_color="red", annotation_text=f"Rata-rata: {mean_berat_all:.1f} Kg")
        st.plotly_chart(fig_q3_v, use_container_width=True)
        
        st.markdown("""
            <div class="info-card" style="border-left-color: #4CAF50; margin-top: 2rem;">
                <h3 style="color: #4CAF50; margin-bottom: 15px;">Kesimpulan Analisis Data Tabular</h3>
                <p style="color: #D1D5DB; line-height: 1.8; font-size: 1rem;">
                    Berdasarkan analisis data sampah yang telah dilakukan, ada beberapa kesimpulan:
                </p>
                <ul style="color: #D1D5DB; line-height: 1.8; margin-top: 10px;">
                    <li><strong>Kecamatan Penyumbang Sampah Terbesar:</strong> Kecamatan Cilandak teridentifikasi sebagai penyumbang berat sampah tertinggi, diikuti oleh Pasar Minggu dan Cengkareng. Hal ini menunjukkan perlunya fokus dan strategi pengelolaan sampah yang lebih intensif di wilayah-wilayah tersebut.</li>
                    <li><strong>Jenis Sampah Dominan dan Pengelolaan:</strong> Sampah organik adalah jenis sampah yang paling dominan dalam dataset. Untuk mengelola sampah organik secara efektif, metode seperti pengomposan atau produksi biogas sangat direkomendasikan. Selain itu, proporsi sampah anorganik seperti kertas dan plastik yang signifikan menekankan pentingnya program daur ulang yang terstruktur dan edukasi masyarakat mengenai pemilahan sampah di sumbernya.</li>
                    <li><strong>Pengaruh Cuaca:</strong> Analisis menunjukkan bahwa kondisi cuaca (cerah, hujan, mendung) memiliki pengaruh yang tidak signifikan terhadap jumlah berat sampah yang dihasilkan. Fluktuasi berat sampah cenderung stabil terlepas dari kondisi cuaca, menunjukkan bahwa faktor lain mungkin lebih berpengaruh terhadap volume sampah harian.</li>
                </ul>
                <p style="color: #D1D5DB; line-height: 1.8; font-size: 1rem; margin-top: 15px;">
                    Secara keseluruhan, temuan ini memberikan dasar bagi pemerintah daerah dan pemangku kepentingan lainnya untuk merancang kebijakan dan program pengelolaan sampah yang lebih tepat sasaran, dengan memprioritaskan area dan jenis sampah tertentu, serta mengoptimalkan strategi berdasarkan karakteristik data yang ada.
                </p>
            </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.info(f"Visualisasi Volume Sampah tidak dapat ditampilkan. Pastikan file 'Dataset_Sampah_Cleaned_2018_2025.csv' berada dalam folder yang sama. (Error: {e})")

    st.markdown("<br>", unsafe_allow_html=True)

    if not df.empty:
        summary = df.groupby("Kategori", as_index=False)["Jumlah"].sum()

        st.markdown("""
            <div style="background: linear-gradient(145deg, rgba(76, 175, 80, 0.05) 0%, rgba(20, 20, 20, 0.9) 100%); 
                        padding: 25px; border-radius: 20px; border: 1px solid rgba(76, 175, 80, 0.15);
                        margin-bottom: 2rem;">
                <h2 style="color: #F3F4F6; font-size: 1.5rem; margin-bottom: 1rem;">
                    Apakah Dataset Gambar Sudah Seimbang?
                </h2>
            </div>
        """, unsafe_allow_html=True)

        fig1 = px.bar(
            summary, 
            x="Kategori", 
            y="Jumlah", 
            color="Kategori",
            text_auto=True, 
            title="Distribusi Total Data Per Kelas",
            template="plotly_dark",
            color_discrete_sequence=["#4CAF50", "#2196F3", "#F44336"]
        )
        fig1.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter, sans-serif", color="#D1D5DB"),
            title_font=dict(size=18, color="#F3F4F6"),
            showlegend=False,
            height=450
        )
        st.plotly_chart(fig1, use_container_width=True)

        diff = summary["Jumlah"].max() - summary["Jumlah"].min()

        col_q1_1, col_q1_2 = st.columns([2, 1])
        with col_q1_1:
            if diff < 300:
                st.success(f"""
                    **Dataset Tergolong Seimbang**

                    Selisih antar kelas hanya **{diff}** sampel. Model AI akan belajar secara adil dan tidak mengalami bias terhadap salah satu jenis sampah. 
                """)
            else:
                st.warning(f"""
                    **Ketimpangan Dataset Terdeteksi**

                    Terdapat selisih **{diff}** sampel antar kelas. Disarankan menambah data atau augmentasi.
                """)

        with col_q1_2:
            st.markdown("""
                        <div style="background: #161b22; padding: 20px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05);">
                        <p style="color: #9CA3AF; font-size: 0.8rem; margin-bottom: 10px;">STATISTIK KESEIMBANGAN</p>
                    """, unsafe_allow_html=True)
            for _, row in summary.iterrows():
                pct = (row["Jumlah"] / summary["Jumlah"].sum()) * 100
                color = "#4CAF50" if row["Kategori"].lower() in ["organik", "organic"] else "#2196F3" if row["Kategori"].lower() in ["anorganik", "inorganic"] else "#F44336"
                st.markdown(f"""
                    <div style="margin-bottom: 12px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="color: #D1D5DB; font-size: 0.85rem;">{row["Kategori"]}</span>
                            <span style="color: {color}; font-size: 0.85rem; font-weight: 600;">{pct:.1f}%</span>
                        </div>
                        <div style="background: rgba(255,255,255,0.05); border-radius: 4px; height: 6px;">
                            <div style="background: {color}; width: {pct}%; height: 100%; border-radius: 4px; transition: width 0.5s ease;"></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
            <div style="background: linear-gradient(145deg, rgba(33, 150, 243, 0.05) 0%, rgba(20, 20, 20, 0.9) 100%); 
                        padding: 25px; border-radius: 20px; border: 1px solid rgba(33, 150, 243, 0.15);
                        margin-bottom: 2rem;">
                <h2 style="color: #F3F4F6; font-size: 1.5rem; margin-bottom: 1rem;">
                    Kategori Sampah Gambar Apa yang Mendominasi?
                </h2>
            </div>
        """, unsafe_allow_html=True)

        fig2 = px.bar(
            summary.sort_values("Jumlah", ascending=True), 
            x="Jumlah", 
            y="Kategori", 
            orientation='h',
            color="Jumlah", 
            title="Urutan Dominasi Sampah (Terendah ke Tertinggi)",
            text_auto=True, 
            template="plotly_dark",
            color_continuous_scale=["#4CAF50", "#81C784", "#FFB74D", "#FF9800"]
        )
        fig2.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter, sans-serif", color="#D1D5DB"),
            title_font=dict(size=18, color="#F3F4F6"),
            showlegend=False,
            height=400,
            coloraxis_showscale=False
        )
        st.plotly_chart(fig2, use_container_width=True)

        top_cat = summary.loc[summary["Jumlah"].idxmax(), "Kategori"]
        top_count = summary["Jumlah"].max()
        top_pct = (top_count / summary["Jumlah"].sum()) * 100

        st.markdown("""
            <div class="info-card" style="margin-top: 2rem; border-left: 4px solid #4CAF50;">
            <h3 style="color: #4CAF50;">Kesimpulan Akhir: Dataset Klasifikasi Gambar</h3>
            <p style="color: #D1D5DB; line-height: 1.8;">
            Seluruh proses dari pengumpulan data hingga finalisasi dataset untuk pelatihan model klasifikasi sampah 
            telah berhasil dilakukan. Dataset telah dibersihkan dari duplikasi, dinormalisasi ke dalam tiga kategori
             utama (Anorganik, Organik, B3), dan diseimbangkan untuk mengatasi ketidakseimbangan kelas. 
            Visualisasi data telah memberikan wawasan tentang distribusi kategori and ukuran file. Pembagian 
            dataset menjadi train, test, dan validation telah dilakukan dengan stratifikasi untuk memastikan 
            representasi kelas yang seimbang di setiap subset. Terakhir, gambar-gambar telah diproses, diubah ukurannya, dan disimpan dalam struktur 
            folder yang terorganisir, siap untuk digunakan dalam pelatihan model klasifikasi gambar.
            </p>
            </div>
      """, unsafe_allow_html=True)

elif menu == "Evaluasi Model":
    st.markdown("<h1 class='section-title'>Evaluasi Kinerja Model</h1>", unsafe_allow_html=True)
    st.markdown("<p class='section-subtitle'>Visualisasi riwayat pelatihan dan Confusion Matrix dari proses training model.</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='color: #F3F4F6; font-size: 1.5rem; margin-bottom: 1rem;'>Visualisasi History Pelatihan</h2>", unsafe_allow_html=True)
    
    uploaded_history_img = st.file_uploader("Unggah gambar grafik History Pelatihan (JPG/PNG)...", type=["jpg", "jpeg", "png"], key="hist")
    
    if uploaded_history_img is not None:
        hist_image = Image.open(uploaded_history_img)
        st.image(hist_image, caption='Grafik History Pelatihan', use_container_width=True)
    else:
        st.info("Harap unggah gambar grafik history pelatihan model Anda.")

    st.markdown("<br><h2 style='color: #F3F4F6; font-size: 1.5rem; margin-bottom: 1rem;'>Confusion Matrix</h2>", unsafe_allow_html=True)
    
    uploaded_cm_img = st.file_uploader("Unggah gambar Confusion Matrix (JPG/PNG)...", type=["jpg", "jpeg", "png"], key="cm")
    
    if uploaded_cm_img is not None:
        cm_image = Image.open(uploaded_cm_img)
        st.image(cm_image, caption='Confusion Matrix Hasil Evaluasi', use_container_width=True)
    else:
        st.info("Harap unggah gambar Confusion Matrix model Anda.")

elif menu == "Uji Model AI":
    st.markdown("<h1 class='section-title'>Uji Coba Model Klasifikasi 🤖</h1>", unsafe_allow_html=True)
    st.markdown("<p class='section-subtitle'>Unggah gambar sampah untuk diklasifikasikan secara real-time oleh model SOLO.</p>", unsafe_allow_html=True)

    if klasifikasi_model is None:
        st.error(f"⚠️ Gagal memuat model! Error aslinya: {error_msg}")
    else:
        uploaded_file = st.file_uploader("Pilih gambar sampah (JPG/PNG)...", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            col_img, col_res = st.columns([1, 1])
            
            with col_img:
                image = Image.open(uploaded_file)
                st.image(image, caption='Gambar yang diunggah', use_container_width=True)
            
            with col_res:
                st.markdown("<h3 style='color: #F3F4F6;'>Hasil Analisis</h3>", unsafe_allow_html=True)
                
                if st.button('🔍 Mulai Klasifikasi'):
                    with st.spinner('Sedang memproses gambar...'):
                        try:
                            target_size = (224, 224)
                            
                            if image.mode != "RGB":
                                image = image.convert("RGB")
                                
                            img_resized = image.resize(target_size)
                            img_array = np.array(img_resized)
                            img_array = np.expand_dims(img_array, axis=0)
                            
                            predictions = klasifikasi_model.predict(img_array)
                            predicted_class_idx = np.argmax(predictions[0])
                            confidence = np.max(predictions[0]) * 100
                            
                            class_names = ['Anorganik', 'B3', 'Organik']
                            
                            predicted_class = class_names[predicted_class_idx]
                            
                            if predicted_class == 'Organik':
                                st.success(f"**Kategori:** {predicted_class}")
                            elif predicted_class == 'Anorganik':
                                st.info(f"**Kategori:** {predicted_class}")
                            else:
                                st.error(f"**Kategori:** {predicted_class}")
                                
                            st.write(f"**Tingkat Kepercayaan (Confidence):** {confidence:.2f}%")
                            
                            st.progress(int(confidence))
                            
                        except Exception as e:
                            st.error(f"Terjadi kesalahan saat memproses: {e}")