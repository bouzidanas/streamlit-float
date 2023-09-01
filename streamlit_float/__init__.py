import streamlit as st
import uuid

def float_init():
# add css to streamlit app
    html_style = '''
    <style>
    div:has( >.element-container div.float) {
        display: flex;
        flex-direction: column;
        position: fixed;
        z-index: 99;
    }
    div.float {
        height:0%;
    }
    div.floating {
        display: flex;
        flex-direction: column;
        position: fixed;
        z-index: 99; 
    }
    </style>
    '''
    st.markdown(html_style, unsafe_allow_html=True)

# adds empty div to parent in order to target it with css
def float_parent(css=None):
    if css is not None:
        new_id = str(uuid.uuid4())[:8]
        new_css = '<style>\ndiv:has( >.element-container div.flt-' + new_id + ') {' + css + '}\n</style>'
        st.markdown(new_css, unsafe_allow_html=True)
        st.markdown('<div class="float flt-' + new_id + '"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="float"></div>', unsafe_allow_html=True)

# float container via its delta generator 
def float(self, css=None):
    if css is not None:
        new_id = str(uuid.uuid4())[:8]
        new_css = '<style>\ndiv:has( >.element-container div.flt-' + new_id + ') {' + css + '}\n</style>'
        st.markdown(new_css, unsafe_allow_html=True)
        self.markdown('<div class="float flt-' + new_id + '"></div>', unsafe_allow_html=True)
    else:
        self.markdown('<div class="float"></div>', unsafe_allow_html=True)

# add float method to st.delta_generator.DeltaGenerator class so it can be directly called
st.delta_generator.DeltaGenerator.float = float