import streamlit as st
import sqlite3
from utils import display_opp, display_att
import os

def connect():
    db_path = os.path.join(os.path.dirname(__file__), 'UI', 'db', 'attendance.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return cursor, conn

def main():

    cursor, conn = connect()

    st.set_page_config(page_title="Prediction", page_icon=None, layout="wide", initial_sidebar_state="auto")

    st.title('Prediction Page')

    sub_col, sport_col, _, _ = st.columns([2.0, 1.80, 2.0, 2.5])

    with sub_col:
        st.header("Choose Sport 🏀/🏉",  divider='blue')
    with sport_col:
        sport = st.selectbox('', ["Men's Football", "Women's Basketball"], index=None)

    st.header('Choose Oponent 🤼‍♂️', divider='blue')

    if sport == "Men's Football":

        pred_att = display_opp('assets/logos_mf', cursor, 'mens_football')

    elif sport == "Women's Basketball":

        pred_att = display_opp('assets/logos_wb', cursor, 'womens_basketball')

    
    st.subheader("", divider="blue")

    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #55a8f2;
        color:#ffffff;
        width: 200px;
        height: 50px;
        border-radius: 10px;
        font-size: 25px;
    }
    </style>""", unsafe_allow_html=True)

    if st.button("Predict"):
        with st.container():
            if sport == "Men's Football":
                display_att(pred_att, 40004)
            elif sport == "Women's Basketball":
                display_att(pred_att, 9314)

if __name__ == '__main__':
    main()
