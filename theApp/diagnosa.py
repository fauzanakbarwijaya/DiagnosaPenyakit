import streamlit as st
from functions.function import proses_diagnosa
from medical_data.dataRumahSakit98 import gejalaUmum, gejalaGigi

def diagnosa_page():
    if not st.session_state.get("is_logged_in", False):
        st.warning("Silakan login terlebih dahulu.")
        return

    st.title("Diagnosa Pasien")
    nama_pasien = st.text_input("Masukkan Nama Pasien")
    poli_dokter = st.session_state["dokter"]["poli"]

    if poli_dokter == "Poli Umum":
        gejala = st.multiselect("Pilih Gejala", gejalaUmum.keys())
    elif poli_dokter == "Poli Gigi":
        gejala = st.multiselect("Pilih Gejala", gejalaGigi.keys())

    if st.button("Diagnosa"):
        if gejala:
            penyakit, persentase = proses_diagnosa(gejala, gejalaUmum if poli_dokter == "Poli Umum" else gejalaGigi)
            st.write(f"**Penyakit yang kemungkinan diderita:** {penyakit}")
            st.write(f"**Persentase Kemungkinan:** {persentase:.2f}%")
        else:
            st.error("Silakan pilih gejala terlebih dahulu.")
