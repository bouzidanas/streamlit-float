import streamlit as st
from __init__ import *
import streamlit_antd_components as sac
from streamlit_option_menu import option_menu

st.set_page_config(page_title='streamlit-float demo', initial_sidebar_state='collapsed')

float_init()

if "show" not in st.session_state:
    st.session_state.show = False

# Function to navigate to a new page
# An improvement here would be to open in new tab
def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("# streamlit-float")

st.image("https://github.com/bouzidanas/streamlit-float/assets/25779130/6543e315-3e42-4f11-b4a5-939853f2a048")
st.markdown('''# Large Language Models

Large language models, such as GPT-3 and BERT, have revolutionized natural language processing. These models are trained on massive amounts of text data and can generate human-like text, answer questions, and perform various language-related tasks. They have been used in a wide range of applications, including chatbots, language translation, and content generation. The advancements in large language models have opened up new possibilities for improving communication and understanding between humans and machines.

## The beginning

The beginning of large language models can be traced back to the development of the Transformer model by Vaswani et al. in 2017. This model introduced the concept of self-attention, which allows the model to capture long-range dependencies in text and greatly improves its ability to understand and generate coherent sentences. Since then, researchers and engineers have built upon this foundation to create even larger and more powerful language models like GPT-3 and BERT.

One of the key challenges in developing large language models is the computational resources required for training and inference. Training these models often involves using thousands of GPUs and weeks or even months of compute time. Additionally, the size of these models can make them difficult to deploy and run on resource-constrained devices. However, advancements in hardware and distributed computing have made it possible to train and use these models at scale, opening up new opportunities for natural language processing.

## Enter the big players

The big players in AI, such as Microsoft, Google, and Facebook, have played a crucial role in bringing the resources needed to accelerate progress in large language models (LLMs). These companies have invested heavily in research and development, as well as in building the necessary infrastructure to train and deploy these models.

Microsoft, for example, has made significant contributions to the field of natural language processing through projects like Microsoft Research NLP and the development of the Turing NLG language model. They have also developed Azure Machine Learning, a cloud-based platform that provides the computational resources and tools needed to train and deploy large language models at scale.

Google, on the other hand, has been at the forefront of LLM research with projects like Google Brain and Google Research. They have developed models like BERT and T5, which have achieved state-of-the-art performance on a wide range of natural language processing tasks. Google's cloud platform, Google Cloud, provides the infrastructure and tools necessary for training and deploying large language models.

Meta has also made significant contributions to the field of natural language processing through projects like PyTorch and the development of models like RoBERTa. They have also invested in building powerful computing infrastructure, such as the FAIR (Facebook AI Research) cluster, which enables researchers to train and experiment with large language models.

These companies have not only brought the necessary computational resources to the table but have also contributed to the research and development of novel techniques and architectures for improving the performance and efficiency of large language models. Their contributions have helped to push the boundaries of what is possible in natural language processing and have accelerated progress in the field.

## Llama 2: Partnership between Microsoft and Meta

Llama 2 is a collection of open-source large language models (LLMs) developed by Meta AI. The models range in size from 7 billion to 70 billion parameters and are designed to perform well on various language processing tasks. Llama 2 is available for free for research and commercial use. 
Llama 2 is the result of a partnership between Meta and Microsoft. The models are optimized for dialogue use cases and can be used to create a ChatGPT-like chatbot. 

Llama 2 is considered a game-changer for the adoption and commercialization of LLMs because of its comparable performance with much larger models and its permissive open-source license. The license allows the use and distribution of Llama 2 in commercial applications. 

Meta has also introduced Code Llama, a large language model that can generate code from text prompts.
            
## Getting started with Llama 2

To get started with Llama 2, you need to fill out the access form on Meta's website and wait for a confirmation email. Once access is granted, you can:

- Visit llama2.ai to interact with the chatbot demo.
- Download the Llama 2 code.
- Access Llama 2 through Microsoft Azure or Amazon SageMaker JumpStart.
- Try a variant at llama.perplexity.ai.

You can also run Llama 2 locally. To do this, you can: 

- Download the Llama 2 model in GGML format from Hugging Face.
- Install the latest version of Python.
- Prepare the Python environment.
- Interact with the Llama 2 large language model.

Facebook researchers say that Llama 2 models perform better than existing open-source models. They also say that Llama 2 models are close behind closed-source models like ChatGPT.\n
''')
st.warning("**DISCLAIMER!** The majority of this psuedo-article was generated by AI. Information may be inaccurate or misleading. Tools such as [Markdown Composer](https://markdown-composer.streamlit.app/) and Google's [Generative AI search](https://blog.google/products/search/generative-ai-search/) were used to create this article.")

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
    button_b_pos = "21.3rem"
else:
    vid_y_pos = "-19.5rem"
    button_b_pos = "1rem"

button_css = float_css_helper(width="2.2rem", right="2rem", bottom=button_b_pos, transition=0)

button_container.float(button_css)
float_box('<iframe width="100%" height="100%" src="https://www.youtube.com/embed/J8TgKxomS2g?si=Ir_bq_E5e9jHAEFw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',width="29rem", right="2rem", bottom=vid_y_pos, transition=0, shadow=12, css="padding: 0;")


# Initialize session variable that will open/close dialog
if "dialog" not in st.session_state:
    st.session_state.dialog = False

# Button that opens the dialog
if st.button("Contact us"):
    st.session_state.dialog = True
    st.experimental_rerun()

# Create Float Dialog container
dialog_container = float_dialog(st.session_state.dialog, background="var(--default-backgroundColor)")

# Add contents of Dialog including button to close it
with dialog_container:
    st.header("Contact us")
    name_input = st.text_input("Enter your name")
    email_input = st.text_input("Enter your email")
    message = st.text_area("Enter your message")
    if st.button("Send", key="send"):
        st.session_state.dialog = False
        st.experimental_rerun()

# Create a menu container
menu_container = st.container()

# Add option menu to menu container
with menu_container:
    menu_selection = option_menu(None, ["Home", "Tutorial", "Video", 'Contact'], 
    icons=['house', 'people', 'play-btn', "chat-square-text"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0.2rem 0", "background-color": "#22222200"},
           })

# Handle menu selection
if menu_selection == "Contact":
    st.session_state.menusel = 3
    if not st.session_state.dialog:
        st.session_state.dialog = True
        st.experimental_rerun()
    else:
        st.session_state.dialog = False
elif menu_selection == "Video":
    st.session_state.menusel = 2
    if not st.session_state.show:
        st.session_state.show = True
        st.experimental_rerun()    
elif menu_selection == "Home":
    st.session_state.menusel = 0

# Float menu container
menu_container.float("top: 0.15rem;z-index: 999990;")

# Create a floating links
float_box('<a href="https://pypi.org/project/streamlit-float/">PYPI</a>・<a href="https://github.com/bouzidanas/streamlit-float">Github</a>・<a href="https://discuss.streamlit.io/t/anybody-interested-in-simple-component-to-float-containers/45013?u=bouzidanas">Community</a> ', width="fit-content", height="2rem", right="-5.6rem", top="12rem", background="transparent", css="flex-direction: row;align-items: center;color: #ffffff99;rotate: 90deg;")

# Create a banner container
banner_container = st.container()

# Add alert banner to banner container
with banner_container:
    sac.alert(message='**WARNING! This is a demo. This is not a real article.**', description=None, type='warning', height=None, icon=True, closable=True, banner=True)

# Float banner container
banner_container.float("bottom: -1rem;z-index: 999992;")

# Custom styles for floating links
# Note Float box container has "floating" class
style = '''<style>
.floating a {
    color: var(--default-textColor);
    opacity: 0.4;
    text-decoration: none;
}
.floating a:hover {
    color: var(--default-textColor)!important;
    opacity: 1;
}
</style>'''
st.markdown(style, unsafe_allow_html=True)