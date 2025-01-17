import os
import datetime
import pandas as pd
from medical_data.dataRumahSakit98 import dataDokter, gejalaUmum
from functions.function import proses_diagnosa, auth_dokter, simpan_history_excel as simpan_history

# Data untuk history konsultasi
history_konsultasi = []

# Convert dataDokter to DataFrame
df_dokter = pd.DataFrame(dataDokter)

print('\t\t SELAMAT DATANG DI RUMAH SAKIT 98')
print('=' * 70)

# Autentikasi Dokter
nama_dokter, poli_dokter = auth_dokter(df_dokter)

print(f"\nSelamat Datang, {nama_dokter}!")
print(f"Anda terdaftar di {poli_dokter}\n\n")

while True:
    # Masuk ke tampilan Poli yang sesuai
    if poli_dokter == "Poli Umum":
        print('\t\t\t POLI UMUM\t\t\t')
        print('=' * 70)
        nama_pasien = input("Masukkan Nama Pasien : ")
        gejala = input("Masukkan gejala pasien (dipisahkan koma): ").split(",")
        gejala_fisik = input("Masukkan gejala fisik pasien : ").split(",")
        faktor_pendukung = input("Masukkan faktor pendukung : ").split(",")

        # Proses diagnosa Poli Umum
        penyakit, persentase, saran_obat = proses_diagnosa(gejala, gejala_fisik, faktor_pendukung, gejalaUmum)

    elif poli_dokter == "Poli Gigi":
        print('\t\t\t POLI GIGI\t\t\t')
        print('=' * 70)
        # nama_pasien = input("Masukkan Nama Pasien : ")
        # gejala = input("Masukkan gejala pasien (dipisahkan koma): ").split(",")
        # # Proses diagnosa Poli Gigi
        # penyakit, persentase = proses_diagnosa(gejala, gejalaGigi)

    else:
        print(f"Poli {poli_dokter} belum terdaftar.")
        break

    # Simpan history konsultasi
    history_konsultasi.append({
        "nama_pasien": nama_pasien,
        "gejala": gejala,
        "gejala_fisik": gejala_fisik,
        "faktor_pendukung": faktor_pendukung,
        "penyakit_kemungkinan": penyakit,
        "persentase_kemungkinan": persentase,
        "saran_obat": ", ".join(saran_obat),
        "dokter": nama_dokter,
        "poli": poli_dokter,
        "tanggal_konsultasi": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    # Tampilkan hasil diagnosa
    print("\n=== Hasil Diagnosa ===")
    print(f"Nama Pasien: {nama_pasien}")
    print(f"Gejala: {', '.join(gejala)}")
    print(f"Gejala Fisik: {', '.join(gejala_fisik)}")
    print(f"Faktor Pendukung: {', '.join(faktor_pendukung)}")
    print(f"Penyakit Kemungkinan: {penyakit}")
    print(f"Persentase Kemungkinan: {persentase:.2f}%")
    print(f"Saran Obat: {', '.join(saran_obat)}")
    print("=======================")

    # Pilihan lanjut atau akhiri
    lanjut = input("Apakah ingin lanjut konsultasi pasien berikutnya? (ya/tidak): ").lower()
    if lanjut != 'ya':
        break

# Simpan history ke Excel setelah dokter selesai
simpan_history(history_konsultasi)