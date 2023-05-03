import streamlit as st
from PIL import Image

st.write("HELLO")
image = Image.open('kids.jpg')

st.image(image, caption='Enjoy this picture of Michelle and Elliot', width=400)