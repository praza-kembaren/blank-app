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
    column1, column2, column3 = st.columns(3)
    column1.markdown("[![Title]('https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg')]('https://www.linkedin.com/in/praza-kembaren')")
    column2.markdown("[![Title]('https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png')]('https://github.com/praza-kembaren')")
    column3.markdown("[![Title]('https://about.x.com/content/dam/about-twitter/x/brand-toolkit/logo-black.png.twimg.1920.png')]('https://x.com/prazakembaren')")

with col2:
    file_ = open("/workspaces/blank-app/file/ezgif.com-speed.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(f'<img src="data:image/gif;base64,{data_url}" width="300" height="300" alt="tco gif">',
    unsafe_allow_html=True,)
 