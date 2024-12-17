import streamlit as st
from functions.functionApp import proses_diagnosa, simpan_history_excel
from medical_data.dataRumahSakit98 import gejalaUmum, gejalaGigi
import datetime

# History konsultasi (akan disimpan ke Excel)
history_konsultasi = []

def diagnosa_page():
    st.title("Halaman Diagnosa Pasien")
    st.write("Silakan masukkan data pasien untuk melakukan diagnosa.")

    # Input data pasien
    nama_pasien = st.text_input("Nama Pasien", "")
    gejala = st.text_input("Gejala Pasien (dipisahkan dengan koma)", "")
    gejala_fisik = st.text_input("Gejala Fisik Pasien (dipisahkan dengan koma)", "")
    faktor_pendukung = st.text_input("Faktor Pendukung (dipisahkan dengan koma)", "")

    # Tombol Diagnosa
    if st.button("Proses Diagnosa"):
        if nama_pasien and gejala:
            # Proses data inputan
            list_gejala = [g.strip() for g in gejala.split(",")]
            list_gejala_fisik = [gf.strip() for gf in gejala_fisik.split(",")]
            list_faktor_pendukung = [fp.strip() for fp in faktor_pendukung.split(",")]

            # Lakukan proses diagnosa
            penyakit, persentase, saran_obat = proses_diagnosa(
                list_gejala, list_gejala_fisik, list_faktor_pendukung, gejalaUmum
            )

            file_path = simpan_history_excel(history_konsultasi)

            st.success(f"Hasil diagnosa telah disimpan ke {file_path}")

            # Simpan hasil diagnosa ke dalam history
            history_konsultasi.append({
                "nama_pasien": nama_pasien,
                "gejala": list_gejala,
                "gejala_fisik": list_gejala_fisik,
                "faktor_pendukung": list_faktor_pendukung,
                "penyakit_kemungkinan": penyakit,
                "persentase_kemungkinan": persentase,
                "saran_obat": ", ".join(saran_obat),
                "tanggal_konsultasi": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            # Tampilkan hasil diagnosa
            st.subheader("Hasil Diagnosa")
            st.write(f"**Nama Pasien**: {nama_pasien}")
            st.write(f"**Gejala**: {', '.join(list_gejala)}")
            st.write(f"**Gejala Fisik**: {', '.join(list_gejala_fisik)}")
            st.write(f"**Faktor Pendukung**: {', '.join(list_faktor_pendukung)}")
            st.write(f"**Penyakit Kemungkinan**: {penyakit}")
            st.write(f"**Persentase Kemungkinan**: {persentase:.2f}%")
            st.write(f"**Saran Obat**: {', '.join(saran_obat)}")

            lanjut = st.radio("Apakah ingin melanjutkan konsultasi untuk pasien berikutnya?", ("Pilih","Ya", "Tidak"))

            if lanjut == "Ya":
                st.rerun()  
            elif lanjut == 'tidak':
                st.success("Data konsultasi telah disimpan. Anda sekarang keluar dari proses konsultasi.")
            else:
                st.error("Pilihan Tidak sesuai")

        else:
            st.error("Nama pasien dan gejala wajib diisi!")

    # # Tampilkan riwayat konsultasi
    # st.subheader("Riwayat Konsultasi")
    # if st.session_state.history_konsultasi:
    #     history_df = pd.DataFrame(st.session_state.history_konsultasi)
    #     st.dataframe(history_df)

    #     # Tombol Simpan ke Excel
    #     if st.button("Simpan Riwayat ke Excel"):
    #         simpan_history_excel(st.session_state.history_konsultasi)
    #         st.success("Riwayat konsultasi berhasil disimpan ke Excel.")
    # else:
    #     st.write("Belum ada riwayat konsultasi.")