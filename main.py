import cv2
import streamlit as st
import time
import socket
import requests as r
import json

m = ["Image Processing", "Lyrics", "YouTube video Downloader"]
st.set_option('deprecation.showPyplotGlobalUse', False)


def ch():
    st.sidebar.title("Test Projest")
    h = st.sidebar.selectbox("Choose:", m)
    if h == m[1]:
        s = st.text_input("Singer:")
        ss = st.text_input("song: ")
        ro = r.get("https://api.lyrics.ovh/v1/" + s + "/" + ss)
        o = json.load(ro.text)
        st.text(o)




