from streamlit_extras.metric_cards import style_metric_cards 
import streamlit as st
import os
from PIL import Image, ImageDraw
import numpy as np

def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

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
               filter:saturate(4);
            }}
 
        </style>
        <img src="https://www.freeiconspng.com/thumbs/person-icon/grab-vector-graphic-person-icon--imagebasket-13.png" alt="Colorized Photo" class="{colorclass}">
    """

def resize_image(input_path, new_width=None, new_height=None):
    # Open the image file
    original_image = Image.open(input_path)

    if original_image.mode in ("RGBA", "P"): 
        original_image = original_image.convert("RGB")

    # Calculate the aspect ratio
    original_width, original_height = original_image.size
    aspect_ratio = original_width / float(original_height)

    # If only one dimension is provided, calculate the other to maintain the aspect ratio
    if new_width is None:
        new_width = int(aspect_ratio * new_height)
    elif new_height is None:
        new_height = int(new_width / aspect_ratio)

    # Resize the image while keeping the original aspect ratio
    resized_image = original_image.resize((new_width, new_height))

    return resized_image

def display_statistics(stats, cursor):
    # Display statistics using st.write or other appropriate Streamlit components
    column_names = [description[0] for description in cursor.description]

    column_index = {name: index for index, name in enumerate(column_names)}

    date = stats[0][column_index['Date']]
    time = stats[0][column_index['Time']]
    day_of_week = stats[0][column_index['Day of Week Str']]
    duke_ranking = stats[0][column_index['Duke Ranking']]
    temp = stats[0][column_index['temp']]
    weather = stats[0][column_index['weather']]
    event_type = stats[0][column_index['Event Type']]
    category = stats[0][column_index['Category']]
    duke_wl = int(stats[0][column_index['Duke W']])/(int(stats[0][column_index['Duke W']])+int(stats[0][column_index['Duke L']]))

    pred_att = float(stats[0][column_index['Predictions']])

    mygrid = make_grid(3,3)

    mygrid[0][0].metric(label="Date 📆", value=date)
    mygrid[0][1].metric(label="Time ⏰", value=time)
    mygrid[0][2].metric(label="Day of Week 📅", value=day_of_week)
    mygrid[1][0].metric(label="Duke Ranking 🥇", value=duke_ranking)
    mygrid[1][1].metric(label="Temperature 🌡️", value=f"{temp} °C")
    mygrid[1][2].metric(label="Weather 🌤️", value=weather)
    mygrid[2][0].metric(label="Event Type 🎉", value=event_type)
    mygrid[2][1].metric(label="Category 🏟️", value=category)
    mygrid[2][2].metric(label="Duke Win Percentage 🏆", value=f"{round(duke_wl, 2)} %")

    style_metric_cards(border_left_color="#9AD8E1")

    return pred_att 

def display_att(pred_att, total):

    att_per = int((pred_att/total)*100)

    columns = st.columns(20)
    for i in range(100):
        with columns[i % 20]:
            if i<att_per:
                st.markdown(generate_icon("colorized-photo"), unsafe_allow_html=True )
            else:
                st.markdown(generate_icon("greyed-photo"), unsafe_allow_html=True )
    
    st.markdown("***")

    att_col, _, _, _ = st.columns([1.5, 2.25, 0.25, 1.5])

    att_col.header('Attendance 📈', divider='green')
    
    _, sub_col, per_col, _ = st.columns([3, 1.5, 1.5, 3])

    sub_col.metric(":green[Predicted Fans]", f"{int(round(pred_att, 2))} 👤")
    per_col.metric(":green[% of Stadium Filled]", f"{att_per}%")

    style_metric_cards(border_left_color="#3a9c4f")


def init_session_state():
    if 'index' not in st.session_state:
        st.session_state.index = 0

def image_carousel(images, captions):
    
    init_session_state()

    col1, col2, col3 = st.columns(3)
    if col1.button("◀️ Prev"):
        st.session_state.index -= 1
    # col2.write("") 
    if col3.button("Next ▶️"):
        st.session_state.index += 1
        
    st.session_state.index = max(0, min(st.session_state.index, len(images) - 1))
    
    st.image(images[st.session_state.index], caption=captions[st.session_state.index])

    return captions[st.session_state.index]

def img_circle(img):
    height,width = img.size 
    lum_img = Image.new('L', [height,width] , 0) 
    
    draw = ImageDraw.Draw(lum_img) 
    draw.pieslice([(0,0), (height,width)], 0, 360,  
                fill = 255, outline = "white") 
    img_arr =np.array(img) 
    lum_img_arr =np.array(lum_img) 
    final_img_arr = np.dstack((img_arr,lum_img_arr)) 

    return Image.fromarray(final_img_arr)

def display_opp(path, cursor, sport):

    images = os.listdir(path)

    captions = [x[:-4] for x in images]

    images = [f'{path}/{x}' for x in images]

    images = [resize_image(x, new_width=250, new_height=250) for x in images]

    images = [img_circle(x) for x in images]

    opp_col, _, stats_col = st.columns([1, 0.25, 3])
    
    with opp_col:
        opp = image_carousel(images, captions)

    with stats_col:
        cursor.execute(f"SELECT * FROM {sport} WHERE Opponent = '{opp}' ")
        stats = cursor.fetchall()

        pred_att = display_statistics(stats, cursor)

    return pred_att