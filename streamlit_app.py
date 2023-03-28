import requests
import streamlit as st

st.title("Webhook Client")
url = st.text_input("Webhook URL", "")
payload = st.text_input("JSON Payload", "")

if st.button("Submit"):
    if not url.strip() == "":
        response = requests.post(url, data = payload)
        st.write(f"Response: {response.text}")
    else:
        st.write(f"Response: Please provide the Webhook URL.")
