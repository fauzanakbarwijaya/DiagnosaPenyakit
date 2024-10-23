import os
import datetime
import pandas as pd
from medical_data.dataRumahSakit98 import dataDokter, gejalaUmum, gejalaGigi
from functions.function import proses_diagnosa

# Data untuk history konsultasi
history_konsultasi = []
# Convert dataDokter to DataFrame
df_dokter = pd.DataFrame(dataDokter)

print('\t\t SELAMAT DATANG DI RUMAH SAKIT 98')
print('='*70)

# Attandance Doctor Fiture
while True:
    # Attandance Doctor Feature
    id_dr = int(input("Silahkan Masukkan ID Dokter Anda : "))
    dokter = df_dokter[df_dokter['id_dr'] == id_dr] # Cari dokter berdasarkan ID
    if dokter.empty:
        print("ID Dokter tidak ditemukan!")
        continue
    else:
        nama_dokter = dokter.iloc[0]['name']
        poli_dokter = dokter.iloc[0]['poli']

        print(f"\nSelamat Datang, {nama_dokter}!")
        print(f"Anda terdaftar di {poli_dokter}\n\n")

        while True:
            # Masuk ke tampilan Poli yang sesuai
            if poli_dokter == "Poli Umum":
                print('\t\t\t POLI UMUM\t\t\t')
                print('='*70)
                nama_pasien = input("Masukkan Nama Pasien : ")
                gejala = input("Masukkan gejala pasien (dipisahkan koma): ").split(",")
                # Proses diagnosa Poli Umum
                penyakit, persentase = proses_diagnosa(gejala, gejalaUmum)

            elif poli_dokter == "Poli Gigi":
                print('\t\t\t POLI GIGI\t\t\t')
                print('='*70)
                nama_pasien = input("Masukkan Nama Pasien : ")
                gejala = input("Masukkan gejala pasien (dipisahkan koma): ").split(",")
                # Proses diagnosa Poli Gigi
                penyakit, persentase = proses_diagnosa(gejala, gejalaGigi)

            else:
                print(f"Poli {poli_dokter} belum terdaftar.")
                break

            # Simpan history konsultasi
            history_konsultasi.append({
                "nama_pasien": nama_pasien,
                "gejala": gejala,
                "penyakit_kemungkinan": penyakit,
                "persentase_kemungkinan": persentase,
                "dokter": nama_dokter,
                "poli": poli_dokter,
                "tanggal_konsultasi": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            # Tampilkan hasil diagnosa
            print("\n=== Hasil Diagnosa ===")
            print(f"Nama Pasien: {nama_pasien}")
            print(f"Gejala: {', '.join(gejala)}")
            print(f"Penyakit Kemungkinan: {penyakit}")
            print(f"Persentase Kemungkinan: {persentase:.2f}%")
            print("=======================")

            # Pilihan lanjut atau akhiri
            lanjut = input("Apakah ingin lanjut konsultasi pasien berikutnya? (ya/tidak): ").lower()
            if lanjut != 'ya':
                break

    # Cek apakah file sudah ada
    if os.path.exists("history_konsultasi.xlsx"):
        # Jika ada, baca data yang sudah ada
        df_existing = pd.read_excel("history_konsultasi.xlsx")
        # Gabungkan dengan data baru
        df_history = pd.concat([df_existing, pd.DataFrame(history_konsultasi)], ignore_index=True)
    else:
        # Jika tidak ada, buat DataFrame baru
        df_history = pd.DataFrame(history_konsultasi)

    # Simpan history ke Excel setelah dokter selesai
    df_history.to_excel("history_konsultasi.xlsx", index=False)
    print("History konsultasi telah disimpan ke Excel.")
    break