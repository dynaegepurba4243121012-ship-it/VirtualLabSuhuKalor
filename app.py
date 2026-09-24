import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import io

# ============================================================
# KONFIGURASI
# ============================================================

st.set_page_config(
    page_title="Virtual Lab Suhu dan Kalor",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: #f5f7fb;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #071a35 0%, #0b315d 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.sidebar-title {
    text-align: center;
    font-size: 23px;
    font-weight: 800;
    margin-top: 15px;
}

.sidebar-subtitle {
    text-align: center;
    font-size: 12px;
    opacity: 0.75;
    margin-bottom: 25px;
}

/* HERO */

.hero {
    background: linear-gradient(135deg, #083b73 0%, #1473bd 100%);
    color: white;
    border-radius: 24px;
    padding: 40px;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
}

.hero h1 {
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    font-size: 15px;
    line-height: 1.7;
}

/* CARD */

.card {
    background: white;
    border-radius: 18px;
    padding: 25px;
    border: 1px solid #e1e7ef;
    box-shadow: 0 5px 18px rgba(0,0,0,0.05);
    margin-bottom: 18px;
}

.card h3 {
    color: #123b68;
}

/* SECTION */

.section-title {
    color: #123b68;
    font-size: 25px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* PRAKTIKUM */

.praktikum-box {
    background: white;
    border-radius: 18px;
    padding: 28px;
    border: 1px solid #dfe6ef;
    margin-bottom: 22px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.04);
}

.praktikum-title {
    font-size: 22px;
    font-weight: 700;
    color: #123b68;
    margin-bottom: 15px;
}

/* TUJUAN */

.objective {
    background: #eef7ff;
    border-left: 5px solid #1675c8;
    padding: 18px;
    border-radius: 10px;
    line-height: 1.7;
}

/* ANALISIS */

.analysis {
    background: #fff8e8;
    border-left: 5px solid #f0a500;
    padding: 20px;
    border-radius: 12px;
    line-height: 1.8;
}

/* HASIL */

.result {
    background: #edf7ff;
    border-left: 5px solid #1473bd;
    padding: 20px;
    border-radius: 12px;
}

.big-result {
    font-size: 35px;
    font-weight: 800;
    color: #0964aa;
}

/* FOOTER */

.footer {
    margin-top: 50px;
    padding: 25px;
    text-align: center;
    color: #7d8a9c;
    border-top: 1px solid #dfe4eb;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "halaman" not in st.session_state:
    st.session_state.halaman = "Beranda"

if "hasil_praktikum" not in st.session_state:
    st.session_state.hasil_praktikum = []


# ============================================================
# FUNGSI SIMPAN HASIL
# ============================================================

def simpan_hasil(data):
    st.session_state.hasil_praktikum.append(data)


def buat_csv():

    if not st.session_state.hasil_praktikum:
        return None

    df = pd.DataFrame(st.session_state.hasil_praktikum)

    output = io.StringIO()
    df.to_csv(output, index=False)

    return output.getvalue()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🌡️ VIRTUAL LAB</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">SUHU DAN KALOR</div>',
        unsafe_allow_html=True
    )

    st.markdown("### MENU")

    if st.button("🏠 Beranda", use_container_width=True):
        st.session_state.halaman = "Beranda"

    if st.button("🌡️ Praktikum Suhu", use_container_width=True):
        st.session_state.halaman = "Suhu"

    if st.button("🔥 Praktikum Kalor", use_container_width=True):
        st.session_state.halaman = "Kalor"

    if st.button("⚖️ Praktikum Asas Black", use_container_width=True):
        st.session_state.halaman = "Black"

    if st.button("💧 Praktikum Perubahan Wujud", use_container_width=True):
        st.session_state.halaman = "Wujud"

    st.markdown("---")

    if st.button("📋 Hasil Praktikum Saya", use_container_width=True):
        st.session_state.halaman = "Hasil"

    st.markdown("---")

    st.markdown("""
    <div style="
        background:rgba(255,255,255,0.08);
        padding:15px;
        border-radius:12px;
        text-align:center;
        font-size:12px;">
        <b>VIRTUAL LAB FISIKA</b><br><br>
        Suhu dan Kalor
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# BERANDA
# ============================================================

if st.session_state.halaman == "Beranda":

    st.markdown("""
    <div class="hero">
        <h1>🌡️ VIRTUAL LAB SUHU DAN KALOR</h1>

        <p>
        Media pembelajaran praktikum fisika berbasis web
        yang memungkinkan peserta didik melakukan simulasi,
        mengamati hasil, melakukan analisis, dan menyusun
        kesimpulan.
        </p>

        <p>
        <b>Materi:</b> Suhu, Kalor, Asas Black, dan Perubahan Wujud
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🎯 Tujuan Pembelajaran</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    Setelah melakukan kegiatan praktikum menggunakan
    Virtual Lab, peserta didik diharapkan mampu:

    <ol>
    <li>Menjelaskan konsep suhu dan pengukurannya.</li>
    <li>Mengonversi suhu ke dalam beberapa skala.</li>
    <li>Menganalisis hubungan kalor, massa, kalor jenis,
    dan perubahan suhu.</li>
    <li>Menjelaskan perpindahan kalor berdasarkan Asas Black.</li>
    <li>Mengidentifikasi proses perubahan wujud zat.</li>
    <li>Menganalisis data hasil simulasi.</li>
    <li>Menyusun kesimpulan berdasarkan hasil praktikum.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🧪 Pilih Praktikum</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown("""
        <div class="card">
        <h3>🌡️ Suhu</h3>
        <p>
        Mengamati hubungan antar skala suhu
        melalui simulasi termometer.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Mulai Praktikum",
            key="home_suhu",
            use_container_width=True
        ):
            st.session_state.halaman = "Suhu"

    with c2:

        st.markdown("""
        <div class="card">
        <h3>🔥 Kalor</h3>
        <p>
        Menyelidiki pengaruh massa,
        kalor jenis, dan perubahan suhu.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Mulai Praktikum",
            key="home_kalor",
            use_container_width=True
        ):
            st.session_state.halaman = "Kalor"

    with c3:

        st.markdown("""
        <div class="card">
        <h3>⚖️ Asas Black</h3>
        <p>
        Mengamati perpindahan kalor antara
        benda panas dan benda dingin.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Mulai Praktikum",
            key="home_black",
            use_container_width=True
        ):
            st.session_state.halaman = "Black"

    with c4:

        st.markdown("""
        <div class="card">
        <h3>💧 Perubahan Wujud</h3>
        <p>
        Mengamati perubahan wujud zat
        akibat pemberian dan pelepasan kalor.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Mulai Praktikum",
            key="home_wujud",
            use_container_width=True
        ):
            st.session_state.halaman = "Wujud"


# ============================================================
# PRAKTIKUM SUHU
# ============================================================

elif st.session_state.halaman == "Suhu":

    st.markdown("""
    <div class="hero">
        <h1>🌡️ PRAKTIKUM SUHU</h1>
        <p>
        Pengamatan dan konversi skala suhu.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # IDENTITAS

    st.markdown(
        '<div class="section-title">👤 Identitas Praktikan</div>',
        unsafe_allow_html=True
    )

    nama_suhu = st.text_input(
        "Nama peserta didik",
        key="nama_suhu"
    )

    kelas_suhu = st.text_input(
        "Kelas",
        key="kelas_suhu"
    )

    # TUJUAN

    st.markdown("""
    <div class="praktikum-box">

    <div class="praktikum-title">
    🎯 Tujuan Praktikum
    </div>

    <div class="objective">

    Setelah melakukan praktikum, peserta didik mampu
    mengamati hubungan antara skala Celsius, Fahrenheit,
    Kelvin, dan Reamur serta melakukan konversi suhu.

    </div>

    </div>
    """, unsafe_allow_html=True)

    # DASAR TEORI

    st.markdown("""
    <div class="praktikum-box">

    <div class="praktikum-title">
    📖 Dasar Teori Singkat
    </div>

    Suhu merupakan besaran yang menyatakan derajat
    panas atau dinginnya suatu benda. Suhu dapat dinyatakan
    menggunakan beberapa skala, antara lain Celsius,
    Fahrenheit, Kelvin, dan Reamur.

    </div>
    """, unsafe_allow_html=True)

    # LANGKAH

    st.markdown("""
    <div class="praktikum-box">

    <div class="praktikum-title">
    📋 Langkah Praktikum
    </div>

    <ol>
    <li>Atur nilai suhu Celsius.</li>
    <li>Amati perubahan pada termometer.</li>
    <li>Amati hasil konversi pada skala lainnya.</li>
    <li>Catat hasil pengamatan.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    # SIMULASI

    st.markdown(
        '<div class="section-title">🧪 Simulasi Termometer</div>',
        unsafe_allow_html=True
    )

    suhu = st.slider(
        "Geser termometer untuk mengubah suhu",
        -50,
        150,
        25
    )

    fahrenheit = (9 / 5 * suhu) + 32
    kelvin = suhu + 273.15
    reamur = 4 / 5 * suhu

    # GAMBAR TERMOMETER

    fig, ax = plt.subplots(figsize=(3, 5))

    ax.set_xlim(0, 1)
    ax.set_ylim(-50, 150)

    ax.bar(
        0.5,
        suhu + 50,
        bottom=-50,
        width=0.12
    )

    ax.scatter(
        [0.5],
        [-50],
        s=1000,
        zorder=3
    )

    ax.set_ylabel("Suhu (°C)")
    ax.set_xticks([])
    ax.set_title("Simulasi Termometer")

    st.pyplot(fig)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Celsius", f"{suhu:.1f} °C")
    col2.metric("Fahrenheit", f"{fahrenheit:.1f} °F")
    col3.metric("Kelvin", f"{kelvin:.1f} K")
    col4.metric("Reamur", f"{reamur:.1f} °R")

    # TABEL

    st.markdown("### 📊 Tabel Hasil Pengamatan")

    tabel_suhu = pd.DataFrame({
        "Skala": [
            "Celsius",
            "Fahrenheit",
            "Kelvin",
            "Reamur"
        ],
        "Nilai": [
            suhu,
            round(fahrenheit, 2),
            round(kelvin, 2),
            round(reamur, 2)
        ]
    })

    st.dataframe(
        tabel_suhu,
        use_container_width=True,
        hide_index=True
    )

    # ANALISIS OTOMATIS

    st.markdown("### 🔎 Analisis Hasil")

    st.markdown(f"""
    <div class="analysis">

    Berdasarkan simulasi, ketika suhu berada pada
    <b>{suhu} °C</b>, diperoleh:

    <ul>
    <li>Fahrenheit = <b>{fahrenheit:.2f} °F</b></li>
    <li>Kelvin = <b>{kelvin:.2f} K</b></li>
    <li>Reamur = <b>{reamur:.2f} °R</b></li>
    </ul>

    Ketika nilai Celsius dinaikkan, nilai pada skala
    Fahrenheit, Kelvin, dan Reamur juga meningkat.

    Hal tersebut menunjukkan bahwa skala-skala suhu
    memiliki hubungan matematis satu sama lain.

    </div>
    """, unsafe_allow_html=True)

    # PERTANYAAN

    st.markdown("### ❓ Pertanyaan Analisis")

    jawaban1 = st.text_area(
        "1. Apa yang dimaksud dengan suhu?",
        key="suhu_j1"
    )

    jawaban2 = st.text_area(
        "2. Apa yang terjadi pada nilai Fahrenheit ketika suhu Celsius dinaikkan?",
        key="suhu_j2"
    )

    jawaban3 = st.text_area(
        "3. Bagaimana hubungan Celsius dengan Kelvin?",
        key="suhu_j3"
    )

    jawaban4 = st.text_area(
        "4. Apa kesimpulan dari praktikum ini?",
        key="suhu_j4"
    )

    kesimpulan_suhu = st.text_area(
        "📝 Kesimpulan Praktikum",
        height=150,
        key="kesimpulan_suhu"
    )

    # KIRIM

    if st.button(
        "📤 Kumpulkan Hasil Praktikum",
        key="kirim_suhu",
        use_container_width=True
    ):

        if nama_suhu.strip() == "":
            st.warning("Silakan isi nama terlebih dahulu.")

        else:

            data = {
                "Waktu": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Nama": nama_suhu,
                "Kelas": kelas_suhu,
                "Praktikum": "Suhu",
                "Data Utama": f"{suhu} °C",
                "Hasil": f"F={fahrenheit:.2f}°F; K={kelvin:.2f}K; R={reamur:.2f}°R",
                "Pertanyaan 1": jawaban1,
                "Pertanyaan 2": jawaban2,
                "Pertanyaan 3": jawaban3,
                "Pertanyaan 4": jawaban4,
                "Kesimpulan": kesimpulan_suhu
            }

            simpan_hasil(data)

            st.success(
                "Hasil praktikum berhasil dikumpulkan!"
            )


# ============================================================
# PRAKTIKUM KALOR
# ============================================================

elif st.session_state.halaman == "Kalor":

    st.markdown("""
    <div class="hero">
        <h1>🔥 PRAKTIKUM KALOR</h1>
        <p>
        Menyelidiki hubungan massa, kalor jenis,
        perubahan suhu, dan kalor.
        </p>
    </div>
    """, unsafe_allow_html=True)

    nama_kalor = st.text_input(
        "Nama peserta didik",
        key="nama_kalor"
    )

    kelas_kalor = st.text_input(
        "Kelas",
        key="kelas_kalor"
    )

    st.markdown("""
    <div class="praktikum-box">

    <div class="praktikum-title">
    🎯 Tujuan Praktikum
    </div>

    <div class="objective">

    Peserta didik mampu menganalisis hubungan
    massa, kalor jenis, perubahan suhu, dan kalor
    yang diterima atau dilepaskan benda.

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="praktikum-box">

    <div class="praktikum-title">
    📋 Langkah Praktikum
    </div>

    <ol>
    <li>Atur massa benda.</li>
    <li>Atur kalor jenis benda.</li>
    <li>Tentukan suhu awal.</li>
    <li>Atur suhu akhir.</li>
    <li>Amati besar kalor.</li>
    <li>Ubah salah satu variabel dan amati perubahan hasil.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧪 Simulasi Kalor")

    c1, c2, c3 = st.columns(3)

    with c1:

        massa = st.slider(
            "Massa benda (kg)",
            0.1,
            10.0,
            1.0,
            0.1
        )

    with c2:

        kalor_jenis = st.slider(
            "Kalor jenis (J/kg°C)",
            100.0,
            5000.0,
            4200.0,
            100.0
        )

    with c3:

        suhu_awal = st.slider(
            "Suhu awal (°C)",
            -20.0,
            100.0,
            25.0,
            1.0
        )

    suhu_akhir = st.slider(
        "Suhu akhir (°C)",
        -20.0,
        200.0,
        75.0,
        1.0
    )

    delta_T = suhu_akhir - suhu_awal

    Q = massa * kalor_jenis * delta_T

    # VISUAL

    fig, ax = plt.subplots(figsize=(8, 4))

    suhu_data = [suhu_awal, suhu_akhir]

    ax.plot(
        ["Awal", "Akhir"],
        suhu_data,
        marker="o",
        linewidth=3
    )

    ax.set_ylabel("Suhu (°C)")
    ax.set_title("Perubahan Suhu Benda")
    ax.grid(alpha=0.3)

    st.pyplot(fig)

    a, b = st.columns(2)

    a.metric(
        "Perubahan Suhu",
        f"{delta_T:.2f} °C"
    )

    b.metric(
        "Kalor",
        f"{Q:,.2f} J"
    )

    # ANALISIS OTOMATIS

    st.markdown("### 🔎 Analisis Hasil")

    if delta_T > 0:
        kondisi = "Benda menerima kalor."
    elif delta_T < 0:
        kondisi = "Benda melepaskan kalor."
    else:
        kondisi = "Tidak terjadi perubahan suhu."

    st.markdown(f"""
    <div class="analysis">

    Berdasarkan simulasi:

    <ul>
    <li>Massa = <b>{massa:.2f} kg</b></li>
    <li>Kalor jenis = <b>{kalor_jenis:.0f} J/kg°C</b></li>
    <li>Perubahan suhu = <b>{delta_T:.2f} °C</b></li>
    <li>Kalor = <b>{Q:,.2f} J</b></li>
    </ul>

    {kondisi}

    Berdasarkan persamaan Q = m × c × ΔT,
    besar kalor dipengaruhi oleh massa, kalor jenis,
    dan perubahan suhu.

    </div>
    """, unsafe_allow_html=True)

    # TABEL

    st.markdown("### 📊 Tabel Hasil Pengamatan")

    tabel_kalor = pd.DataFrame({
        "Besaran": [
            "Massa",
            "Kalor jenis",
            "Suhu awal",
            "Suhu akhir",
            "Perubahan suhu",
            "Kalor"
        ],
        "Nilai": [
            f"{massa:.2f} kg",
            f"{kalor_jenis:.0f} J/kg°C",
            f"{suhu_awal:.2f} °C",
            f"{suhu_akhir:.2f} °C",
            f"{delta_T:.2f} °C",
            f"{Q:,.2f} J"
        ]
    })

    st.dataframe(
        tabel_kalor,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### ❓ Pertanyaan Analisis")

    j1 = st.text_area(
        "1. Apa yang terjadi terhadap kalor jika perubahan suhu diperbesar?",
        key="kalor_j1"
    )

    j2 = st.text_area(
        "2. Bagaimana pengaruh massa terhadap besar kalor?",
        key="kalor_j2"
    )

    j3 = st.text_area(
        "3. Bagaimana pengaruh kalor jenis terhadap kalor?",
        key="kalor_j3"
    )

    j4 = st.text_area(
        "4. Jelaskan hubungan Q, m, c, dan ΔT.",
        key="kalor_j4"
    )

    kesimpulan = st.text_area(
        "📝 Kesimpulan Praktikum",
        height=150,
        key="kalor_kesimpulan"
    )

    if st.button(
        "📤 Kumpulkan Hasil Praktikum",
        key="kirim_kalor",
        use_container_width=True
    ):

        if nama_kalor.strip() == "":
            st.warning("Silakan isi nama terlebih dahulu.")

        else:

            data = {
                "Waktu": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Nama": nama_kalor,
                "Kelas": kelas_kalor,
                "Praktikum": "Kalor",
                "Data Utama": f"Massa {massa} kg",
                "Hasil": f"ΔT={delta_T:.2f}°C; Q={Q:.2f} J",
                "Pertanyaan 1": j1,
                "Pertanyaan 2": j2,
                "Pertanyaan 3": j3,
                "Pertanyaan 4": j4,
                "Kesimpulan": kesimpulan
            }

            simpan_hasil(data)

            st.success(
                "Hasil praktikum berhasil dikumpulkan!"
            )


# ============================================================
# PRAKTIKUM ASAS BLACK
# ============================================================

elif st.session_state.halaman == "Black":

    st.markdown("""
    <div class="hero">
        <h1>⚖️ PRAKTIKUM ASAS BLACK</h1>
        <p>
        Mengamati perpindahan kalor antara benda panas
        dan benda dingin sampai mencapai kesetimbangan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    nama_black = st.text_input(
        "Nama peserta didik",
        key="nama_black"
    )

    kelas_black = st.text_input(
        "Kelas",
        key="kelas_black"
    )

    st.markdown("""
    <div class="praktikum-box">

    <div class="praktikum-title">
    🎯 Tujuan Praktikum
    </div>

    <div class="objective">

    Peserta didik mampu menganalisis perpindahan
    kalor antara benda panas dan benda dingin
    serta menentukan suhu kesetimbangan.

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="praktikum-box">

    <div class="praktikum-title">
    📋 Langkah Praktikum
    </div>

    <ol>
    <li>Tentukan suhu benda panas.</li>
    <li>Tentukan suhu benda dingin.</li>
    <li>Tentukan massa masing-masing benda.</li>
    <li>Amati suhu kesetimbangan.</li>
    <li>Bandingkan kalor yang dilepas dan diterima.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🔥 Benda Panas")

        m1 = st.slider(
            "Massa benda panas (kg)",
            0.1,
            5.0,
            1.0,
            0.1,
            key="black_m1"
        )

        T1 = st.slider(
            "Suhu benda panas (°C)",
            30.0,
            150.0,
            80.0,
            1.0,
            key="black_T1"
        )

        c1 = st.number_input(
            "Kalor jenis benda panas",
            min_value=100.0,
            value=4200.0,
            key="black_c1"
        )

    with col2:

        st.markdown("### ❄️ Benda Dingin")

        m2 = st.slider(
            "Massa benda dingin (kg)",
            0.1,
            5.0,
            1.0,
            0.1,
            key="black_m2"
        )

        T2 = st.slider(
            "Suhu benda dingin (°C)",
            0.0,
            70.0,
            20.0,
            1.0,
            key="black_T2"
        )

        c2 = st.number_input(
            "Kalor jenis benda dingin",
            min_value=100.0,
            value=4200.0,
            key="black_c2"
        )

    Te = (
        (m1 * c1 * T1) +
        (m2 * c2 * T2)
    ) / (
        (m1 * c1) +
        (m2 * c2)
    )

    Q_lepas = m1 * c1 * (T1 - Te)
    Q_terima = m2 * c2 * (Te - T2)

    # GAMBAR PROSES

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        ["Benda Panas", "Kesetimbangan", "Benda Dingin"],
        [T1, Te, T2]
    )

    ax.set_ylabel("Suhu (°C)")
    ax.set_title("Perubahan Suhu pada Asas Black")

    st.pyplot(fig)

    a, b, c = st.columns(3)

    a.metric(
        "Suhu Panas",
        f"{T1:.2f} °C"
    )

    b.metric(
        "Suhu Kesetimbangan",
        f"{Te:.2f} °C"
    )

    c.metric(
        "Suhu Dingin",
        f"{T2:.2f} °C"
    )

    st.markdown("### 📊 Hasil Perhitungan")

    r1, r2 = st.columns(2)

    r1.metric(
        "Kalor Dilepas",
        f"{Q_lepas:,.2f} J"
    )

    r2.metric(
        "Kalor Diterima",
        f"{Q_terima:,.2f} J"
    )

    # ANALISIS

    st.markdown("### 🔎 Analisis Hasil")

    st.markdown(f"""
    <div class="analysis">

    Benda panas memiliki suhu awal
    <b>{T1:.2f} °C</b>, sedangkan benda dingin
    memiliki suhu awal <b>{T2:.2f} °C</b>.

    Setelah terjadi pertukaran kalor,
    suhu kesetimbangan diperoleh sebesar
    <b>{Te:.2f} °C</b>.

    Benda panas mengalami penurunan suhu,
    sedangkan benda dingin mengalami kenaikan suhu.

    Secara ideal:

    <b>Kalor yang dilepas ≈ Kalor yang diterima.</b>

    Hal tersebut sesuai dengan prinsip Asas Black.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Tabel Pengamatan")

    data_black = pd.DataFrame({
        "Besaran": [
            "Suhu benda panas",
            "Suhu benda dingin",
            "Suhu kesetimbangan",
            "Kalor dilepas",
            "Kalor diterima"
        ],
        "Nilai": [
            f"{T1:.2f} °C",
            f"{T2:.2f} °C",
            f"{Te:.2f} °C",
            f"{Q_lepas:,.2f} J",
            f"{Q_terima:,.2f} J"
        ]
    })

    st.dataframe(
        data_black,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### ❓ Pertanyaan Analisis")

    j1 = st.text_area(
        "1. Mengapa suhu benda panas menurun?",
        key="black_j1"
    )

    j2 = st.text_area(
        "2. Mengapa suhu benda dingin meningkat?",
        key="black_j2"
    )

    j3 = st.text_area(
        "3. Apa yang dimaksud dengan suhu kesetimbangan?",
        key="black_j3"
    )

    j4 = st.text_area(
        "4. Bagaimana hubungan kalor yang dilepas dan kalor yang diterima?",
        key="black_j4"
    )

    kesimpulan = st.text_area(
        "📝 Kesimpulan Praktikum",
        height=150,
        key="black_kesimpulan"
    )

    if st.button(
        "📤 Kumpulkan Hasil Praktikum",
        key="kirim_black",
        use_container_width=True
    ):

        if nama_black.strip() == "":
            st.warning("Silakan isi nama terlebih dahulu.")

        else:

            data = {
                "Waktu": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Nama": nama_black,
                "Kelas": kelas_black,
                "Praktikum": "Asas Black",
                "Data Utama": f"T panas={T1}°C; T dingin={T2}°C",
                "Hasil": f"T kesetimbangan={Te:.2f}°C",
                "Pertanyaan 1": j1,
                "Pertanyaan 2": j2,
                "Pertanyaan 3": j3,
                "Pertanyaan 4": j4,
                "Kesimpulan": kesimpulan
            }

            simpan_hasil(data)

            st.success(
                "Hasil praktikum berhasil dikumpulkan!"
            )


# ============================================================
# PRAKTIKUM PERUBAHAN WUJUD
# ============================================================

elif st.session_state.halaman == "Wujud":

    st.markdown("""
    <div class="hero">
        <h1>💧 PRAKTIKUM PERUBAHAN WUJUD</h1>
        <p>
        Mengamati perubahan wujud zat akibat
        pemberian atau pelepasan kalor.
        </p>
    </div>
    """, unsafe_allow_html=True)

    nama_wujud = st.text_input(
        "Nama peserta didik",
        key="nama_wujud"
    )

    kelas_wujud = st.text_input(
        "Kelas",
        key="kelas_wujud"
    )

    st.markdown("""
    <div class="praktikum-box">

    <div class="praktikum-title">
    🎯 Tujuan Praktikum
    </div>

    <div class="objective">

    Peserta didik mampu mengidentifikasi perubahan
    wujud zat serta menjelaskan hubungan antara
    kalor dan perubahan wujud.

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="praktikum-box">

    <div class="praktikum-title">
    📋 Langkah Praktikum
    </div>

    <ol>
    <li>Pilih jenis perubahan wujud.</li>
    <li>Atur jumlah kalor.</li>
    <li>Amati keadaan partikel.</li>
    <li>Amati perubahan suhu.</li>
    <li>Catat hasil pengamatan.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    proses = st.selectbox(
        "Pilih proses perubahan wujud",
        [
            "Mencair",
            "Membeku",
            "Menguap",
            "Mengembun",
            "Menyublim",
            "Mengkristal"
        ]
    )

    info = {

        "Mencair": {
            "awal": "Padat",
            "akhir": "Cair",
            "arah": "Menerima kalor",
            "contoh": "Es berubah menjadi air."
        },

        "Membeku": {
            "awal": "Cair",
            "akhir": "Padat",
            "arah": "Melepaskan kalor",
            "contoh": "Air berubah menjadi es."
        },

        "Menguap": {
            "awal": "Cair",
            "akhir": "Gas",
            "arah": "Menerima kalor",
            "contoh": "Air berubah menjadi uap."
        },

        "Mengembun": {
            "awal": "Gas",
            "akhir": "Cair",
            "arah": "Melepaskan kalor",
            "contoh": "Uap berubah menjadi titik air."
        },

        "Menyublim": {
            "awal": "Padat",
            "akhir": "Gas",
            "arah": "Menerima kalor",
            "contoh": "Kapur barus berubah menjadi gas."
        },

        "Mengkristal": {
            "awal": "Gas",
            "akhir": "Padat",
            "arah": "Melepaskan kalor",
            "contoh": "Gas berubah langsung menjadi padat."
        }
    }

    data_proses = info[proses]

    st.markdown(f"""
    <div class="card" style="text-align:center;">

    <h2>{data_proses['awal']} → {data_proses['akhir']}</h2>

    <h3>{proses}</h3>

    <p><b>{data_proses['arah']}</b></p>

    <p>{data_proses['contoh']}</p>

    </div>
    """, unsafe_allow_html=True)

    # ========================================================
    # SIMULASI PARTIKEL
    # ========================================================

    st.markdown("### 🧪 Simulasi Partikel Zat")

    energi = st.slider(
        "Atur energi/kalor",
        0,
        100,
        50
    )

    if proses in ["Mencair", "Menguap", "Menyublim"]:

        kerapatan = max(4, 16 - int(energi / 8))

    else:

        kerapatan = min(16, 5 + int(energi / 8))

    np.random.seed(10)

    jumlah_partikel = 40

    x = np.random.rand(jumlah_partikel)
    y = np.random.rand(jumlah_partikel)

    if proses in ["Mencair", "Menguap", "Menyublim"]:

        x = x * (0.6 + energi / 200)
        y = y * (0.6 + energi / 200)

    else:

        x = 0.2 + x * 0.6
        y = 0.2 + y * 0.6

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.scatter(
        x,
        y,
        s=100
    )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_title(
        f"Visualisasi Partikel — {proses}"
    )

    st.pyplot(fig)

    # ENERGI

    massa = st.slider(
        "Massa zat (kg)",
        0.1,
        5.0,
        1.0,
        0.1
    )

    kalor_laten = st.number_input(
        "Kalor laten (J/kg)",
        min_value=1000.0,
        value=334000.0,
        step=1000.0
    )

    Q = massa * kalor_laten

    st.metric(
        "Energi perubahan wujud",
        f"{Q:,.2f} J"
    )

    # ANALISIS

    st.markdown("### 🔎 Analisis Hasil")

    if energi < 30:

        analisis = """
        Energi yang diberikan masih relatif kecil.
        Partikel cenderung lebih berdekatan dan
        gerakannya lebih terbatas.
        """

    elif energi < 70:

        analisis = """
        Energi berada pada tingkat sedang.
        Jarak antarpartikel mulai berubah dan
        gerakan partikel menjadi lebih bebas.
        """

    else:

        analisis = """
        Energi tinggi menyebabkan gerakan partikel
        semakin bebas dan jarak antarpartikel
        cenderung semakin besar.
        """

    st.markdown(
        f"""
        <div class="analysis">

        <b>Hasil analisis:</b><br><br>

        Proses yang dipilih adalah
        <b>{proses}</b>.

        Perubahan yang terjadi adalah
        <b>{data_proses['awal']} → {data_proses['akhir']}</b>.

        Proses ini
        <b>{data_proses['arah'].lower()}</b>.

        {analisis}

        </div>
        """,
        unsafe_allow_html=True
    )

    # PERTANYAAN

    st.markdown("### ❓ Pertanyaan Analisis")

    j1 = st.text_area(
        "1. Apa yang dimaksud dengan perubahan wujud?",
        key="wujud_j1"
    )

    j2 = st.text_area(
        "2. Perubahan wujud apa saja yang membutuhkan kalor?",
        key="wujud_j2"
    )

    j3 = st.text_area(
        "3. Perubahan wujud apa saja yang melepaskan kalor?",
        key="wujud_j3"
    )

    j4 = st.text_area(
        "4. Bagaimana pengaruh energi terhadap gerak partikel?",
        key="wujud_j4"
    )

    kesimpulan = st.text_area(
        "📝 Kesimpulan Praktikum",
        height=150,
        key="wujud_kesimpulan"
    )

    if st.button(
        "📤 Kumpulkan Hasil Praktikum",
        key="kirim_wujud",
        use_container_width=True
    ):

        if nama_wujud.strip() == "":
            st.warning("Silakan isi nama terlebih dahulu.")

        else:

            data = {
                "Waktu": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Nama": nama_wujud,
                "Kelas": kelas_wujud,
                "Praktikum": "Perubahan Wujud",
                "Data Utama": proses,
                "Hasil": f"Energi={Q:.2f} J; Energi simulasi={energi}",
                "Pertanyaan 1": j1,
                "Pertanyaan 2": j2,
                "Pertanyaan 3": j3,
                "Pertanyaan 4": j4,
                "Kesimpulan": kesimpulan
            }

            simpan_hasil(data)

            st.success(
                "Hasil praktikum berhasil dikumpulkan!"
            )


# ============================================================
# HALAMAN HASIL PRAKTIKUM
# ============================================================

elif st.session_state.halaman == "Hasil":

    st.markdown("""
    <div class="hero">
        <h1>📋 HASIL PRAKTIKUM</h1>
        <p>
        Lihat dan simpan hasil praktikum yang telah dikumpulkan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.hasil_praktikum:

        st.info(
            "Belum ada hasil praktikum yang dikumpulkan."
        )

    else:

        st.success(
            f"{len(st.session_state.hasil_praktikum)} hasil praktikum telah dikumpulkan."
        )

        df = pd.DataFrame(
            st.session_state.hasil_praktikum
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### 📥 Simpan Hasil")

        csv = buat_csv()

        st.download_button(
            label="⬇️ Download Hasil Praktikum (CSV)",
            data=csv,
            file_name="hasil_praktikum_suhu_kalor.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.markdown("""
        <div class="praktikum-box">

        <div class="praktikum-title">
        ℹ️ Keterangan
        </div>

        File CSV berisi nama peserta didik,
        kelas, waktu pengumpulan, data praktikum,
        jawaban pertanyaan, dan kesimpulan.

        File tersebut dapat dibuka menggunakan
        Microsoft Excel atau Google Sheets.

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

<b>VIRTUAL LAB SUHU DAN KALOR</b><br>

Media Pembelajaran Praktikum Fisika Berbasis Web<br><br>

Suhu • Kalor • Asas Black • Perubahan Wujud

</div>
""", unsafe_allow_html=True)
