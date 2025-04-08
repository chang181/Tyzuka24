import streamlit as st
from PIL import Image
import numpy as np
import base64
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Happy Birthday!",
    page_icon="🌹",
    layout="centered"
)

# Add custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f8e1e7;
    }
    .title {
        font-family: 'Arial', sans-serif;
        font-size: 3em;
        color: #FF4B91;
        text-align: center;
    }
    .message {
        font-family: 'Arial', sans-serif;
        font-size: 1.5em;
        color: #333;
        text-align: center;
        margin: 20px 0;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>Happy Birthday!</h1>", unsafe_allow_html=True)

# Display flower image
flower_img = """
<div style="display: flex; justify-content: center; margin: 30px 0;">
    <div style="text-align: center; font-size: 150px;">
        🌹🌸🌺🌷🌹
    </div>
</div>
"""
st.markdown(flower_img, unsafe_allow_html=True)

# Birthday message
st.markdown("""
<div class='message'>
    Wishing you a beautiful day filled with happiness and joy.<br>
    May all your dreams and wishes come true.<br><br>
    With love ❤️
</div>
""", unsafe_allow_html=True)

# Add a simple animation
st.balloons()