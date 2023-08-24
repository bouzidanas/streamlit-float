import streamlit as st

def float_init():
# add css to streamlit app
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

# adds empty div to parent in order to target it with css
def float_parent():
    st.markdown('<div class="float"></div>', unsafe_allow_html=True)

# float container via its delta generator 
def float(self):
    self.markdown('<div class="float"></div>', unsafe_allow_html=True)

# add float method to st.delta_generator.DeltaGenerator class so it can be directly called
st.delta_generator.DeltaGenerator.float = float