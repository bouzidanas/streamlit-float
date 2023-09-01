import streamlit as st
import uuid

# list containing various types of box-shadow implementations (source: https://getcssscan.com/css-box-shadow-examples)
shadow_list = ["box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;", 
               "box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;", 
               "box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;",
               "box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;",
               "box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;",
               "box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;",
               "box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;",
               "box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px, rgb(51, 51, 51) 0px 0px 0px 3px;",
               "box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px, rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;",
               "box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;",
               "box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;",
               "box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;",
               "box-shadow: rgba(0, 0, 0, 0.16) 0px 10px 36px 0px, rgba(0, 0, 0, 0.06) 0px 0px 0px 1px;",
               "box-shadow: rgba(17, 12, 46, 0.15) 0px 48px 100px 0px;",
               "box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;",
               "box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;",
               "box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;",
               "box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;",
               "box-shadow: rgba(50, 50, 93, 0.25) 0px 13px 27px -5px, rgba(0, 0, 0, 0.3) 0px 8px 16px -8px;",
               "box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;",
               "box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;",
               "box-shadow: rgba(6, 24, 44, 0.4) 0px 0px 0px 2px, rgba(6, 24, 44, 0.65) 0px 4px 6px -1px, rgba(255, 255, 255, 0.08) 0px 1px 0px inset;",
               "box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;",
               "box-shadow: rgba(50, 50, 93, 0.25) 0px 13px 27px -5px, rgba(0, 0, 0, 0.3) 0px 8px 16px -8px;",
               "box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px;",
               "box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;",
               "box-shadow: rgba(17, 17, 26, 0.1) 0px 4px 16px, rgba(17, 17, 26, 0.05) 0px 8px 32px;"
               ]

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

# create a floating box containing markdown content
def float_box(markdown, width="300px", height="300px", top=None, left=None, right=None, bottom=None, background=None, border=None, shadow=None, css=None):
    jct_css = "width: " + width + "; height: " + height + ";border-radius: 0.5rem;padding: 1rem;padding-left: 1.3rem;padding-right: 1.3rem;"
    if shadow is not None and type(shadow) is int and shadow < len(shadow_list) and shadow >= 0:
        jct_css += shadow_list[int(shadow)]
    if border is not None:
        jct_css += "border: " + border + ";"
    if background is not None:
        jct_css += "background-color: " + background + ";"
    if top is not None:
        jct_css += "top: " + top + ";"
    if left is not None:
        jct_css += "left: " + left + ";"
    if right is not None:
        jct_css += "right: " + right + ";"
    if bottom is not None:
        jct_css += "bottom: " + bottom + ";"
    if css is not None:
        jct_css += css

    new_id = str(uuid.uuid4())[:8]
    new_css = '<style>\ndiv.flt-' + new_id + ' {' + jct_css + '}\n</style>'
    st.markdown(new_css, unsafe_allow_html=True)
    st.markdown('<div class="floating flt-' + new_id + '">' + markdown + '</div>', unsafe_allow_html=True)

# helper function to create css string
def float_css_helper(width=None, height=None, top=None, left=None, right=None, bottom=None, background=None, border=None, shadow=None, css=None):
    jct_css = ""
    if width is not None:
        jct_css += "width: " + width + ";"
    if height is not None:
        jct_css += "height: " + height + ";"
    if shadow is not None and type(shadow) is int and shadow < len(shadow_list) and shadow >= 0:
        jct_css += shadow_list[int(shadow)]
    if border is not None:
        jct_css += "border: " + border + ";"
    if background is not None:
        jct_css += "background-color: " + background + ";"
    if top is not None:
        jct_css += "top: " + top + ";"
    if left is not None:
        jct_css += "left: " + left + ";"
    if right is not None:
        jct_css += "right: " + right + ";"
    if bottom is not None:
        jct_css += "bottom: " + bottom + ";"
    if css is not None:
        jct_css += css
    return jct_css

# add float method to st.delta_generator.DeltaGenerator class so it can be directly called
st.delta_generator.DeltaGenerator.float = float