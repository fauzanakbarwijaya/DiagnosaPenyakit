import streamlit as st
import pandas as pd
from medical_data.dataRumahSakit98 import gejalaUmum

# Try to load the 'GejalaGigi' sheet safely
# try:
#     gejalaGigi = pd.read_excel('dataRumahSakit98.xlsx', sheet_name='GejalaGigi')
# except ValueError:
#     # If sheet is not found, use an empty DataFrame or a default one with 0
#     gejalaGigi = pd.DataFrame(columns=["penyakit", "gejala", "gejalaFisik", "faktorPendukung", "resepObat"])

def format_gejala_data(gejala_data):
    """Format the gejala data into a DataFrame suitable for display."""
    formatted_data = []

    for penyakit, details in gejala_data.items():
        # Combine all fields into a row
        row = {
            "No": len(formatted_data)+1,
            "Nama Penyakit": penyakit,
            "Gejala Non Fisik": ", ".join(details['gejala']),
            "Gejala Fisik": ", ".join(details['gejalaFisik']),
            "Faktor Pendukung": ", ".join(details['faktorPendukung']),
            "Resep Obat": ", ".join(details['resepObat']),
        }
        formatted_data.append(row)

    # Convert to DataFrame and set the index to False to avoid showing it
    df = pd.DataFrame(formatted_data)
    df.set_index('No', inplace=True)  # Optional: Set 'No' as the index column
    return df

def gejala_page():
    selectpoli = st.selectbox(
        "Lihat Gejala",
        ("Poli Umum", "Poli Gigi"),
        index=None,
        placeholder="Pilih Poli Gejala",
    )

    if selectpoli == "Poli Umum":
        formatted_data = format_gejala_data(gejalaUmum)
        st.dataframe(formatted_data)
    elif selectpoli == "Poli Gigi":
        formatted_data = format_gejala_data(gejalaGigi)
        st.dataframe(formatted_data)
