import streamlit as st
import datetime
import time
import random
from PIL import Image
import numpy as np
import base64
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Happy Birthday!",
    page_icon="🎂",
    layout="wide"
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        .birthday-title {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            font-size: 4em;
            text-align: center;
            color: #FF4B91;
            text-shadow: 3px 3px 5px rgba(0,0,0,0.2);
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .message-box {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin: 20px 0;
        }
        .btn-primary {
            background-color: #FF4B91 !important;
            border-color: #FF4B91 !important;
            color: white !important;
            font-weight: bold !important;
        }
        .birthday-message {
            font-size: 1.5em;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            color: #333;
        }
        .confetti {
            position: fixed;
            width: 10px;
            height: 10px;
            background-color: #f00;
            border-radius: 50%;
            animation: fall 5s linear infinite;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Function to create a confetti animation effect
def confetti_animation():
    confetti_html = ""
    colors = ["#f00", "#0f0", "#00f", "#ff0", "#f0f", "#0ff"]
    for i in range(100):
        color = random.choice(colors)
        left = random.randint(0, 100)
        size = random.randint(5, 15)
        duration = random.uniform(3, 8)
        delay = random.uniform(0, 5)
        
        confetti_html += f"""
        <div class="confetti" style="
            left: {left}%;
            width: {size}px;
            height: {size}px;
            background-color: {color};
            animation: fall {duration}s linear {delay}s infinite;
            opacity: {random.uniform(0.6, 1.0)};
            "></div>
        """
    
    st.markdown(f"""
    <style>
        @keyframes fall {{
            0% {{ top: -10%; transform: rotate(0deg); }}
            100% {{ top: 100%; transform: rotate(360deg); }}
        }}
    </style>
    {confetti_html}
    """, unsafe_allow_html=True)

# Birthday cake function
def get_cake_animation():
    cake_html = """
    <div style="text-align: center; margin: 20px 0;">
        <div style="font-size: 100px; animation: flame 1s infinite alternate">
            🔥
        </div>
        <div style="font-size: 120px;">
            🎂
        </div>
    </div>
    <style>
        @keyframes flame {
            0% { transform: scale(1); }
            100% { transform: scale(1.2); }
        }
    </style>
    """
    return cake_html

# Generate hearts animation
def generate_hearts_animation():
    hearts_html = ""
    for i in range(40):
        left = random.randint(0, 100)
        animation_duration = random.uniform(3, 8)
        delay = random.uniform(0, 5)
        font_size = random.randint(15, 40)
        
        hearts_html += f"""
        <div style="
            position: fixed;
            left: {left}%;
            top: -10%;
            color: rgba(255, 20, 147, 0.7);
            font-size: {font_size}px;
            animation: float {animation_duration}s linear {delay}s infinite;
            ">❤️</div>
        """
    
    st.markdown(f"""
    <style>
        @keyframes float {{
            0% {{ top: -10%; transform: translateY(0) rotate(0deg); }}
            100% {{ top: 100%; transform: translateY(0) rotate(360deg); }}
        }}
    </style>
    {hearts_html}
    """, unsafe_allow_html=True)

# Main app
def main():
    # Add confetti effect
    confetti_animation()
    
    # Hearts animation
    generate_hearts_animation()
    
    # Title with animation
    st.markdown("<h1 class='birthday-title'>Happy Birthday!</h1>", unsafe_allow_html=True)
    
    # Get boyfriend's name
    boyfriend_name = st.text_input("Enter your boyfriend's name:", "")
    
    if boyfriend_name:
        # Birthday message
        st.markdown(f"<div class='birthday-message message-box'>Dear {boyfriend_name},<br><br>"
                    f"On this special day, I want to celebrate you and all the joy you bring into my life. "
                    f"You make every day brighter just by being you. I'm so grateful for your love, "
                    f"your smile, and all the wonderful memories we've created together.<br><br>"
                    f"Happy Birthday, my love! Here's to many more years of happiness together!<br><br>"
                    f"With all my love ❤️</div>", unsafe_allow_html=True)
        
        # Birthday cake
        st.markdown(get_cake_animation(), unsafe_allow_html=True)
        
        # Add a countdown timer
        st.markdown("<h3 style='text-align: center;'>Celebrating your special day in:</h3>", unsafe_allow_html=True)
        
        countdown_placeholder = st.empty()
        
        # Custom birthday messages
        messages = [
            "You are amazing!",
            "You light up my world!",
            "Every day with you is a gift!",
            "You mean everything to me!",
            "You're my favorite person!",
            "I cherish every moment with you!",
            "You make me smile every day!"
        ]
        
        # Loop for the countdown and messages
        for i in range(10, 0, -1):
            countdown_placeholder.markdown(f"<h1 style='text-align: center;'>{i}</h1>", unsafe_allow_html=True)
            # Show random message
            st.markdown(f"<h3 style='text-align: center; color: #FF4B91;'>{random.choice(messages)}</h3>", 
                       unsafe_allow_html=True)
            time.sleep(1)
        
        countdown_placeholder.markdown("<h1 style='text-align: center; color: #FF4B91;'>Happy Birthday!!! 🎉🎉🎉</h1>", 
                                    unsafe_allow_html=True)
        
        # Photo gallery
        st.markdown("<h2 style='text-align: center; margin-top: 30px;'>Our Memories Together</h2>", 
                  unsafe_allow_html=True)
        
        # Instructions for adding photos
        st.markdown("<div class='message-box'>Add your favorite photos below to create a gallery of memories.</div>", 
                  unsafe_allow_html=True)
        
        uploaded_files = st.file_uploader("Choose photos to add to the gallery", 
                                         type=["jpg", "jpeg", "png"], 
                                         accept_multiple_files=True)
        
        if uploaded_files:
            cols = st.columns(3)
            for i, file in enumerate(uploaded_files):
                img = Image.open(file)
                with cols[i % 3]:
                    st.image(img, use_column_width=True, caption=f"Memory #{i+1}")
        
        # Birthday wishes
        st.markdown("<h2 style='text-align: center; margin-top: 30px;'>Birthday Wishes</h2>", 
                  unsafe_allow_html=True)
        
        custom_message = st.text_area("Write a special birthday wish:", 
                                    "You make every day special just by being you. I love you more than words can express!")
        
        if st.button("Send Birthday Wishes", key="send_wishes"):
            st.balloons()
            st.success("Your birthday wishes have been sent with love! ❤️")
            
            # Display the message in a fancy way
            st.markdown(f"""
            <div style='background: linear-gradient(45deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%); 
                       padding: 20px; border-radius: 10px; margin-top: 20px;'>
                <p style='font-size: 1.2em; color: #333; text-align: center;'>{custom_message}</p>
                <p style='text-align: right; font-style: italic;'>With love, to {boyfriend_name} ❤️</p>
            </div>
            """, unsafe_allow_html=True)
    
    else:
        st.markdown("<div class='message-box'>Enter your boyfriend's name to start the celebration!</div>", 
                  unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()