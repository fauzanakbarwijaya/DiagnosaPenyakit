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

def proses_diagnosa(gejala_pasien, dataset_gejala):
    penyakit_kemungkinan = "Tidak Diketahui"
    persentase_kemungkinan = 0

    # Loop untuk mencocokkan gejala dengan dataset_gejala
    for penyakit, data in dataset_gejala.items():
        gejala_terkait = data["gejala"]
        match_count = len(set(gejala_pasien) & set(gejala_terkait))
        total_gejala = len(gejala_terkait)
        persentase = (match_count / total_gejala) * 100

        if persentase > persentase_kemungkinan:
            penyakit_kemungkinan = penyakit
            persentase_kemungkinan = persentase

    return penyakit_kemungkinan, persentase_kemungkinan

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
