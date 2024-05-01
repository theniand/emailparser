
import streamlit as st
import utilities.utils as utils
from openai import OpenAI

st.divider()
st.write("Here is a sample email to copy:" + utils.getSampleEmail())
st.divider()

st.title("Email Parser")

client = OpenAI(api_key="")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
 
if prompt := st.chat_input("Enter the email for the ai to parse"):
    st.session_state.messages.append({"role": "system", "content": utils.getContent()})
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
