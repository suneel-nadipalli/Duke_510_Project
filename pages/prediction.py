import streamlit as st
    
st.title('Prediction Page')

import streamlit.components.v1 as components
import os
import numpy as np

def generate_icon(colorclass):
     return f"""
        <style>
            .greyed-photo, .colorized-photo{{
               width: 60px;
               height: 50px;
            }}
            .greyed-photo {{
               filter: grayscale(100%);
 
            }}
            .colorized-photo{{
               filter:saturate(3);
            }}
 
        </style>
        <img src="https://www.freeiconspng.com/thumbs/person-icon/grab-vector-graphic-person-icon--imagebasket-13.png" alt="Colorized Photo" class="{colorclass}">
    """
 

calendar, time_, opp = st.columns(3)

with calendar:

    st.date_input('Date')

with time_:
    st.time_input('Time')

with opp:
    imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

    # enumerate all the file paths from assets/logos_mf
    imageUrls = [f"logos_mf/{file}" for file in os.listdir("frontend/public/logos_mf")]

    # print(imageUrls)

    selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

    if selectedImageUrl is not None:
        st.image(selectedImageUrl) 


predict = st.button('Predict')
 
# Content for the top column
if predict:
    # generate random number between 0 and 100
    user_input = np.random.randint(1,100)
 
# Content for the bottom column
    with st.container():
        st.markdown('<div class = "custom-div">', unsafe_allow_html=True)
        columns = st.columns(20)
        for i in range(100):
            with columns[i % 20]:
                if i<user_input:
                    st.markdown(generate_icon("colorized-photo"), unsafe_allow_html=True )
                else:
                    st.markdown(generate_icon("greyed-photo"), unsafe_allow_html=True )
        
        st.text("Predicted Number of Students in Attendance " + str(user_input))
        st.text(" Percent of Stadium Filled: " + str(user_input) + "%")