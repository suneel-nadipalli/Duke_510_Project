import streamlit as st
import numpy as np

st.set_page_config(page_title="Duke Women's Basketball")

st.title("Women's Basketball Attendance Predictions")

option = st.sidebar.selectbox(
   "How would you like to be contacted?",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select contact method...",
)