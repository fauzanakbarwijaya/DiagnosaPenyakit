import streamlit as st

st.title("Sistem Konsultasi Rumah Sakit 98")
st.sidebar.title("Navigasi")

# Navigasi ke halaman yang berbeda
page = st.sidebar.radio(
    "Pilih Halaman",
    ["Landing Page", "Login Dokter", "Diagnosa", "Lihat Gejala", "Riwayat Konsultasi"]
)

if page == "Landing Page":
    st.write("Selamat datang di Rumah Sakit 98!")
    st.write("Silakan gunakan menu navigasi di samping untuk masuk ke halaman yang diinginkan.")
elif page == "Login Dokter":
    from theApp.auth import auth_page
    auth_page()
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
    st.write('tidak ada pilihan yang dipilih')