import streamlit as st
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import base64
import time
from datetime import datetime

# Set up the page
st.set_page_config(page_title="home", page_icon=":milky_way:")

st.header("About Me", divider='rainbow')
col1, col2 = st.columns(2)

with col1:
    
    st.markdown('<div style="text-align: justify;">Hello, I’m Praza, an Atmospheric and Planetary Sciences grad with a big interest in creating N-Body simulations, modeling the trajectories or orbits of small solar system bodies, analyzing their orbital evolution and dynamics, and studying exoplanet systems. This website contains my coursework as a student and a few other small astronomy-related topics.</div>', unsafe_allow_html=True)
    st.subheader("Get in touch on me ", divider='rainbow')
    st.markdown("""[LinkedIn](https://www.linkedin.com/in/praza-kembaren) | [GitHub](https://github.com/praza-kembaren) | [Twitter](https://x.com/prazakembaren)""")

with col2:
    file_ = open("/workspaces/blank-app/file/ezgif.com-speed.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(f'<img src="data:image/gif;base64,{data_url}" width="300" height="300" alt="tco gif">',
    unsafe_allow_html=True,)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

cdm = st.Page("/workspaces/blank-app/AstroPython/Comet Destination Map.py", title="Comet Destination Map", icon=":material/dashboard:", default=True)
ci  = st.Page("Meteo/Cloud Identification.py", title="Clouds Identification", icon=":material/bug_report:")
esi = st.Page("Course Work/Earth Similarity Index.py", title="Earth Similarity Index", icon=":material/notification_important:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "AstroPython": [cdm],
            "Meteo": [ci],
            "Course Work": [esi],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
 