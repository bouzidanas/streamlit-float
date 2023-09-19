import streamlit as st
from __init__ import *

float_init()

# cola, colb = st.columns([2, 1])

# with cola:    
#     dialog_container = st.container()
#     with dialog_container:
#         st.text_input("Enter your name", key="name")
#         st.text_area("Enter your message", key="message")
#         if st.button("Send", key="send"):
#             st.experimental_rerun()

# float_box("", width="100%", height="100%", left="0", top="0", background="rgba(0, 0, 0, 0.5)", css="z-index: 999000;")
# cola.float("padding: 2rem;left: 50%;top: 2.8rem;transform: translateX(-50%);;background-color: slategray;z-index: 999900;")

if "dialog" not in st.session_state:
    st.session_state.dialog = True

dialog = float_dialog(st.session_state.dialog, width=3)

with dialog:
    st.header("Contact us")
    name_input = st.text_input("Enter your name", key="name")
    email_input = st.text_input("Enter your email", key="email")
    message = st.text_area("Enter your message", key="message")
    if st.button("Send", key="send"):
        st.session_state.dialog = False
        st.experimental_rerun()

t = 'A faster way to build and share data apps'
col1, col2, col3 = st.columns([9, 4, 4])

with col1:
    if st.button("Click me"):
        st.session_state.dialog = True
        st.experimental_rerun()
    for i in range(0, 30):
        st.header("Today's news")
        st.write(t)

with col2:
    st.write("Yesterday's news")
    cont=st.container()
    cont.write("moved container")
    cont.float("top: 4rem;left: 6rem")

with col3:
    st.write("Tomorrow's news &copy;")

    float_box("This is a floating box", left="2px", background="black", border="1px solid rgba(250, 250, 250, 0.2)")

test_css = float_css_helper(css={"color": "red", "font-size": "2rem"}, background_color="blue")
st.write(test_css)