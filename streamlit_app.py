import streamlit as st
import numpy as np
import pandas as pd


st.header("Introduction", divider='rainbow')
st.write(
    "Hallo, Wellcome to my personal website, hehe"
)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)