# functions app

import os
import datetime
import pandas as pd

def auth_dokter(df_dokter, id_dr):
    # Cari dokter berdasarkan ID
    dokter = df_dokter[df_dokter['id_dr'] == id_dr]

    # Jika ID tidak ditemukan
    if dokter.empty:
        return None

    # Jika ditemukan, kembalikan data dokter
    return {
        'nama': dokter.iloc[0]['name'],
        'poli': dokter.iloc[0]['poli']
    }

def proses_diagnosa(gejala_pasien, gejala_fisik_pasien, faktor_pendukung_pasien, dataset_gejala):
    penyakit_kemungkinan = "Tidak Diketahui"
    persentase_kemungkinan = 0
    resep_obat = []

    # Loop untuk mencocokkan gejala dengan dataset_gejala
    for penyakit, data in dataset_gejala.items():
        gejala_terkait = data["gejala"]
        gejala_fisik_terkait = data.get("gejalaFisik", [])
        faktor_pendukung_terkait = data.get("faktorPendukung", [])

        # Memastikan hanya gejala yang ada dalam dataset yang dihitung
        valid_gejala_pasien = [gejala for gejala in gejala_pasien if gejala in gejala_terkait]
        valid_gejala_fisik_pasien = [gejala for gejala in gejala_fisik_pasien if gejala in gejala_fisik_terkait]
        valid_faktor_pendukung_pasien = [faktor for faktor in faktor_pendukung_pasien if faktor in faktor_pendukung_terkait]

        # Hitung kecocokan untuk gejala yang ada
        match_count_gejala = len(valid_gejala_pasien)
        match_count_fisik = len(valid_gejala_fisik_pasien)
        match_count_faktor = len(valid_faktor_pendukung_pasien)

        # Total gejala yang benar
        total_gejala_benar = match_count_gejala + match_count_fisik + match_count_faktor

        # Total inputan gejala pasien (baik yang benar maupun salah)
        total_inputan_gejala = len(gejala_pasien) + len(gejala_fisik_pasien) + len(faktor_pendukung_pasien)

        # Hitung persentase kecocokan
        persentase = (total_gejala_benar / total_inputan_gejala) * 100

        # Update kemungkinan penyakit jika persentase lebih tinggi
        if persentase > persentase_kemungkinan:
            penyakit_kemungkinan = penyakit
            persentase_kemungkinan = persentase
            resep_obat = data.get("resepObat", [])


    return penyakit_kemungkinan, persentase_kemungkinan, resep_obat

def simpan_history_excel(history_konsultasi, file_path="history_konsultasi.xlsx"):
    # Membuat DataFrame dari history_konsultasi
    df_history = pd.DataFrame(history_konsultasi)

    # Memeriksa apakah file sudah ada atau belum
    try:
        # Jika file sudah ada, kita append data ke file yang ada
        df_existing = pd.read_excel(file_path)
        df_history = pd.concat([df_existing, df_history], ignore_index=True)
    except FileNotFoundError:
        # Jika file belum ada, buat file baru
        pass

    # Menyimpan DataFrame ke file Excel
    df_history.to_excel(file_path, index=False)
    return file_path
