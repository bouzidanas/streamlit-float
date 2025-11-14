import streamlit as st
from __init__ import *

# Initialize the float functionality
float_init()

st.title("Width Preservation Test")

# Create columns to test width calculation
col1, col2 = st.columns([2, 1])

with col1:
    float_parent()
    st.write("This is column 1 - it should be 66.67% width minus some margin")
    st.write("This container should maintain its original width when floated")
    st.button("Button in floated container")
    st.write("This container uses direct .float() method")
    st.slider("Slider in floated container", 0, 100, 50)

with col2:
    st.write("This is column 2 - it should be 33.33% width")

# Test with direct float method




st.write("---")
st.write("The floated containers above should maintain their original calculated widths, not expand to full screen width.")

# Test float_box as well
float_box(
    "This is a float_box with preserved width",
    top="300px",
    left="20px",
    background="lightgreen"
)