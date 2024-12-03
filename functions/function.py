# functions/function.py

import os
import datetime
import pandas as pd

def auth_dokter(df_dokter):
    while True:
        try:
            id_dr = int(input("Silahkan Masukkan ID Dokter Anda : "))
        except ValueError:
            print("ID harus berupa angka!")
            continue

        dokter = df_dokter[df_dokter['id_dr'] == id_dr]  # Cari dokter berdasarkan ID
        if dokter.empty:
            print("ID Dokter tidak ditemukan!")
        else:
            nama_dokter = dokter.iloc[0]['name']
            poli_dokter = dokter.iloc[0]['poli']
            return nama_dokter, poli_dokter
        
def proses_diagnosa(gejala_pasien, gejala_fisik_pasien, faktor_pendukung_pasien, dataset_gejala):
    penyakit_kemungkinan = "Tidak Diketahui"
    persentase_kemungkinan = 0
    resep_obat = []

    # Loop untuk mencocokkan gejala dengan dataset_gejala
    for penyakit, data in dataset_gejala.items():
        gejala_terkait = data["gejala"]
        gejala_fisik_terkait = data.get("gejalaFisik", [])
        faktor_pendukung_terkait = data.get("faktorPendukung", [])

        # Hitung kecocokan gejala
        match_count_gejala = len(set(gejala_pasien) & set(gejala_terkait))
        match_count_fisik = len(set(gejala_fisik_pasien) & set(gejala_fisik_terkait))
        match_count_faktor = len(set(faktor_pendukung_pasien) & set(faktor_pendukung_terkait))
        total_gejala = len(gejala_terkait) + len(gejala_fisik_terkait) + len(faktor_pendukung_terkait)

        # Hitung persentase kecocokan
        persentase = ((match_count_gejala + match_count_fisik + match_count_faktor) / total_gejala) * 100

        # Update kemungkinan penyakit jika persentase lebih tinggi
        if persentase > persentase_kemungkinan:
            penyakit_kemungkinan = penyakit
            persentase_kemungkinan = persentase
            resep_obat = data.get("resepObat", [])

    return penyakit_kemungkinan, persentase_kemungkinan, resep_obat


def simpan_history_excel(history_konsultasi, filename="history_konsultasi.xlsx"):
    # Cek apakah file sudah ada
    if os.path.exists(filename):
        # Jika ada, baca data yang sudah ada
        df_existing = pd.read_excel(filename)
        # Gabungkan dengan data baru
        df_history = pd.concat([df_existing, pd.DataFrame(history_konsultasi)], ignore_index=True)
    else:
        # Jika tidak ada, buat DataFrame baru
        df_history = pd.DataFrame(history_konsultasi)

    # Simpan ke Excel
    df_history.to_excel(filename, index=False)
    print("History konsultasi telah disimpan ke Excel.")
