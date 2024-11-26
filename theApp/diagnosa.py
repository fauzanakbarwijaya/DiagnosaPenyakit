import streamlit as st
from functions.functionApp import proses_diagnosa, simpan_history_excel
from medical_data.dataRumahSakit98 import gejalaUmum, gejalaGigi
import datetime

# History konsultasi (akan disimpan ke Excel)
history_konsultasi = []

def diagnosa_page():
    if not st.session_state.get("is_logged_in", False):
        st.warning("Silakan login terlebih dahulu.")
        return

    st.title(f"Diagnosa Pasien")
    nama_pasien = st.text_input("Masukkan Nama Pasien")
    poli_dokter = st.session_state["dokter"]["poli"]

    # Menampilkan input gejala sebagai teks
    gejala_input = st.text_area("Masukkan Gejala Pasien (dipisahkan dengan koma)", "")

    if st.button("Diagnosa"):
        if gejala_input:
            # Mengubah input gejala yang dipisahkan koma menjadi list
            gejala = [gejala.strip() for gejala in gejala_input.split(",")]

            # Proses diagnosa berdasarkan poli yang dipilih
            if poli_dokter == "Poli Umum":
                penyakit, persentase = proses_diagnosa(gejala, gejalaUmum)
            elif poli_dokter == "Poli Gigi":
                penyakit, persentase = proses_diagnosa(gejala, gejalaGigi)

            # Menampilkan hasil diagnosa
            st.write(f"**Penyakit yang kemungkinan diderita:** {penyakit}")
            st.write(f"**Persentase Kemungkinan:** {persentase:.2f}%")

            # Simpan hasil diagnosa ke history konsultasi
            history_konsultasi.append({
                "nama_pasien": nama_pasien,
                "gejala": gejala,
                "penyakit_kemungkinan": penyakit,
                "persentase_kemungkinan": persentase,
                "dokter": st.session_state["dokter"]["nama"],  # Nama dokter dari session
                "poli": poli_dokter,
                "tanggal_konsultasi": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            file_path = simpan_history_excel(history_konsultasi)

            st.success(f"Hasil diagnosa telah disimpan ke {file_path}")

            lanjut = st.radio("Apakah ingin melanjutkan konsultasi untuk pasien berikutnya?", ("Pilih","Ya", "Tidak"))

            if lanjut == "Ya":
                st.rerun()  
            elif lanjut == 'tidak':
                st.success("Data konsultasi telah disimpan. Anda sekarang keluar dari proses konsultasi.")
            else:
                st.error("Pilihan Tidak sesuai")
                
        else:
            st.error("Silakan masukkan gejala terlebih dahulu.")
