import streamlit as st
from streamlit_option_menu import option_menu


def page_home():
    # Set up HTML and CSS for split background
    split_background_html = f'''
        <style>
            body {{
                margin: 0;
                padding: 0;
            }}

            .split-container {{
                display: flex;
                position:fixed;
                height: 100vh; 
                width: 100vw;
                right: 0;
                bottom: 0;
            }}

            .left-half, .right-half {{
                flex: 1; /* Equal width for both halves */
                background-size: cover; /* Ensure the background image covers the container */
                background-position: center; /* Center the background image */
            }}

            .left-half {{
                background-image: url('https://pbs.twimg.com/media/E46EJvSWYAsZR0C.jpg:large');
            }}

            .right-half {{
                background-image:url('https://c8.alamy.com/comp/2MFMEEW/general-view-of-the-opening-kickoff-between-the-duke-blue-devils-and-the-north-carolina-tar-heels-in-an-empty-stadium-during-the-first-quarter-of-an-ncaa-college-football-game-at-wallace-wade-stadium-saturday-nov-7-2020-in-durham-nc-jim-dedmonpool-photo-via-ap-2MFMEEW.jpg')
            }}
            .team-button-left, .team-button-right{{
                position:relative;
                display: inline-block;
                color: white;

            }}
            .team-button-left {{
                left: 30%;
                top: 30%;
            }}
            .team-button-right {{
                left: 40%;
                top: 30%;
            }}
        </style>
        <div class="split-container">
            <div class="left-half"></div>
            <div class="right-half"></div>
        </div>
    '''

#    Render the split background using st.markdown with unsafe_allow_html=True
    st.markdown(split_background_html, unsafe_allow_html=True)

    duke_image_url = "https://pbs.twimg.com/profile_images/1629164833643048961/Vf2I35Mv_400x400.png"
    duke_image_html = f'''
        <div style=" position: fixed; top: 5%; left:20%; width: 60%; text-align: center;">
            <h2 style="font-style: italic; color:white; text-shadow: 4px 5px 4px rgba(0, 0, 0, 1) "> Forecasting the Fan Wave </h2>
            <h1 style = "color:white; text-shadow: 2px 2px 4px rgba(0, 0, 0, 1)" > Duke Athletics Attendance Prediction</h1>
            <img src="{duke_image_url}" style="width: 40%; height: auto;">
        </div>
    '''
    st.markdown(duke_image_html, unsafe_allow_html=True)
    
      

    # Add an image from a URL
    crowd_image_url = "https://png.pngtree.com/png-clipart/20220804/ourmid/pngtree-audiences-in-club-musical-png-image_6098435.png"

    # Set up HTML and CSS to position the image at the bottom and make it wide
    crowd_image_html = f'''
        <div style="position: fixed; bottom: -15%; left: 0; width: 100%; text-align: center;">
            <img src="{crowd_image_url}" style="width: 100%; height: auto;">
        </div>
    '''

    # Render the image using st.markdown with unsafe_allow_html=True
    st.markdown(crowd_image_html, unsafe_allow_html=True)

def main():

    st.set_page_config( page_title="Home")

    page_home()


if __name__ == "__main__":
    main()