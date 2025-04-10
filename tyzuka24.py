import streamlit as st
import time
import os
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Tyzuka 24+",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Define CSS styles with emerald green color theme
# Using #00674f as our emerald green color
css = """
<style>
    /* General Layout */
    .main {
        padding: 2rem;
        border-radius: 10px;
        background-color: white;
    }
    body {
        background-color: white;
        color: black;
    }
    
    /* Button Styles */
    .stButton button {
        width: 120px;
        border-radius: 5px;
        font-size: 18px;
        padding: 10px;
        border: 2px solid #00674f;
        background-color: white;
        color: black;
    }
    .stButton button:hover {
        background-color: #00674f;
        color: white;
    }
    
    /* Text and Header Styles */
    .big-header {
        font-size: 28px;
        font-weight: bold;
        color: black;
    }
    .center-text {
        text-align: center;
        color: black;
    }
    
    /* Container Styles */
    .gift-container {
        border: 2px solid #00674f;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        background-color: white;
    }
    .number-box {
        width: 60px;
        height: 60px;
        border: 2px solid #00674f;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
        background-color: white;
        color: black;
    }
    .input-box {
        border: 2px solid #00674f;
        border-radius: 5px;
        padding: 10px;
        background-color: white;
    }
    .birthday-page {
        background-color: #e8f8f0;
        padding: 30px;
        border-radius: 10px;
        border: 3px solid #00674f;
        text-align: center;
        color: black;
    }
    .user-wish {
        font-style: italic;
        font-size: 18px;
        border-left: 4px solid #00674f;
        padding-left: 15px;
        margin: 20px 0;
        background-color: #f0fff8;
        padding: 15px;
        border-radius: 8px;
        color: black;
    }
    
    /* Text Area Specific Styling */
    .stTextArea textarea {
        background-color: white !important;
        color: black !important;
        border: 1px solid #00674f !important;
    }
    .stTextArea > div {
        background-color: white !important;
    }
    .stTextArea label {
        color: black !important;
    }
    .stTextArea textarea:focus {
        border-color: #00674f !important;
        box-shadow: 0 0 0 1px #00674f !important;
    }
    
    /* Input Fields Styling */
    .stTextInput input {
        background-color: white !important;
        color: black !important;
        border: 1px solid #00674f !important;
    }
    .stTextInput > div {
        background-color: white !important;
    }
    .stTextInput label {
        color: black !important;
    }
    .stTextInput input:focus {
        border-color: #00674f !important;
        box-shadow: 0 0 0 1px #00674f !important;
    }
    
    /* Progress Bar Styling */
    .stProgress > div > div {
        background-color: #00674f !important;
    }
    
    /* Error Message Styling */
    .stAlert {
        border-color: #00674f !important;
    }
    
    /* Override Streamlit's default theme */
    .st-emotion-cache-10trblm {
        color: black;
    }
    .st-emotion-cache-1gulkj5 {
        background-color: white;
    }
    .st-emotion-cache-16txtl3 {
        color: black;
    }
    .st-emotion-cache-16idsys {
        color: black;
    }
    
    /* Global Text Color Overrides */
    h1, h2, h3, h4, h5, h6, p, span, div, label {
        color: black !important;
    }
    .stSelectbox label, .stMultiselect label {
        color: black !important;
    }
    pre {
        color: black !important;
    }
    
    /* Force all elements to have black text */
    * {
        color: black !important;
    }
    .streamlit-expanderHeader, .main, .element-container, .stMarkdown, p {
        color: black !important;
    }
</style>
"""

# Apply the CSS styling
st.markdown(css, unsafe_allow_html=True)

# Function to set theme with JavaScript
def set_theme():
    js = """
    <script>
        var elements = window.parent.document.querySelectorAll('[data-testid="stAppViewBlockContainer"]');
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.backgroundColor = 'white';
        }
        var elements = window.parent.document.querySelectorAll('[data-testid="stVerticalBlock"]');
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.backgroundColor = 'white';
        }
        
        // Set all text to black
        document.addEventListener('DOMContentLoaded', function() {
            var allElements = document.querySelectorAll('*');
            for (var i = 0; i < allElements.length; i++) {
                allElements[i].style.color = 'black';
            }
        }, false);
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)

# Set light theme
set_theme()

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
    correct_password = "omm"
    if password.lower() == correct_password.lower():
        return True
    return False

# Function to save wish
def save_wish(wish):
    st.session_state.wishes = wish
    navigate_to('birthday')

# Define markdown content for each page
page_content = {
    'A': {
        'title': '<p class="big-header center-text">Anh Ty, iu, oi...</p>'
    },
    'B': {
        'title': '<p class="big-header center-text">Happy Tyzuka 24+</p>',
        'subtitle': '<p class="center-text">A Ty san sang khui sit rit. chuaaa:</p>'
    },
    '1': {
        'title': '<p class="big-header">A Ty uoc 1 dieu iii,</p>',
        'subtitle': '<p>(hong an giannn, hong uoc xam nheeee)</p>'
    },
    '2': {
        'title': '<p class="big-header">Dien dzo dau ...: </p>',
        'subtitle': '<p>Hint: e hay doi` a Ty ... e </p>'
    },
    'birthday': {
        'title': '<h1>🎉 Happy Birthday! 🎂</h1>',
        'wish_header': '<h5>uoc j a Ty noi cho e biet a Ty uoc j, neu hong thi e van tin:</h5>',
        'wish_header_2': '<h5>se thanh su that thuiiiii </h5>',
        'wish_header_3': '<p>(tru khi a Ty go~ xam thiec) </p>',
        'image_header': '<h5>[o day la 1 pic xam dang bi pending huhu ...]</h5>',
        'message': [
            '<h5>Mong a pe Ty binh an nheee (tu nhien thay cringe nua rui hic) </h5>',
            '<h5>Pe iu anh Ty 💝</h5>'
        ],
        
    }
}

# Page A - Welcome Page
if st.session_state.page == 'A':
    st.markdown(page_content['A']['title'], unsafe_allow_html=True)
    
    # Next button
    col_left, col_right = st.columns([1, 1])
    with col_right:
        if st.button("Next", key="next_from_a"):
            navigate_to('B')

# Page B - Choice Page
elif st.session_state.page == 'B':
    st.markdown(page_content['B']['title'], unsafe_allow_html=True)
    st.markdown(page_content['B']['subtitle'], unsafe_allow_html=True)
    
    # Option buttons layout
    # col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    # with col2:
    #     if st.button("Secret 1"):
    #         navigate_to('1')
    
    # with col3:
    #     if st.button("Secret 2"):
    #         navigate_to('2')
    
    # Navigation buttons at the bottom
    col_left, col_right = st.columns([1, 1])
    with col_left:
        if st.button("Back", key="back_from_b"):
            navigate_to('A')

    with col_left:
        if st.button("Roi, nextt", key="next_from_b"):
            navigate_to('1')

# Page 1 - Write Wishes
elif st.session_state.page == '1':
    st.markdown(page_content['1']['title'], unsafe_allow_html=True)
    st.markdown(page_content['1']['subtitle'], unsafe_allow_html=True)
    
    # Text area for wishes
    wishes = st.text_area("Go~ dieu uoc dzo day:", height=100, key="wish_input")
    
    # Navigation buttons at the bottom
    col_left, col_right = st.columns([1, 1])
    with col_left:
        if st.button("Back", key="back_from_1"):
            navigate_to('B')
    with col_right:
        if st.button("Next", key="next_from_1"):
            if wishes.strip():  # Check if wishes is not empty after removing whitespace
                save_wish(wishes)
                navigate_to('2')
            else:
                st.error("Ai cho skip z haaaa")

# Page 2 - Password Page
elif st.session_state.page == '2':
    st.markdown(page_content['2']['title'], unsafe_allow_html=True)
    st.markdown(page_content['2']['subtitle'], unsafe_allow_html=True)
    
    # Password input
    password = st.text_input("Enter password:", type="password")
    
    # Navigation buttons at the bottom
    col_left, col_right = st.columns([1, 1])
    with col_left:
        if st.button("Back", key="back_from_2"):
            navigate_to('B')
    with col_right:
        if st.button("Next", key="next_from_2"):
            if check_password(password):
                navigate_to('birthday')
            else:
                st.error("Another hint: co 3 ky tu, '10s nuaaa'")

# Birthday Page
elif st.session_state.page == 'birthday':
    # st.markdown('<div class="birthday-page">', unsafe_allow_html=True)
    # st.markdown(page_content['birthday']['title'], unsafe_allow_html=True)
    
    # Display animation (simple loading bar to simulate "surprise")
    with st.spinner("Preparing your surprise..."):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.01)
        progress_bar.empty()
    
    st.balloons()
    
    # Display wishes if any
    if st.session_state.wishes:
        st.markdown(page_content['birthday']['wish_header'], unsafe_allow_html=True)
        st.markdown(f'<div class="user-wish">{st.session_state.wishes}</div>', unsafe_allow_html=True)
        st.markdown(page_content['birthday']['wish_header_2'], unsafe_allow_html=True)
        st.markdown(page_content['birthday']['wish_header_3'], unsafe_allow_html=True)
    
    # Display the birthday image
    try:
        # First try to load the specific tyzuka24.jpg image
        if os.path.exists('tyzuka24.jpg'):
            img = Image.open('tyzuka24.jpg')
            st.markdown(page_content['birthday']['image_header'], unsafe_allow_html=True)
            # st.image(img, caption="Happy Birthday!", use_column_width=True)
        else:
            # If specific image not found, look for other images
            image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            image_files = []
            
            for file in os.listdir('.'):
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    image_files.append(file)
            
            if image_files:
                # st.markdown(page_content['birthday']['image_header'], unsafe_allow_html=True)
                for img_file in image_files:
                    img = Image.open(img_file)
                    st.image(img, caption=f"Birthday Image: {img_file}", use_column_width=True)
            else:
                st.info("[o day la 1 pic xam dang bi pending huhu ...]")
    except Exception as e:
        st.error(f"Error loading image: {e}")

    # Display birthday message
    for message in page_content['birthday']['message']:
        st.markdown(message, unsafe_allow_html=True)
        
    # st.markdown('</div>', unsafe_allow_html=True)
    
    # Back to start button
    if st.button("Back"):
        navigate_to('A')