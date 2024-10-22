# function/diagnosa.py

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
