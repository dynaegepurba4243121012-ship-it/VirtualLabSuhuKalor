import streamlit as st
import pandas as pd

# =========================================================
# KONFIGURASI
# =========================================================

st.set_page_config(
    page_title="Virtual Lab Suhu dan Kalor",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: #f5f7fb;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #071a35, #0c315d);
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
    background: linear-gradient(135deg, #083b73, #1371bd);
    color: white;
    border-radius: 24px;
    padding: 38px;
    margin-bottom: 25px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.10);
}

.hero h1 {
    font-size: 36px;
    font-weight: 800;
}

.hero p {
    font-size: 15px;
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

/* JUDUL */
.section-title {
    color: #123b68;
    font-size: 25px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* LKPD */
.lkpd {
    background: white;
    border-radius: 18px;
    padding: 28px;
    border: 1px solid #dfe6ef;
    margin-bottom: 22px;
}

.lkpd-title {
    font-size: 22px;
    font-weight: 700;
    color: #123b68;
    margin-bottom: 15px;
}

.objective {
    background: #eef7ff;
    border-left: 5px solid #1874c9;
    padding: 18px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.question {
    background: #fafbfc;
    border: 1px solid #e2e7ee;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 12px;
}

/* HASIL */
.result {
    background: #edf7ff;
    border-left: 5px solid #1371bd;
    padding: 20px;
    border-radius: 12px;
}

.big-number {
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


# =========================================================
# SESSION STATE
# =========================================================

if "halaman" not in st.session_state:
    st.session_state.halaman = "Beranda"


# =========================================================
# SIDEBAR
# =========================================================

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

    if st.button("📖 LKPD Suhu", use_container_width=True):
        st.session_state.halaman = "Suhu"

    if st.button("🔥 LKPD Kalor", use_container_width=True):
        st.session_state.halaman = "Kalor"

    if st.button("⚖️ LKPD Asas Black", use_container_width=True):
        st.session_state.halaman = "Black"

    if st.button("💧 LKPD Perubahan Wujud", use_container_width=True):
        st.session_state.halaman = "Wujud"

    st.markdown("---")

    st.markdown("""
    <div style="
        background:rgba(255,255,255,0.08);
        padding:15px;
        border-radius:12px;
        text-align:center;
        font-size:12px;">
        <b>KELOMPOK 8</b><br><br>
        Praktikum Fisika SMA
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# BERANDA
# =========================================================

if st.session_state.halaman == "Beranda":

    st.markdown("""
    <div class="hero">
        <h1>🌡️ VIRTUAL LAB SUHU DAN KALOR</h1>
        <p>
        Media pembelajaran praktikum fisika berbasis web
        dalam bentuk LKPD digital interaktif.
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

    Setelah melakukan kegiatan pada Virtual Lab ini, peserta didik
    diharapkan mampu:

    <ol>
    <li>Menjelaskan konsep suhu dan pengukurannya.</li>
    <li>Mengonversi nilai suhu ke berbagai skala.</li>
    <li>Menjelaskan hubungan kalor, massa, kalor jenis, dan perubahan suhu.</li>
    <li>Menganalisis perpindahan kalor menggunakan Asas Black.</li>
    <li>Mengidentifikasi berbagai perubahan wujud zat.</li>
    <li>Menganalisis hasil simulasi melalui tabel dan pertanyaan.</li>
    <li>Menyusun kesimpulan berdasarkan hasil percobaan.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🧪 Pilih Kegiatan LKPD</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>🌡️ Suhu</h3>
        <p>
        Mengamati dan mengonversi suhu pada
        berbagai skala termometer.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Mulai LKPD", key="btn1",
                     use_container_width=True):
            st.session_state.halaman = "Suhu"

    with c2:
        st.markdown("""
        <div class="card">
        <h3>🔥 Kalor</h3>
        <p>
        Menyelidiki pengaruh massa, kalor jenis,
        dan perubahan suhu terhadap kalor.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Mulai LKPD", key="btn2",
                     use_container_width=True):
            st.session_state.halaman = "Kalor"

    with c3:
        st.markdown("""
        <div class="card">
        <h3>⚖️ Asas Black</h3>
        <p>
        Menyelidiki perpindahan kalor antara
        benda panas dan benda dingin.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Mulai LKPD", key="btn3",
                     use_container_width=True):
            st.session_state.halaman = "Black"

    with c4:
        st.markdown("""
        <div class="card">
        <h3>💧 Perubahan Wujud</h3>
        <p>
        Mengidentifikasi perubahan wujud zat
        akibat pemberian atau pelepasan kalor.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Mulai LKPD", key="btn4",
                     use_container_width=True):
            st.session_state.halaman = "Wujud"


# =========================================================
# LKPD SUHU
# =========================================================

elif st.session_state.halaman == "Suhu":

    st.markdown("""
    <div class="hero">
        <h1>🌡️ LKPD DIGITAL — PENGUKURAN SUHU</h1>
        <p>
        Simulasi pengukuran dan konversi skala suhu.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # TUJUAN
    st.markdown("""
    <div class="lkpd">
    <div class="lkpd-title">🎯 Tujuan Pembelajaran</div>

    <div class="objective">
    Peserta didik mampu menjelaskan pengertian suhu,
    melakukan konversi skala suhu, serta menganalisis
    hasil pengukuran melalui simulasi.
    </div>
    </div>
    """, unsafe_allow_html=True)

    # PETUNJUK
    st.markdown("""
    <div class="lkpd">
    <div class="lkpd-title">📋 Petunjuk Percobaan</div>

    <ol>
    <li>Geser nilai suhu pada simulasi.</li>
    <li>Amati perubahan nilai pada setiap skala.</li>
    <li>Catat hasil pengamatan.</li>
    <li>Jawab pertanyaan pada bagian analisis.</li>
    <li>Buat kesimpulan berdasarkan hasil percobaan.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

    # SIMULASI
    st.markdown(
        '<div class="section-title">🧪 Simulasi Pengukuran</div>',
        unsafe_allow_html=True
    )

    suhu = st.slider(
        "Atur suhu Celsius",
        -50,
        150,
        25
    )

    fahrenheit = (9 / 5 * suhu) + 32
    kelvin = suhu + 273.15
    reamur = 4 / 5 * suhu

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Celsius", f"{suhu} °C")
    col2.metric("Fahrenheit", f"{fahrenheit:.2f} °F")
    col3.metric("Kelvin", f"{kelvin:.2f} K")
    col4.metric("Reamur", f"{reamur:.2f} °R")

    # TABEL
    st.markdown("### 📊 Tabel Hasil Pengamatan")

    data = pd.DataFrame({
        "Skala": [
            "Celsius",
            "Fahrenheit",
            "Kelvin",
            "Reamur"
        ],
        "Hasil": [
            f"{suhu:.2f}",
            f"{fahrenheit:.2f}",
            f"{kelvin:.2f}",
            f"{reamur:.2f}"
        ]
    })

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

    # PERTANYAAN
    st.markdown("""
    <div class="lkpd">
    <div class="lkpd-title">❓ Pertanyaan Analisis</div>
    </div>
    """, unsafe_allow_html=True)

    q1 = st.text_area(
        "1. Apa yang dimaksud dengan suhu?"
    )

    q2 = st.text_area(
        "2. Bagaimana hubungan antara skala Celsius dan Fahrenheit?"
    )

    q3 = st.text_area(
        "3. Jika suhu dinaikkan, bagaimana perubahan nilai Kelvin?"
    )

    q4 = st.text_area(
        "4. Apa yang dapat kamu simpulkan dari hasil simulasi?"
    )

    st.markdown("### 📝 Kesimpulan")

    kesimpulan = st.text_area(
        "Tuliskan kesimpulan percobaan:",
        height=150
    )

    if st.button("💾 Simpan Jawaban LKPD", key="simpan_suhu"):
        st.success("Jawaban LKPD telah dicatat pada halaman ini.")


# =========================================================
# LKPD KALOR
# =========================================================

elif st.session_state.halaman == "Kalor":

    st.markdown("""
    <div class="hero">
        <h1>🔥 LKPD DIGITAL — KALOR</h1>
        <p>
        Menyelidiki hubungan massa, kalor jenis,
        perubahan suhu, dan kalor.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="lkpd">

    <div class="lkpd-title">🎯 Tujuan Pembelajaran</div>

    <div class="objective">
    Peserta didik mampu menganalisis hubungan massa,
    kalor jenis, perubahan suhu, dan kalor yang diterima
    atau dilepaskan oleh suatu benda.
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="lkpd">

    <div class="lkpd-title">📋 Langkah Percobaan</div>

    <ol>
    <li>Tentukan massa benda.</li>
    <li>Tentukan kalor jenis benda.</li>
    <li>Tentukan suhu awal.</li>
    <li>Atur suhu akhir.</li>
    <li>Amati nilai kalor yang diperoleh.</li>
    <li>Ubah salah satu variabel dan bandingkan hasilnya.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🧪 Simulasi Kalor</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        massa = st.number_input(
            "Massa (kg)",
            min_value=0.1,
            value=1.0,
            step=0.1
        )

    with c2:
        kalor_jenis = st.number_input(
            "Kalor jenis (J/kg°C)",
            min_value=100.0,
            value=4200.0,
            step=100.0
        )

    with c3:
        suhu_awal = st.number_input(
            "Suhu awal (°C)",
            value=25.0
        )

    suhu_akhir = st.slider(
        "Suhu akhir (°C)",
        -50.0,
        200.0,
        75.0
    )

    delta_t = suhu_akhir - suhu_awal

    Q = massa * kalor_jenis * delta_t

    st.markdown("### 📊 Hasil Simulasi")

    r1, r2 = st.columns(2)

    r1.metric(
        "Perubahan Suhu",
        f"{delta_t:.2f} °C"
    )

    r2.metric(
        "Kalor",
        f"{Q:,.2f} J"
    )

    st.markdown("### 📋 Tabel Hasil")

    tabel = pd.DataFrame({
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
            f"{kalor_jenis:.2f} J/kg°C",
            f"{suhu_awal:.2f} °C",
            f"{suhu_akhir:.2f} °C",
            f"{delta_t:.2f} °C",
            f"{Q:.2f} J"
        ]
    })

    st.dataframe(
        tabel,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("""
    <div class="lkpd">

    <div class="lkpd-title">❓ Pertanyaan Analisis</div>

    </div>
    """, unsafe_allow_html=True)

    q1 = st.text_area(
        "1. Apa yang terjadi pada kalor jika perubahan suhu diperbesar?",
        key="kalor_q1"
    )

    q2 = st.text_area(
        "2. Bagaimana pengaruh massa benda terhadap kalor?",
        key="kalor_q2"
    )

    q3 = st.text_area(
        "3. Bagaimana pengaruh kalor jenis terhadap kalor?",
        key="kalor_q3"
    )

    q4 = st.text_area(
        "4. Berdasarkan simulasi, apa hubungan Q, m, c, dan ΔT?",
        key="kalor_q4"
    )

    st.markdown("### 📝 Kesimpulan")

    kesimpulan = st.text_area(
        "Tuliskan kesimpulan percobaan:",
        height=150,
        key="kalor_kesimpulan"
    )

    if st.button(
        "💾 Simpan Jawaban LKPD",
        key="simpan_kalor"
    ):
        st.success("Jawaban LKPD telah dicatat.")


# =========================================================
# LKPD ASAS BLACK
# =========================================================

elif st.session_state.halaman == "Black":

    st.markdown("""
    <div class="hero">
        <h1>⚖️ LKPD DIGITAL — ASAS BLACK</h1>
        <p>
        Simulasi pencampuran benda panas dan benda dingin.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="lkpd">

    <div class="lkpd-title">🎯 Tujuan Pembelajaran</div>

    <div class="objective">
    Peserta didik mampu menjelaskan prinsip Asas Black
    dan menentukan suhu kesetimbangan antara dua benda
    yang memiliki suhu berbeda.
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="lkpd">

    <div class="lkpd-title">📋 Langkah Percobaan</div>

    <ol>
    <li>Tentukan massa benda panas.</li>
    <li>Tentukan suhu benda panas.</li>
    <li>Tentukan massa benda dingin.</li>
    <li>Tentukan suhu benda dingin.</li>
    <li>Amati suhu kesetimbangan.</li>
    <li>Bandingkan kalor yang dilepas dan diterima.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🧪 Simulasi Asas Black</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🔥 Benda Panas")

        m1 = st.number_input(
            "Massa benda panas (kg)",
            min_value=0.1,
            value=1.0,
            step=0.1,
            key="m1"
        )

        c1 = st.number_input(
            "Kalor jenis benda panas",
            min_value=100.0,
            value=4200.0,
            step=100.0,
            key="c1"
        )

        T1 = st.number_input(
            "Suhu awal benda panas (°C)",
            value=80.0,
            key="T1"
        )

    with col2:

        st.markdown("### ❄️ Benda Dingin")

        m2 = st.number_input(
            "Massa benda dingin (kg)",
            min_value=0.1,
            value=1.0,
            step=0.1,
            key="m2"
        )

        c2 = st.number_input(
            "Kalor jenis benda dingin",
            min_value=100.0,
            value=4200.0,
            step=100.0,
            key="c2"
        )

        T2 = st.number_input(
            "Suhu awal benda dingin (°C)",
            value=20.0,
            key="T2"
        )

    penyebut = (m1 * c1) + (m2 * c2)

    Te = (
        (m1 * c1 * T1) +
        (m2 * c2 * T2)
    ) / penyebut

    Q_lepas = m1 * c1 * (T1 - Te)
    Q_terima = m2 * c2 * (Te - T2)

    st.markdown("### 📊 Hasil Simulasi")

    a, b, c = st.columns(3)

    a.metric(
        "Suhu Kesetimbangan",
        f"{Te:.2f} °C"
    )

    b.metric(
        "Kalor Dilepas",
        f"{Q_lepas:,.2f} J"
    )

    c.metric(
        "Kalor Diterima",
        f"{Q_terima:,.2f} J"
    )

    st.markdown("### 📋 Tabel Hasil")

    data_black = pd.DataFrame({
        "Besaran": [
            "Suhu benda panas",
            "Suhu benda dingin",
            "Suhu kesetimbangan",
            "Kalor dilepas",
            "Kalor diterima"
        ],
        "Hasil": [
            f"{T1:.2f} °C",
            f"{T2:.2f} °C",
            f"{Te:.2f} °C",
            f"{Q_lepas:.2f} J",
            f"{Q_terima:.2f} J"
        ]
    })

    st.dataframe(
        data_black,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("""
    <div class="lkpd">

    <div class="lkpd-title">❓ Pertanyaan Analisis</div>

    </div>
    """, unsafe_allow_html=True)

    q1 = st.text_area(
        "1. Mengapa benda panas mengalami penurunan suhu?",
        key="black_q1"
    )

    q2 = st.text_area(
        "2. Mengapa benda dingin mengalami kenaikan suhu?",
        key="black_q2"
    )

    q3 = st.text_area(
        "3. Apa yang terjadi pada suhu kedua benda ketika mencapai kesetimbangan?",
        key="black_q3"
    )

    q4 = st.text_area(
        "4. Bagaimana hubungan kalor yang dilepas dengan kalor yang diterima?",
        key="black_q4"
    )

    st.markdown("### 📝 Kesimpulan")

    kesimpulan = st.text_area(
        "Tuliskan kesimpulan percobaan:",
        height=150,
        key="black_kesimpulan"
    )

    if st.button(
        "💾 Simpan Jawaban LKPD",
        key="simpan_black"
    ):
        st.success("Jawaban LKPD telah dicatat.")


# =========================================================
# LKPD PERUBAHAN WUJUD
# =========================================================

elif st.session_state.halaman == "Wujud":

    st.markdown("""
    <div class="hero">
        <h1>💧 LKPD DIGITAL — PERUBAHAN WUJUD</h1>
        <p>
        Mengamati perubahan wujud zat akibat
        pemberian dan pelepasan kalor.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="lkpd">

    <div class="lkpd-title">🎯 Tujuan Pembelajaran</div>

    <div class="objective">
    Peserta didik mampu mengidentifikasi berbagai
    perubahan wujud zat serta menjelaskan hubungan
    antara kalor dan perubahan wujud.
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="lkpd">

    <div class="lkpd-title">📋 Langkah Percobaan</div>

    <ol>
    <li>Pilih salah satu proses perubahan wujud.</li>
    <li>Amati perubahan keadaan zat.</li>
    <li>Amati apakah zat menerima atau melepaskan kalor.</li>
    <li>Catat hasil pengamatan.</li>
    <li>Jawab pertanyaan analisis.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    proses = st.selectbox(
        "Pilih perubahan wujud:",
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
        "Mencair": (
            "🧊 → 💧",
            "Padat → Cair",
            "Menerima kalor",
            "Contoh: es mencair menjadi air."
        ),
        "Membeku": (
            "💧 → 🧊",
            "Cair → Padat",
            "Melepaskan kalor",
            "Contoh: air membeku menjadi es."
        ),
        "Menguap": (
            "💧 → ☁️",
            "Cair → Gas",
            "Menerima kalor",
            "Contoh: air berubah menjadi uap."
        ),
        "Mengembun": (
            "☁️ → 💧",
            "Gas → Cair",
            "Melepaskan kalor",
            "Contoh: uap air menjadi titik air."
        ),
        "Menyublim": (
            "🧊 → ☁️",
            "Padat → Gas",
            "Menerima kalor",
            "Contoh: kapur barus menyublim."
        ),
        "Mengkristal": (
            "☁️ → 🧊",
            "Gas → Padat",
            "Melepaskan kalor",
            "Contoh: terbentuknya kristal dari gas."
        )
    }

    ikon, perubahan, kalor, contoh = info[proses]

    st.markdown(f"""
    <div class="card" style="text-align:center;">

    <div style="font-size:65px;">
    {ikon}
    </div>

    <h2>{proses}</h2>

    <h3>{perubahan}</h3>

    <p><b>{kalor}</b></p>

    <p>{contoh}</p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Simulasi Energi Kalor")

    massa = st.number_input(
        "Massa zat (kg)",
        min_value=0.1,
        value=1.0,
        step=0.1,
        key="massa_wujud"
    )

    kalor_laten = st.number_input(
        "Kalor laten (J/kg)",
        min_value=1000.0,
        value=334000.0,
        step=1000.0,
        key="laten"
    )

    Q = massa * kalor_laten

    st.metric(
        "Kalor perubahan wujud",
        f"{Q:,.2f} J"
    )

    st.markdown("""
    <div class="lkpd">

    <div class="lkpd-title">❓ Pertanyaan Analisis</div>

    </div>
    """, unsafe_allow_html=True)

    q1 = st.text_area(
        "1. Apa yang dimaksud dengan perubahan wujud zat?",
        key="wujud_q1"
    )

    q2 = st.text_area(
        "2. Perubahan wujud apa saja yang membutuhkan kalor?",
        key="wujud_q2"
    )

    q3 = st.text_area(
        "3. Perubahan wujud apa saja yang melepaskan kalor?",
        key="wujud_q3"
    )

    q4 = st.text_area(
        "4. Apakah suhu selalu berubah ketika zat menerima kalor?",
        key="wujud_q4"
    )

    st.markdown("### 📝 Kesimpulan")

    kesimpulan = st.text_area(
        "Tuliskan kesimpulan percobaan:",
        height=150,
        key="wujud_kesimpulan"
    )

    if st.button(
        "💾 Simpan Jawaban LKPD",
        key="simpan_wujud"
    ):
        st.success("Jawaban LKPD telah dicatat.")


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
<b>VIRTUAL LAB SUHU DAN KALOR</b><br>
Media Pembelajaran Praktikum Fisika Berbasis Web<br>
Kelompok 8 • Fisika SMA
</div>
""", unsafe_allow_html=True)
