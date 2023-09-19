streamlit-float  [![Version](https://img.shields.io/pypi/v/streamlit-float)](https://pypi.org/project/streamlit-float/#history) 
[![PyPi - Downloads](https://img.shields.io/pypi/dm/streamlit-float)](https://pypi.org/project/streamlit-float/#files)[![Component Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://float-demo.streamlit.app/)
============

Fix the vertical position of Streamlit containers relative to viewport instead of page

## Installation
Install [streamlit-float](https://pypi.org/project/streamlit-float/) with pip:
```bash
pip install streamlit-float
```

## Usage
This package provides two ways to float a container. The first is to call the `float` method of a container:

```python
import streamlit as st
from streamlit_float import *

# initialize float feature/capability
float_init()

col1, col2 = st.columns(2)

# Fix/float the whole column
col1.write("This entire column is fixed/floating")
col1.float()

with col2:
    container = st.container()
    # Fix/float a single container inside
    container.write("This text is in a container that is fixed")
    container.float()

```

Alternatively, you can use the `float_parent` method:

```python
import streamlit as st
from streamlit_float import *

# initialize float feature/capability
float_init()

col1, col2 = st.columns(2)

# Fix/float the whole column
with col1:
    st.write("This entire column is fixed/floating")
    float_parent()

with col2:
    container = st.container()
    # Fix/float a single container inside
    with container:
        st.write("This text is in a container that is fixed")
        float_parent()

```

Note that the float feature does not work well with `expander` and `tabs` containers. Also, it is recommended to call the float methods on a container after all the content has been added to it.

If instead you would like to float/fix a container that is constructed in html markup and added using Streamlits `markdown` method (with `unsafe_allow_html=True`), make sure to add 'floating' to the containers classlist.

```python
st.markdown('''<div class="floating">..content..</div>''', unsafe_allow_html=True)
```

## New features:

### Target floating containers with your own CSS!
You can now add your own CSS to any container you float by providing a string containing the CSS!

Example:
```python
import streamlit as st
from streamlit_float import *

# Float feature initialization
float_init()

# Create footer container and add content
footer_container = st.container()
with footer_container:
    st.markdown("Copyright &copy; 2023 Your Name - All Rights Reserved.")

# Float the footer container and provide CSS to target it with
footer_container.float("bottom: 0;background-color: white;")
```

Currently, both `float` and `float_parent` take a string containing CSS as their only (optional) argument.

### CSS helper function
The `streamlit_float` module now contains a CSS helper function that makes it easier to generate CSS for floating containers programmatically.

Example:
```python
import streamlit as st
from streamlit_float import *

# Float feature initialization
float_init()

# Create footer container and add content
footer_container = st.container()
with footer_container:
    st.markdown("Copyright &copy; 2023 Your Name - All Rights Reserved.")

# Get custom theme background color if set, otherwise default to white
bg_color = st.get_option('theme.backgroundColor')
if bg_color is None:
    bg_color = "white"

# Generate CSS to target the floating footer container
css = float_css_helper(bottom="0", background=bg_color)

# Float the footer container and provide CSS to target it with
footer_container.float(css)
```

### NEW Float Box container

The newly added `float_box` function takes the markdown you provide it and puts it in a newly created floating `div` container. This function also provides direct access (via its arguments) to several CSS parameters/attributes allowing you to easily adjust size, position, background, and border as well as add box-shadows and transitions.

Example:
```python
import streamlit as st
from streamlit_float import *

# Float feature initialization
float_init()

# Initialize session variable that will show/hide Float Box
if "show" not in st.session_state:
    st.session_state.show = True

# Page content
st.markdown(''' ...PAGE CONTENT GOES HERE... ''')

# Container with expand/collapse button
button_container = st.container()
with button_container:
    if st.session_state.show:
        if st.button("⭳", type="primary"):
            st.session_state.show = False
            st.experimental_rerun()
    else:
        if st.button("⭱", type="secondary"):
            st.session_state.show = True
            st.experimental_rerun()
    
# Alter CSS based on expand/collapse state
if st.session_state.show:
    vid_y_pos = "2rem"
    button_b_pos = "21rem"
else:
    vid_y_pos = "-19.5rem"
    button_b_pos = "1rem"

button_css = float_css_helper(width="2.2rem", right="2rem", bottom=button_b_pos, transition=0)

# Float button container
button_container.float(button_css)

# Add Float Box with embedded Youtube video
float_box('<iframe width="100%" height="100%" src="https://www.youtube.com/embed/J8TgKxomS2g?si=Ir_bq_E5e9jHAEFw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',width="29rem", right="2rem", bottom=vid_y_pos, css="padding: 0;transition-property: all;transition-duration: .5s;transition-timing-function: cubic-bezier(0, 1, 0.5, 1);", shadow=12)
```
![streamlit-float-demo4](https://github.com/bouzidanas/streamlit-float/assets/25779130/2ddf3926-2cc4-4628-a35f-a5e25cb319b1)

### NEW Float Dialog container

The `float_dialog` function creates a streamlit container that is manipulated to have the appearance and behavior of a simple dialog box. This function takes a boolean which shows or hides the dialog box.

Example:
```python
import streamlit as st
from streamlit_float import *

# Float feature initialization
float_init()

# Initialize session variable that will open/close dialog
if "show" not in st.session_state:
    st.session_state.show = False

# Button that opens the dialog
if st.button("Contact us"):
        st.session_state.show = True
        st.experimental_rerun()

# Create Float Dialog container
dialog_container = float_dialog(st.session_state.show)

# Add contents of Dialog including button to close it
with dialog_container:
    st.header("Contact us")
    name_input = st.text_input("Enter your name", key="name")
    email_input = st.text_input("Enter your email", key="email")
    message = st.text_area("Enter your message", key="message")
    if st.button("Send", key="send"):
        # ...Handle input data here...
        st.session_state.show = False
        st.experimental_rerun()
```

![streamlit-float-demo5](https://github.com/bouzidanas/streamlit-float/assets/25779130/a8cdc662-03dc-42c9-8c68-804fa64b6a29)

 #### Demo: [![Component Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://float-demo.streamlit.app/)

## License
This project is licensed under the [MIT License](LICENSE.txt)