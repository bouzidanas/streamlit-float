import streamlit as st
from streamlit_float import *

t = 'A faster way to build and share data apps'
col1, col2, col3 = st.columns([9, 4, 4])

with col1:
    for i in range(0, 30):
        st.header("Today's news")
        st.write(t)

with col2:
    st.write("Yesterday's news")

with col3:
    st.write("Tomorrow's news")
    float_parent()

col2.float()
