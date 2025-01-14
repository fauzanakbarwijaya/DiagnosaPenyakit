import streamlit as st
import pandas as pd
from theApp.diagnosa import history_konsultasi

def format_konsultasi_data(history_konsultasi):
    """Format the history konsultasi data into a DataFrame suitable for display."""
    formatted_data = []

    for i, record in enumerate(history_konsultasi, start=1):
        # Combine all fields into a row
        row = {
            "No": i,
            "Nama Pasien": record["nama_pasien"],
            "Gejala Non Fisik": ", ".join(record["gejala"]),
            "Gejala Fisik": ", ".join(record["gejala_fisik"]),
            "Faktor Pendukung": ", ".join(record["faktor_pendukung"]),
            "Penyakit Kemungkinan": record["penyakit_kemungkinan"],
            "Persentase": f"{record['persentase_kemungkinan']}%",
            "Resep Obat": record["saran_obat"],
            "Tanggal Konsultasi": record["tanggal_konsultasi"]
        }
        formatted_data.append(row)

    # Convert to DataFrame and set 'No' as the index column
    df = pd.DataFrame(formatted_data)
    df.set_index('No', inplace=True)  # Optional: Set 'No' as the index column
    return df


def history_page():
    st.title("History Konsultasi")
    if history_konsultasi:
        st.dataframe(history_konsultasi)
    else:
        st.write("Belum ada riwayat konsultasi, Mohon untuk melakukan konsultasi sekali.")
