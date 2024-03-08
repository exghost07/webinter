import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from page4 import page_4

# import pandas as pd
# import matplotlib.pyplot as plt
# st.write("Labra24 rev")
# df = pd.DataFrame({
#   'No': [1, 2, 3, 4],
#   'Nama': ['Asep','Alul','Hansen','viny'],
#   'Nilai': [95, 97, 98, 98]
# })

# df


PAGES = {
    "Page1" : page_1,
    "Page2" : page_2, 
    "Page3" : page_3,
    "Page4" : page_4
  }
  
st.sidebar.image("popeye.png", width=100)
page = st.sidebar.radio("Pages List :", list(PAGES.keys()))
PAGES[page]()