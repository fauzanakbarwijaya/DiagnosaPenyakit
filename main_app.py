import streamlit as st
st.set_page_config(page_title="Klinik Bidan Ani", page_icon="🏥")

# Custom CSS
st.markdown(
    """
    <style>
    /* Mengatur warna latar belakang aplikasi */
    .stApp {
        background-color: white;
        color: black;
    }

    .stAppHeader {
        background-color: white !important; /* Ubah background header ke putih */
        color: black !important; /* Ubah warna teks header ke hitam */
        border-bottom: 1px solid #ddd; /* Tambahkan garis bawah opsional */
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #217D8F;
    }
    
    /* Sidebar text color */
    [data-testid="stSidebar"] * {
        color: white;
    }

    .st-ae.st-c8.st-cu.st-bf.st-bg.st-bt.st-bu.st-bv.st-bw.st-bx.st-by.st-bs.st-cq input {
        background-color: #F9F9F9; /* Warna background lebih terang */
        border: 1px solid #D3D3D3; /* Warna border */
        color: black !important; /* Warna teks */
        padding: 10px; /* Padding dalam field */
        border-radius: 5px; /* Membuat sudut field membulat */
    }

    .st-emotion-cache-1n47svx {
        background-color: #217D8F; /* Warna tombol */
        color: #FFFFFF; /* Warna teks pada tombol */
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        cursor: pointer;
    }

    .st-emotion-cache-1n47svx:hover{
        background-color: blue;
        color: white;
    }

    .st-emotion-cache-ysk9xe>p{
        color: black;
    }

    .st-emotion-cache-3lmqu2{
        color: black;
    }

    .st-emotion-cache-1y5f4eg>p{
        color: gray;
    }

    [data-testid="stImageCaption"]{
        color: black;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)



st.title("Sistem Konsultasi Klinik Bidan Ani")
st.image("theApp/images/cover.png", caption="14230, Jl. Alur Laut I No.9 2, RT.2/RW.3, Rawabadak Sel., Kec : Koja, Jkt Utara, Daerah Khusus Ibukota Jakarta 14230")

is_logged_in = st.session_state.get("is_logged_in", False)

if not is_logged_in:
    st.sidebar.title("Navigasi")
else:
    st.sidebar.title(st.session_state.get('dokter', {}).get('nama', 'Dokter'))

if not is_logged_in:
    page = st.sidebar.radio(
        "Pilih Halaman",
        ["Landing Page", "Login Dokter"]
    )
else:
    page = st.sidebar.radio(
        "Pilih Halaman",
        ["Diagnosa", "Lihat Gejala", "Riwayat Konsultasi"]
    )

# Konten setiap halaman
if page == "Landing Page":
    st.write("Selamat datang di Klinik Bidan Ani!")
    st.write("Silakan gunakan menu navigasi di samping untuk masuk ke halaman yang diinginkan.")
elif page == "Login Dokter":
    from theApp.login import auth_page
    auth_page()
elif page == "Dashboard":
    st.write(f"Selamat datang, {st.session_state.get('dokter', {}).get('nama', 'Dokter')}!")
    st.write("Gunakan menu di samping untuk mengakses fitur yang tersedia.")
elif page == "Diagnosa":
    from theApp.diagnosa import diagnosa_page
    diagnosa_page()
elif page == "Lihat Gejala":
    from theApp.lihatGejala import gejala_page
    gejala_page()
elif page == "Riwayat Konsultasi":
    from theApp.history import history_page
    history_page()
else:
    st.write("Halaman tidak ditemukan.")
