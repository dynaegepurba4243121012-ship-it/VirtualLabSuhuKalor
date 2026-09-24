import streamlit as st
import math

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

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: #f5f7fb;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #071a35 0%, #0b2850 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.sidebar-title {
    font-size: 22px;
    font-weight: 800;
    text-align: center;
    padding: 15px 5px 5px 5px;
}

.sidebar-subtitle {
    font-size: 12px;
    text-align: center;
    opacity: 0.75;
    margin-bottom: 25px;
}

.sidebar-info {
    background: rgba(255,255,255,0.08);
    padding: 12px;
    border-radius: 12px;
    margin-top: 25px;
    font-size: 12px;
    text-align: center;
}

/* HEADER */
.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 0 20px 0;
}

.badge {
    background: #e8f1ff;
    color: #1555a5;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
}

/* HERO */
.hero {
    background: linear-gradient(135deg, #0b3d78 0%, #1261a8 100%);
    border-radius: 24px;
    padding: 42px 45px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 12px 30px rgba(15, 70, 130, 0.20);
}

.hero h1 {
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    font-size: 16px;
    opacity: 0.92;
}

.hero-small {
    display: inline-block;
    background: rgba(255,255,255,0.16);
    padding: 7px 14px;
    border-radius: 20px;
    font-size: 12px;
    margin-bottom: 14px;
}

/* CARD */
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e5e9f0;
    box-shadow: 0 5px 18px rgba(0,0,0,0.05);
    min-height: 220px;
}

.card-icon {
    font-size: 38px;
    margin-bottom: 12px;
}

.card h3 {
    color: #12365f;
    margin-bottom: 8px;
}

.card p {
    color: #68778d;
    font-size: 13px;
    line-height: 1.6;
}

/* SECTION */
.section-title {
    color: #12365f;
    font-size: 26px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 18px;
}

/* SIMULATOR */
.sim-box {
    background: white;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #e1e7ef;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}

.result-box {
    background: #edf6ff;
    border-left: 5px solid #1674d1;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
}

.big-result {
    font-size: 35px;
    font-weight: 800;
    color: #075da8;
}

.formula {
    background: #f4f6f9;
    padding: 15px;
    border-radius: 10px;
    font-family: monospace;
    font-size: 16px;
    margin: 15px 0;
}

/* FOOTER */
.footer {
    margin-top: 50px;
    padding: 20px;
    text-align: center;
    color: #8290a3;
    font-size: 12px;
    border-top: 1px solid #e1e6ed;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Beranda"


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">🌡️ Virtual Lab</div>
    <div class="sidebar-subtitle">Suhu dan Kalor</div>
    """, unsafe_allow_html=True)

    st.markdown("### MENU")

    if st.button("🏠  Beranda", use_container_width=True):
        st.session_state.page = "Beranda"

    if st.button("🌡️  Pengukuran Suhu", use_container_width=True):
        st.session_state.page = "Pengukuran Suhu"

    if st.button("🔥  Kalor", use_container_width=True):
        st.session_state.page = "Kalor"

    if st.button("⚖️  Asas Black", use_container_width=True):
        st.session_state.page = "Asas Black"

    if st.button("💧  Perubahan Wujud", use_container_width=True):
        st.session_state.page = "Perubahan Wujud"

    st.markdown("""
    <div class="sidebar-info">
    <b>KELOMPOK 8</b><br><br>
    Media Pembelajaran Praktikum Fisika Berbasis Web
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="topbar">
    <div>
        <b style="font-size:20px;color:#12365f;">
        Virtual Lab Suhu dan Kalor
        </b>
    </div>
    <div class="badge">☀️ Kelompok 8</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# BERANDA
# =========================================================

if st.session_state.page == "Beranda":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">🔬 PRAKTIKUM FISIKA BERBASIS WEB</div>
        <h1>Selamat Datang di<br>VIRTUAL LAB SUHU DAN KALOR</h1>
        <p>
        Media pembelajaran praktikum fisika berbasis web
        untuk mempelajari konsep suhu, kalor, Asas Black,
        dan perubahan wujud zat secara interaktif.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📚 Materi Pembelajaran</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🌡️</div>
            <h3>Suhu</h3>
            <p>
            Mempelajari pengukuran suhu dan hubungan
            antara skala Celsius, Fahrenheit, Kelvin,
            dan Reamur.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🔥</div>
            <h3>Kalor</h3>
            <p>
            Mempelajari kalor yang diperlukan untuk
            menaikkan atau menurunkan suhu suatu zat.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <div class="card-icon">⚖️</div>
            <h3>Asas Black</h3>
            <p>
            Menganalisis pertukaran kalor antara benda
            panas dan benda dingin sampai tercapai
            suhu kesetimbangan.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="card">
            <div class="card-icon">💧</div>
            <h3>Perubahan Wujud</h3>
            <p>
            Mempelajari proses mencair, membeku,
            menguap, mengembun, dan perubahan wujud
            lainnya.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🧪 Pilih Simulasi</div>',
        unsafe_allow_html=True
    )

    s1, s2 = st.columns(2)

    with s1:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🌡️</div>
            <h3>Pengukuran Suhu</h3>
            <p>
            Ubah nilai suhu dari satu skala ke skala
            lainnya dan amati hasil pengukurannya.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Mulai Simulasi →", key="home_suhu",
                     use_container_width=True):
            st.session_state.page = "Pengukuran Suhu"

    with s2:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🔥</div>
            <h3>Perhitungan Kalor</h3>
            <p>
            Simulasikan kalor yang diterima atau dilepas
            oleh suatu benda berdasarkan massa, kalor
            jenis, dan perubahan suhu.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Mulai Simulasi →", key="home_kalor",
                     use_container_width=True):
            st.session_state.page = "Kalor"


# =========================================================
# PENGUKURAN SUHU
# =========================================================

elif st.session_state.page == "Pengukuran Suhu":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">🌡️ SIMULASI 01</div>
        <h1>Pengukuran Suhu</h1>
        <p>
        Simulasikan konversi suhu dari Celsius ke
        Fahrenheit, Kelvin, dan Reamur.
        </p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1, 1])

    with left:

        st.markdown(
            '<div class="section-title">🎛️ Pengaturan Suhu</div>',
            unsafe_allow_html=True
        )

        with st.container(border=True):

            suhu_c = st.slider(
                "Atur suhu dalam Celsius (°C)",
                -50.0,
                150.0,
                25.0,
                1.0
            )

            st.write("Suhu yang dipilih:")

            st.markdown(
                f'<div class="big-result">{suhu_c:.0f} °C</div>',
                unsafe_allow_html=True
            )

    with right:

        fahrenheit = (suhu_c * 9 / 5) + 32
        kelvin = suhu_c + 273.15
        reamur = suhu_c * 4 / 5

        st.markdown(
            '<div class="section-title">📊 Hasil Pengukuran</div>',
            unsafe_allow_html=True
        )

        r1, r2 = st.columns(2)

        with r1:
            st.metric("Celsius", f"{suhu_c:.1f} °C")
            st.metric("Fahrenheit", f"{fahrenheit:.1f} °F")

        with r2:
            st.metric("Kelvin", f"{kelvin:.1f} K")
            st.metric("Reamur", f"{reamur:.1f} °R")

    st.markdown("---")

    st.markdown("### 📖 Persamaan Konversi")

    st.markdown("""
    <div class="formula">
    Fahrenheit = (9/5 × Celsius) + 32
    </div>

    <div class="formula">
    Kelvin = Celsius + 273,15
    </div>

    <div class="formula">
    Reamur = 4/5 × Celsius
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# KALOR
# =========================================================

elif st.session_state.page == "Kalor":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">🔥 SIMULASI 02</div>
        <h1>Simulasi Kalor</h1>
        <p>
        Hitung kalor yang diperlukan untuk mengubah
        suhu suatu benda.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🎛️ Parameter Percobaan</div>',
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)

    with a:
        massa = st.number_input(
            "Massa benda (kg)",
            min_value=0.01,
            max_value=100.0,
            value=1.0,
            step=0.1
        )

    with b:
        kalor_jenis = st.number_input(
            "Kalor jenis (J/kg°C)",
            min_value=1.0,
            max_value=10000.0,
            value=4200.0,
            step=100.0
        )

    with c:
        suhu_awal = st.number_input(
            "Suhu awal (°C)",
            min_value=-100.0,
            max_value=500.0,
            value=25.0,
            step=1.0
        )

    suhu_akhir = st.slider(
        "Atur suhu akhir (°C)",
        -100.0,
        500.0,
        75.0,
        1.0
    )

    delta_t = suhu_akhir - suhu_awal
    kalor = massa * kalor_jenis * delta_t

    st.markdown("---")

    x, y = st.columns(2)

    with x:
        st.markdown("""
        <div class="sim-box">
            <h3>📐 Persamaan</h3>
            <div class="formula">
            Q = m × c × ΔT
            </div>
            <p>
            Q = kalor (J)<br>
            m = massa (kg)<br>
            c = kalor jenis (J/kg°C)<br>
            ΔT = perubahan suhu (°C)
            </p>
        </div>
        """, unsafe_allow_html=True)

    with y:

        if kalor > 0:
            jenis = "Kalor diserap oleh benda 🔥"
        elif kalor < 0:
            jenis = "Kalor dilepas oleh benda ❄️"
        else:
            jenis = "Tidak terjadi perpindahan kalor"

        st.markdown(f"""
        <div class="sim-box">
            <h3>📊 Hasil Simulasi</h3>
            <div class="big-result">{kalor:,.2f} J</div>
            <p>{jenis}</p>
            <p>ΔT = {delta_t:.2f} °C</p>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# ASAS BLACK
# =========================================================

elif st.session_state.page == "Asas Black":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">⚖️ SIMULASI 03</div>
        <h1>Asas Black</h1>
        <p>
        Simulasikan pencampuran dua benda dengan suhu
        berbeda hingga mencapai suhu kesetimbangan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🎛️ Parameter Benda</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🔥 Benda Panas")

        m_panas = st.number_input(
            "Massa benda panas (kg)",
            min_value=0.01,
            value=1.0,
            step=0.1,
            key="mp"
        )

        c_panas = st.number_input(
            "Kalor jenis benda panas (J/kg°C)",
            min_value=1.0,
            value=4000.0,
            step=100.0,
            key="cp"
        )

        T_panas = st.number_input(
            "Suhu benda panas (°C)",
            min_value=-100.0,
            value=80.0,
            step=1.0,
            key="tp"
        )

    with col2:

        st.markdown("### ❄️ Benda Dingin")

        m_dingin = st.number_input(
            "Massa benda dingin (kg)",
            min_value=0.01,
            value=1.0,
            step=0.1,
            key="md"
        )

        c_dingin = st.number_input(
            "Kalor jenis benda dingin (J/kg°C)",
            min_value=1.0,
            value=4200.0,
            step=100.0,
            key="cd"
        )

        T_dingin = st.number_input(
            "Suhu benda dingin (°C)",
            min_value=-100.0,
            value=20.0,
            step=1.0,
            key="td"
        )

    # Suhu keseimbangan
    penyebut = (m_panas * c_panas) + (m_dingin * c_dingin)

    if penyebut != 0:
        T_eq = (
            (m_panas * c_panas * T_panas)
            +
            (m_dingin * c_dingin * T_dingin)
        ) / penyebut
    else:
        T_eq = 0

    Q_panas = m_panas * c_panas * (T_panas - T_eq)
    Q_dingin = m_dingin * c_dingin * (T_eq - T_dingin)

    st.markdown("---")

    st.markdown("""
    <div class="result-box">
        <h3>⚖️ Suhu Kesetimbangan</h3>
    """, unsafe_allow_html=True)

    st.markdown(
        f'<div class="big-result">{T_eq:.2f} °C</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p>
        Kalor yang dilepas benda panas:
        <b>{Q_panas:,.2f} J</b>
        </p>

        <p>
        Kalor yang diterima benda dingin:
        <b>{Q_dingin:,.2f} J</b>
        </p>

        <p>
        Sesuai Asas Black, secara ideal kalor yang dilepas
        sama dengan kalor yang diterima.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 📖 Persamaan Asas Black")

    st.markdown("""
    <div class="formula">
    Q lepas = Q terima
    </div>

    <div class="formula">
    m₁ c₁ (T₁ - Tₑ) = m₂ c₂ (Tₑ - T₂)
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# PERUBAHAN WUJUD
# =========================================================

elif st.session_state.page == "Perubahan Wujud":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">💧 SIMULASI 04</div>
        <h1>Perubahan Wujud Zat</h1>
        <p>
        Amati hubungan suhu dengan energi kalor
        pada proses perubahan wujud.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🧊 Pilih Proses Perubahan Wujud</div>',
        unsafe_allow_html=True
    )

    proses = st.selectbox(
        "Pilih proses:",
        [
            "Mencair",
            "Membeku",
            "Menguap",
            "Mengembun",
            "Menyublim",
            "Mengkristal"
        ]
    )

    data_proses = {
        "Mencair": (
            "Padat → Cair",
            "Es berubah menjadi air.",
            "🧊 → 💧"
        ),
        "Membeku": (
            "Cair → Padat",
            "Air berubah menjadi es.",
            "💧 → 🧊"
        ),
        "Menguap": (
            "Cair → Gas",
            "Air berubah menjadi uap.",
            "💧 → ☁️"
        ),
        "Mengembun": (
            "Gas → Cair",
            "Uap air berubah menjadi air.",
            "☁️ → 💧"
        ),
        "Menyublim": (
            "Padat → Gas",
            "Zat padat berubah langsung menjadi gas.",
            "🧊 → ☁️"
        ),
        "Mengkristal": (
            "Gas → Padat",
            "Gas berubah langsung menjadi zat padat.",
            "☁️ → 🧊"
        )
    }

    bentuk, penjelasan, ikon = data_proses[proses]

    st.markdown(f"""
    <div class="sim-box">
        <div style="font-size:60px;text-align:center;">
        {ikon}
        </div>

        <h2 style="text-align:center;color:#12365f;">
        {proses}
        </h2>

        <h3 style="text-align:center;">
        {bentuk}
        </h3>

        <p style="text-align:center;">
        {penjelasan}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🔥 Simulasi Energi")

    massa_zat = st.number_input(
        "Massa zat (kg)",
        min_value=0.01,
        value=1.0,
        step=0.1
    )

    kalor_laten = st.number_input(
        "Kalor laten (J/kg)",
        min_value=1.0,
        value=334000.0,
        step=1000.0
    )

    energi = massa_zat * kalor_laten

    st.metric(
        "Energi perubahan wujud",
        f"{energi:,.2f} J"
    )

    st.markdown("""
    <div class="formula">
    Q = m × L
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Pada perubahan wujud, kalor digunakan untuk mengubah "
        "keadaan zat. Suhu zat dapat tetap selama proses "
        "perubahan wujud berlangsung."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    <b>Virtual Lab Suhu dan Kalor</b><br>
    Media Pembelajaran Praktikum Fisika Berbasis Web<br><br>
    Kelompok 8 • Fisika SMA
</div>
""", unsafe_allow_html=True)
