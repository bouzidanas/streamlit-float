import streamlit as st

html_style = '''
<style>
div:has( >.element-container div.float) {
    display: flex;
    flex-direction: column;
    position: fixed;
}
div.float {
    height:0%;
}
div.floating {
    display: flex;
    flex-direction: column;
    position: fixed;
}
</style>
'''
st.markdown(html_style, unsafe_allow_html=True)

def float(container):
    with container:
        st.markdown('<div class="float"></div>', unsafe_allow_html=True)