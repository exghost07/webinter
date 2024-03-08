import streamlit as st

def page_4():
    st.title('Hitung Luas Persegi Panjang')
    panjang = st.number_input ("Masukan Nilai Panjang")
    lebar = st.number_input ("Masukan Nilai Lebar")
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = panjang * lebar
        st.write ("Luas Persegi Panjang Adalah = ", luas)
        st.succes (f"Luas Persegi Panjang Adalah = {luas}")