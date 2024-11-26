import streamlit as st
from medical_data.dataRumahSakit98 import dataDokter
from functions.functionApp import auth_dokter
import pandas as pd

def auth_page():
    st.title("Login Dokter")
    
    id_dokter = st.text_input("Masukkan ID Dokter", value="")

    if st.button("Login"):
        df_dokter = pd.DataFrame(dataDokter)

        try:
            id_dokter = int(id_dokter)
        except ValueError:
            st.error("ID Dokter harus berupa angka!")
            return

        result = auth_dokter(df_dokter, id_dokter)

        if result:
            st.success(f"Selamat datang, Dr. {result['nama']} di poli {result['poli']}!")
            st.session_state["is_logged_in"] = True
            st.session_state["dokter"] = result
            
            st.rerun()
        else:
            st.error("ID Dokter tidak ditemukan.")
