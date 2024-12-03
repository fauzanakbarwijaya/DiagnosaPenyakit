import streamlit as st
import pandas as pd
from medical_data.dataRumahSakit98 import gejalaUmum, gejalaGigi

def gejala_page():
    selectpoli = st.selectbox(
        "Lihat Gejala",
        ("Poli Umum", "Poli Gigi"),
        index=None,
        placeholder="Pilih Poli Gejala",
    )
    if selectpoli == "Poli Umum":
        st.dataframe(gejalaUmum)
    elif selectpoli == "Poli Gigi":
        st.dataframe(gejalaGigi)
