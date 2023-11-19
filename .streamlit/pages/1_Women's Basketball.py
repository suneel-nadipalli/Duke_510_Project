import streamlit as st
import numpy as np

st.set_page_config(page_title="Duke Women's Basketball")

st.title("Women's Basketball Attendance Predictions")

#option = st.sidebar.selectbox(
   #"How would you like to be contacted?",
   #("Email", "Home phone", "Mobile phone"),
   #index=None,
   #placeholder="Select contact method...",
#)

st.sidebar.title("1. Data")


tab1, tab2, tab3 = st.tabs(["Datasets", "EDA", "Modeling and Predictions"])

with tab1:
   st.header("Data")

with tab2:
   st.header("Exploratory Data Analysis")

with tab3:
   st.header("Modeling & Predictions")

