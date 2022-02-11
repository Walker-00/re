import streamlit as st
import time
import socket
import requests as r
import json

m = ["Image Processing", "Lyrics", "YouTube video Downloader"]
st.set_option('deprecation.showPyplotGlobalUse', False)


def ch():
    st.sidebar.title("Test Project")
    h = st.sidebar.selectbox("Choose:", m)
    if h == m[1]:
        s = st.text_input("Singer:")
        ss = st.text_input("song: ")
        if st.button("Next", key="next"):
            ro = r.get("https://api.lyrics.ovh/v1/" + s + "/" + ss)
            o = json.loads(ro.text)
            st.text(str(o["lyrics"]))

if __name__ == "__main__":
    ch()
