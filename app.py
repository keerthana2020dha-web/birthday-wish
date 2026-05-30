import streamlit as st
import datetime
import time
from gtts import gTTS
import io

# 1. Page Configuration
st.set_page_config(page_title="A Special Surprise! ✨", page_icon="💖", layout="centered")

# Custom CSS for styling the cute app and Polaroid frames
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffe5ec, #ffc2d1, #f0e6ff);
    }
    div.stButton > button:first-child {
        background-color: #ff477e;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 12px 30px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0 4px 10px rgba(255, 71, 126, 0.3);
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff7096;
        color: white;
        transform: scale(1.05);
    }
    .custom-card {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 35px;
        border-radius: 20px;
        border: 2px solid #fff;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    /* Polaroid Frame Style */
    .polaroid {
        background-color: white;
        padding: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        border-radius: 4px;
        text-align: center;
        margin: 15px auto;
        max-width: 250px;
        border: 1px solid #f0f0f0;
    }
    .polaroid img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 2px;
    }
    .polaroid-caption {
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        color: #555;
        margin-top: 12px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize page state tracker if it doesn't exist yet
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# ==========================================
# PAGE 1: THE WELCOME / ENTER PAGE
# ==========================================
if st.session_state.page == 'welcome':
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.write("### Hello there! 👋")
    st.write("Someone has left a little digital time capsule box here just for you.")
    st.write("")
    
    # Text input for their name
    name_input = st.text_input("First, please enter your name here:", placeholder="Type your name...")
    
    st.write("")
    if st.button("Click to Enter the Surprise 🎁"):
        if name_input.strip() == "":
            st.error("Please type your name first so the magic works! ✨")
        else:
            st.session_state.user_name = name_input.strip()
            st.session_state.page = 'main_wish'
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# PAGE 2: THE MAIN WISHER PAGE
# ==========================================
elif st.session_state.page == 'main_wish':
    name = st.session_state.user_name
    
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.title(f"Wait a minute, {name}! 🤭")
    st.write(f"I know I'm incredibly early, but I just couldn't wait to wish you an amazing birthday! {name}, you deserve to be celebrated every single day.")
    
    # --- SET THE BIRTHDAY DATE HERE ---
    birthday = datetime.datetime(2026, 6, 25, 0, 0) 

    # Live Countdown Logic
    countdown_placeholder = st.empty()
    now = datetime.datetime.now()
    time_remaining = birthday - now

    if time_remaining.total_seconds() > 0:
        days = time_remaining.days
        hours, remainder = divmod(time_remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        col1, col2, col3, col4 = countdown_placeholder.columns(4)
        col1.metric("Days", f"{days:02d}")
        col2.metric("Hours", f"{hours:02d}")
        col3.metric("Mins", f"{minutes:02d}")
        col4.metric("Secs", f"{seconds:02d}")
    else:
        countdown_placeholder.subheader(f"🎉 Happy Birthday {name}!!! The day is finally here! 💖")

    st.markdown("</div>", unsafe_allow_html=True)

    # 🔊 FIXED INBUILT VOICE WISHING BUTTON
    if st.button("🔊 Click to hear my voice wish!"):
        voice_text = f"Advance Happy Birthday, {name}!"
        
        # Convert text to speech audio using Python's memory buffer
        sound_buffer = io.BytesIO()
        tts = gTTS(text=voice_text, lang='en', tld='com')
        tts.write_to_fp(sound_buffer)
        
        # Streamlit's built-in player handles autoplay safely on user click
        st.audio(sound_buffer.getvalue(), format="audio/mp3", autoplay=True)
        st.info(f"🔊 Speaking: '{voice_text}'")

    st.write("") # Spacer

    # ==========================================
    # PHOTO MEMORY GRID SECTION
    # ==========================================
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.markdown(f"### 📸 Our Memory Lane")
    st.write("Here are a few reasons why looking back at this year makes me so happy...")
    
    # --- CHANGE IMAGES HERE ---
    photo_1 = "https://i.postimg.cc/m2m9WVfg/IMG-20251020-081824324-2.jpg"
    photo_2 = "https://i.postimg.cc/85dFKmmD/IMG-20251020-080409496-HDR-2.jpg"
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown(f"""
            <div class="polaroid">
                <img src="{photo_1}">
                <div class="polaroid-caption">✨ That crazy fun day!</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_right:
        st.markdown(f"""
            <div class="polaroid">
                <img src="{photo_2}">
                <div class="polaroid-caption">🍰 Unforgettable times</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)

    # Interactive Hug Element
    if st.button("Click for a little hug! 🌸"):
        st.balloons()
        st.success(f"Since your official day is still a bit away, here is an early dose of love, smiles, and good vibes just for you, {name}! The countdown is officially on! ✨💖")
        
    # Option to reset back to page 1
    if st.button("⬅️ Go Back"):
        st.session_state.page = 'welcome'
        st.rerun()
