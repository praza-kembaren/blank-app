import streamlit as st
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import base64



# Set up the page
st.set_page_config(page_title="home", page_icon=":milky_way:")
st.header("About Me", divider='rainbow')
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div style="text-align: justify;">Hello, I’m Praza, an Atmospheric and Planetary Sciences grad with a big interest in simulations, exoplanets, and using Python to dive into astronomy. I love exploring data to get new insights into how planets form and what’s out there in our universe.</div>', unsafe_allow_html=True)
  

with col2:
    file_ = open("/workspaces/blank-app/file/ezgif.com-speed.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(f'<img src="data:image/gif;base64,{data_url}" width="250" height="250" alt="tco gif">',
    unsafe_allow_html=True,)
 

# # Add social links or contact
# st.markdown("""
# [LinkedIn](https://www.linkedin.com) | [GitHub](https://www.github.com) | [Twitter](https://www.twitter.com)
# """)