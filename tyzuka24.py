import streamlit as st
import time
import os
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Happy Birthday Celebration",
    page_icon="🎂",
    layout="centered"
)

# Custom CSS to style the app
st.markdown("""
<style>
    .main {
        padding: 2rem;
        border-radius: 10px;
    }
    .stButton button {
        width: 100%;
        border-radius: 5px;
        font-size: 18px;
        padding: 10px;
        border: 2px solid #f0bb33;
        background-color: white;
        color: #333;
    }
    .stButton button:hover {
        background-color: #f0bb33;
        color: white;
    }
    .big-header {
        font-size: 28px;
        font-weight: bold;
        color: #333;
    }
    .center-text {
        text-align: center;
    }
    .gift-container {
        border: 2px solid #f0bb33;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
    }
    .number-box {
        width: 60px;
        height: 60px;
        border: 2px solid #f0bb33;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
    }
    .input-box {
        border: 2px solid #f0bb33;
        border-radius: 5px;
        padding: 10px;
    }
    .birthday-page {
        background-color: #fff9e6;
        padding: 30px;
        border-radius: 10px;
        border: 3px solid #f0bb33;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'A'
if 'wishes' not in st.session_state:
    st.session_state.wishes = ""

# Function to navigate pages
def navigate_to(page):
    st.session_state.page = page
    
# Function to check password
def check_password(password):
    # This could be any name you want to set as the password
    correct_password = "Ty"
    if password.lower() == correct_password.lower():
        return True
    return False

# Function to save wish
def save_wish(wish):
    st.session_state.wishes = wish
    navigate_to('birthday')

# Page A - Welcome Page
if st.session_state.page == 'A':
    st.markdown('<p class="big-header center-text">Anh Ty, iu, ơi...</p>', unsafe_allow_html=True)
    
    # Next button
    col1, col2, col3 = st.columns([2, 2, 1])
    with col3:
        if st.button("Next"):
            navigate_to('B')

# Page B - Choice Page
elif st.session_state.page == 'B':
    st.markdown('<p class="big-header center-text">Happy Tyżuka 24+</p>', unsafe_allow_html=True)
    st.markdown('<p class="center-text">Có 2 ô để lựa chọn cho anh Ty:</p>', unsafe_allow_html=True)
    
    # Option buttons layout
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col2:
        st.markdown('<div class="number-box center-text">1</div>', unsafe_allow_html=True)
        if st.button("Next to Option 1"):
            navigate_to('1')
    
    with col3:
        st.markdown('<div class="number-box center-text">2</div>', unsafe_allow_html=True)
        if st.button("Next to Option 2"):
            navigate_to('2')

# Page 1 - Write Wishes
elif st.session_state.page == '1':
    st.markdown('<p class="big-header">A Ty uơc 1 điều iii,</p>', unsafe_allow_html=True)
    st.markdown('<p>(không an gian, không uơc xammm)</p>', unsafe_allow_html=True)
    
    # Text area for wishes
    wishes = st.text_area("Type your wishes here:", height=100, key="wish_input")
    
    col1, col2 = st.columns([3, 1])
    
    # Return to B button
    with col2:
        if st.button("Return"):
            navigate_to('B')
    
    # Submit button for wishes
    if st.button("Next"):
        save_wish(wishes)

# Page 2 - Password Page
elif st.session_state.page == '2':
    st.markdown('<p class="big-header">Type a password to unlock the gift</p>', unsafe_allow_html=True)
    st.markdown('<p>Hint: what is a Ty\'s name</p>', unsafe_allow_html=True)
    
    # Password input
    password = st.text_input("Enter password:", type="password")
    
    # Check password button
    if st.button("Next"):
        if check_password(password):
            navigate_to('birthday')
        else:
            st.error("Incorrect password. Try again!")
    
    # Back button
    if st.button("Return"):
        navigate_to('B')

# Birthday Page
elif st.session_state.page == 'birthday':
    st.markdown('<div class="birthday-page">', unsafe_allow_html=True)
    st.markdown('<h1>🎉 Happy Birthday! 🎂</h1>', unsafe_allow_html=True)
    
    # Display animation (simple loading bar to simulate "surprise")
    with st.spinner("Preparing your surprise..."):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.01)
    
    st.balloons()
    
    # Display wishes if any
    if st.session_state.wishes:
        st.markdown(f"<h3>Your wish:</h3>", unsafe_allow_html=True)
        st.markdown(f"<p><i>\"{st.session_state.wishes}\"</i></p>", unsafe_allow_html=True)
    
    st.markdown("<h3>Wishing you a wonderful day filled with happiness and joy!</h3>", unsafe_allow_html=True)
    st.markdown("<p>May all your dreams come true and may this year bring you success in all your endeavors.</p>", unsafe_allow_html=True)
    
    # Display the birthday image
    try:
        # Look for images in the current directory
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        image_files = []
        
        for file in os.listdir('.'):
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(file)
        
        if image_files:
            st.markdown("<h3>Your special birthday picture:</h3>", unsafe_allow_html=True)
            for img_file in image_files:
                img = Image.open(img_file)
                st.image(img, caption=f"Birthday Image: {img_file}", use_column_width=True)
        else:
            st.info("No birthday images found in the current directory. Add an image file (JPG, PNG, or GIF) to the same folder as this script.")
    except Exception as e:
        st.error(f"Error loading image: {e}")
    
    # Birthday cake ASCII art
    st.markdown("""
    ```
         🎂 🎂 🎂
        🎂 🎂 🎂 🎂
     🎂 🎂 🎂 🎂 🎂 🎂
    🎂 🎂 🎂 🎂 🎂 🎂 🎂
    -------------------------
    |   ♪ ♫ ♪♪ ♫ ♫ ♪♪ ♫   |
    |      HAPPY BIRTHDAY   |
    |        TO TY!        |
    -------------------------
    ```
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Return to start button
    if st.button("Return"):
        navigate_to('A')