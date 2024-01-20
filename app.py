import pyshorteners
import streamlit as st


def shorten_rl(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

st.set_page_config(page_title="URL Shortener", page_icon="✅", layout="centered")
st.image("images/wf.png", use_column_width=True)
st.title("URL Shortener")
url = st.text_input("Enter the uRL")
if st.button("Generate new Url"):
    st.write("URL shorteaned: ", shorten_rl(url))