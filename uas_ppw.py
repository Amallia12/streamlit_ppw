from streamlit_option_menu import option_menu
import streamlit as st
import joblib
import pandas as pd

st.header("Klasifikasi Artikel Berita Dengan Reduksi Dimensi", divider='rainbow')
text = st.text_area("Masukkan Artikel Berita")

button = st.button("Submit")
