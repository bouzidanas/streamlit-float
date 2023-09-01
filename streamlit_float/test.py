import streamlit as st
from __init__ import *

float_init()

t = 'A faster way to build and share data apps'
col1, col2, col3 = st.columns([9, 4, 4])

with col1:
    for i in range(0, 30):
        st.header("Today's news")
        st.write(t)

with col2:
    st.write("Yesterday's news")
    cont=st.container()
    cont.write("moved container")
    cont.float("top: 4rem;left: 6rem")

with col3:
    st.write("Tomorrow's news")
    float_parent("bottom: 4rem;left: 6rem")