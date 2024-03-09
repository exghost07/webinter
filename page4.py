import streamlit as st

def page_4():
    st.title('Hitung Luas Persegi Panjang')
    panjang = st.number_input ("Masukan Nilai Panjang", 0)
    lebar = st.number_input ("Masukan Nilai Lebar", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = panjang * lebar
        st.success (f"Luas Persegi Panjang Adalah = {luas}")