import streamlit as st
import requests

# Start Webpage
st.set_page_config(page_title="API Request", page_icon="🚀")

def get_output(prompt, temperature, top_p, max_tokens, api_url):
    params = {
        'prompt': prompt,
        'temperature': temperature,
        'top_p': top_p,
        'max_tokens': max_tokens,
    }
    response = requests.post(
        api_url,
        json=params
    )
    return response.json()['output']


# Build
with st.container():
    # Header
    st.write("[https://github.com/beckerfelipee](https://github.com/beckerfelipee)")
    st.title('API Request :blue[User Interface]', anchor=False)
    api_url = st.text_input("API URL")

    # API Body
    if api_url != "":

        try:
            response = requests.get(api_url)
            st.write(":green[Connected] ✅")
            status = response.json()['status']
            if status == "NLP ready!":
                st.subheader('Natural Language Processing API - @beckerfelipee', anchor=False)
                with st.container():
                    c1, c2, c3 = st.columns(3)
                    temperature = c1.number_input("Temperature", value=0.7, min_value=0.0, max_value=2.0, step=0.1)
                    top_p = c2.number_input("Top P", value=0.9, min_value=0.0, max_value=1.0, step=0.1)
                    max_tokens = c3.number_input("Max Tokens", value=100, min_value=10, max_value=500, step=5)
                messages = st.container(height=300)
                if prompt := st.chat_input("Say something", max_chars=100):
                    messages.chat_message("user").write(prompt)
                    st.toast("Thinking..")
                    output = get_output(prompt, temperature, top_p, max_tokens, api_url)
                    messages.chat_message("assistant").write(output)

        except requests.exceptions.RequestException as e:
            st.write(f":red[{e}]")





