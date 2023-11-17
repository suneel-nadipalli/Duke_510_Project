import streamlit as st
import numpy as np

st.set_page_config(page_title="Duke Men's Football")

st.title("Men's Football Attendance Predictions")

option = st.sidebar.selectbox(
   "How would you like to be contacted?",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select contact method...",
)