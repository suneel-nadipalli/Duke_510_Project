import streamlit as st

def page_home():
 
    duke_image_url = "https://pbs.twimg.com/profile_images/1629164833643048961/Vf2I35Mv_400x400.png"
    duke_image_html = f'''
        <div style=" position: fixed; top: 3%; left:20%; width: 60%; text-align: center;">
            <h1 align = "center"> Duke Athletics Attendance Prediction Model</h1>
            <img src="{duke_image_url}" style="width: 30%; height: auto;">
        </div>
    '''
    st.markdown(duke_image_html, unsafe_allow_html=True)


    # Add an image from a URL
    crowd_image_url = "https://png.pngtree.com/png-clipart/20220804/ourmid/pngtree-audiences-in-club-musical-png-image_6098435.png"

    # Set up HTML and CSS to position the image at the bottom and make it wide
    crowd_image_html = f'''
        <div style="position: fixed; bottom: 0; left: 0; width: 100%; text-align: center;">
            <img src="{crowd_image_url}" style="width: 100%; height: auto;">
        </div>
    '''

    # Render the image using st.markdown with unsafe_allow_html=True
    st.markdown(crowd_image_html, unsafe_allow_html=True)
    
def page_mission():
    st.title("Our Purpose for our model")

def page_WB():
    st.title("Women's Basketball Attendance Predictions")

def page_MF():
    st.title("Men's Football Attendance Predictions")

def style_pages():
    pass

def main():

    
    # Sidebar navigation buttons
    nav_selection = st.sidebar.radio("Select Page", ["Home", "Our Mission", "Women's Basketball", "Men's Football"])

    # Main content based on user's selection
    if nav_selection == "Home":
        page_home()
    if nav_selection == "Our Mission":
        page_mission()
    elif nav_selection == "Women's Basketball":
        page_WB()
    elif nav_selection == "Men's Football":
        page_MF()

if __name__ == "__main__":
    main()