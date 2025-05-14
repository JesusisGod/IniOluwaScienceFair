# RUN WITH C:\Users\IniOluwa\Streamlit_app\venv\Scripts\python.exe C:\Users\IniOluwa\Streamlit_app\venv\Scripts\streamlit.exe run C:\Users\IniOluwa\Streamlit_app\IniOluwa_2025_Science_Fair\IniOluwa_Ogunbo_2025_Science_Fair_Photo_Log.py
# https://pypi.org/project/streamlit-carousel/

import streamlit as st
from streamlit_carousel import carousel
from PIL import Image
import pandas as pd

st.info('# IniOluwa Ogunbo 2025 Science Fair Photo Log')
st.header('Seoul Central Grade 5 Science Experiment')
st.subheader('Effects of Red, Blue and White light on Plant Growth: Beans and Lettuce')
img = Image.open("IniOluwa_SCI_Photo.jpg")
# #img = Image.open(r"C:\Users\Ogunbo\Documents\Language_subtitles\Jide_Ogunbo_Photo.jpg")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image=img) #,width=300)

# st.image(image=img,width=100)



test_items = [
    dict(
        title="Slide 1",
        text="Materials for planting",
        img="1.jpg",
        
    ),
    dict(
        title="Slide 2",
        text="Containers",
        img="10.jpg",
        
    ),
    dict(
        title="Slide 3",
        text="Lettuce white light container",
        img="2.jpg",
        
    ),
    dict(
        title="Slide 4",
        text="Lettuce red and blue light container",
        img="4.jpg",
        
    ),
    dict(
        title="Slide 5",
        text="Beans blue and red light container",
        img="3.jpg",
        
    ),
    dict(
        title="Slide 6",
        text="Soil",
        img="7.jpg",
        
    ),
    dict(
        title="Slide 7",
        text="Lettuce seeds",
        img="9.jpg",
        
    ),
    dict(
        title="Slide 8",
        text="Water and bean seeds",
        img="11.jpg",
        
    ),
    dict(
        title="Slide 9",
        text="Blue Light",
        img="13.jpg",
        
    ),
    dict(
        title="Slide 10",
        text="Red Light",
        img="14.jpg",
        
    ),
    dict(
        title="Slide 11",
        text="Sprouting",
        img="14a.jpg",
        
    ),
    dict(
        title="Slide 12",
        text="Sprouting Double",
        img="14b.jpg",
        
    ),
    dict(
        title="Slide 13",
        text="Seedling + Red Light",
        img="15.jpg",
        
    ),
    dict(
        title="Slide 14",
        text="Seedling + Red Light in Black Bag",
        img="18.jpg",
        
    ),
    dict(
        title="Slide 15",
        text="Seedling + Blue Light",
        img="20.jpg",
        
    ),
    dict(
        title="Slide 16",
        text="Seedling + Blue Light Side View",
        img="21.jpg",
        
    ),
    dict(
        title="Slide 17",
        text="Seedling + Blue Light in Black Bag",
        img="22.jpg",
        
    ),
    dict(
        title="Slide 18",
        text="Seedling + Blue and Red Light in Black Bags Growing",
        img="23.jpg",
        
    ),
    
    
]
carousel(items=test_items)
st.header("Bean and Lettuce Growth Log")
df = pd.read_csv("Grade_5_Science_Experiment_Log.csv")
#st.dataframe(df.head())
st.dataframe(df, height=None) # To display all rows with scrollbar if needed
