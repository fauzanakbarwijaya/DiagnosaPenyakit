import streamlit as st
import pandas as pd
from theApp.diagnosa import history_konsultasi

def history_page():
    st.title("History Konsultasi")
    if history_konsultasi:
        st.dataframe(history_konsultasi)
    else:
        st.write("Belum ada riwayat konsultasi, Mohon untuk melakukan konsultasi sekali.")
