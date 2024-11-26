import streamlit as st

# Konfigurasi awal aplikasi
st.set_page_config(page_title="Klinik Bidan Ani", page_icon="🏥")

# Judul utama
st.title("Sistem Konsultasi Klinik Bidan Ani")
st.sidebar.title("Navigasi")

# Cek apakah user sudah login
is_logged_in = st.session_state.get("is_logged_in", False)

# Pilihan navigasi berdasarkan status login
if not is_logged_in:
    page = st.sidebar.radio(
        "Pilih Halaman",
        ["Landing Page", "Login Dokter"]
    )
else:
    page = st.sidebar.radio(
        "Pilih Halaman",
        ["Dashboard", "Diagnosa", "Lihat Gejala", "Riwayat Konsultasi"]
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
