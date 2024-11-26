import streamlit as st
from medical_data.dataRumahSakit98 import dataDokter
from functions.function import auth_dokter
import pandas as pd

def auth_page():
    st.title("Login Dokter")
    username = st.text_input("Masukkan Username")
    password = st.text_input("Masukkan Password", type="password")

    if st.button("Login"):
        df_dokter = pd.DataFrame(dataDokter)
        result = auth_dokter(df_dokter, username, password)
        if result:
            st.success(f"Selamat datang, {result['nama']} di {result['poli']}!")
            st.session_state["is_logged_in"] = True
            st.session_state["dokter"] = result
        else:
            st.error("Username atau password salah.")
