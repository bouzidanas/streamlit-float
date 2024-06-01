import json
import logging
import streamlit as st  # 1.34.0
import time
import tiktoken
import os
import sys

from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from streamlit_float import *

st.set_page_config(page_title="Streamlit Chat Interface Improvement",
                   page_icon="🤩")

# initialize float feature/capability
float_init()

from openai import OpenAI  # 1.30.1
# from openai import AzureOpenAI  # 1.30.1

logger = logging.getLogger()
logging.basicConfig(encoding="UTF-8", level=logging.INFO)


st.title("🤩 Improved Streamlit Chat UI")

# Secrets to be stored in /.streamlit/secrets.toml
# OPENAI_API_ENDPOINT = "https://xxx.openai.azure.com/"
# OPENAI_API_KEY = "efpgishhn2kwlnk9928avd6vrh28wkdj" (this is a fake key 😉)

# To be used with standard OpenAI API
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Openai local configuration
load_dotenv(find_dotenv())
try:
    env_openai_key = os.getenv("OPENAI_API_KEY_A")
except:
    sys.stdout.write("No local variables containing OpenAI API credentials found.")

client = OpenAI(api_key = env_openai_key)

# # To be used with standard Azure OpenAI API
# client = AzureOpenAI(
#     azure_endpoint=st.secrets["OPENAI_API_ENDPOINT"],
#     api_key=st.secrets["OPENAI_API_KEY"],
#     api_version="2024-02-15-preview",
# )


# This function logs the last question and answer in the chat messages
def log_feedback(icon):
    # We display a nice toast
    st.toast("Thanks for your feedback!", icon="👌")

    # We retrieve the last question and answer
    last_messages = json.dumps(st.session_state["messages"][-2:])

    # We record the timestamp
    activity = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": "

    # And include the messages
    activity += "positive" if icon == "👍" else "negative"
    activity += ": " + last_messages

    # And log everything
    logger.info(activity)


# Model Choice - Name to be adapter to your deployment
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Adapted from https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps
if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_avatar = "👩‍💻"
assistant_avatar = "🤖"

# In case of rerun of the last question, we remove the last answer from st.session_state["messages"]
if "rerun" in st.session_state and st.session_state["rerun"]:

    st.session_state["messages"].pop(-1)

# We rebuild the previous conversation stored in st.session_state["messages"] with the corresponding emojis
for message in st.session_state["messages"]:
    with st.chat_message(
        message["role"],
        avatar=assistant_avatar if message["role"] == "assistant" else user_avatar,
    ):
        st.markdown(message["content"])

# A chat input will add the corresponding prompt to the st.session_state["messages"]
if prompt := st.chat_input("How can I help you?"):

    st.session_state["messages"].append({"role": "user", "content": prompt})

    # and display it in the chat history
    with st.chat_message("user", avatar=user_avatar):
        st.markdown(prompt)

# If the prompt is initialized or if the user is asking for a rerun, we
# launch the chat completion by the LLM
if prompt or ("rerun" in st.session_state and st.session_state["rerun"]):

    with st.chat_message("assistant", avatar=assistant_avatar):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state["messages"]
            ],
            stream=True,
            max_tokens=300,  # Limited to 300 tokens for demo purposes
        )
        response = st.write_stream(stream)
    st.session_state["messages"].append({"role": "assistant", "content": response})

    # In case this is a rerun, we set the "rerun" state back to False
    if "rerun" in st.session_state and st.session_state["rerun"]:
        st.session_state["rerun"] = False

st.write("")
st.write("")

# If there is at least one message in the chat, we display the options
if len(st.session_state["messages"]) > 0:

    action_buttons_container = st.container()
    action_buttons_container.float("bottom: 6.9rem;background-color: var(--default-backgroundColor); padding-top: 0.9rem;")

    # We set the space between the icons thanks to a share of 100
    cols_dimensions = [7, 19.4, 19.3, 9, 8.6, 8.6, 28.1]
    col0, col1, col2, col3, col4, col5, col6 = action_buttons_container.columns(cols_dimensions)

    with col1:

        # Converts the list of messages into a JSON Bytes format
        json_messages = json.dumps(st.session_state["messages"]).encode("utf-8")

        # And the corresponding Download button
        st.download_button(
            label="📥 Save chat!",
            data=json_messages,
            file_name="chat_conversation.json",
            mime="application/json",
        )

    with col2:

        # We set the message back to 0 and rerun the app
        # (this part could probably be improved with the cache option)
        if st.button("Clear Chat 🧹"):
            st.session_state["messages"] = []
            st.rerun()

    with col3:
        icon = "🔁"
        if st.button(icon):
            st.session_state["rerun"] = True
            st.rerun()

    with col4:
        icon = "👍"

        # The button will trigger the logging function
        if st.button(icon):
            log_feedback(icon)

    with col5:
        icon = "👎"

        # The button will trigger the logging function
        if st.button(icon):
            log_feedback(icon)

    with col6:

        # We initiate a tokenizer
        enc = tiktoken.get_encoding("cl100k_base")

        # We encode the messages
        tokenized_full_text = enc.encode(
            " ".join([item["content"] for item in st.session_state["messages"]])
        )

        # And display the corresponding number of tokens
        label = f"💬 {len(tokenized_full_text)} tokens"
        st.link_button(label, "https://platform.openai.com/tokenizer")

else:

    # At the first run of a session, we temporarly display a message
    if "disclaimer" not in st.session_state:
        with st.empty():
            for seconds in range(3):
                st.warning(
                    "‎ You can click on 👍 or 👎 to provide feedback regarding the quality of responses.",
                    icon="💡",
                )
                time.sleep(1)
            st.write("")
            st.session_state["disclaimer"] = True