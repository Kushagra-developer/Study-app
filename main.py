import streamlit as st
from gtts import gTTS
import os
from utils.gemini_helper import generate_response
from components.sidebar import sidebar_ui
from components.chat_ui import chat_ui

st.set_page_config(page_title="StudyBuddy", page_icon="🧠", layout="wide")

# --- STYLE ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Poppins:wght@400;600&display=swap');

body {
    background: radial-gradient(circle at 20% 20%, #0a0a2a, #000);
    color: #fff;
    font-family: 'Poppins', sans-serif;
}

.main-title {
    text-align: center;
    font-family: 'Orbitron', sans-serif;
    font-size: 3rem;
    background: linear-gradient(90deg, #00ffff, #ff00ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glowPulse 4s ease-in-out infinite alternate;
}

@keyframes glowPulse {
    0% { text-shadow: 0 0 5px #00ffff; }
    100% { text-shadow: 0 0 25px #ff00ff; }
}

/* Single Mic Orb */
.mic-orb {
    margin: 30px auto;
    width: 130px;
    height: 130px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #00ffff, #0044ff);
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.8);
    transition: all 0.4s ease;
    animation: orbGlow 2s infinite alternate;
}
.listening {
    animation: orbListening 0.8s infinite alternate !important;
    box-shadow: 0 0 50px rgba(255, 0, 255, 0.8);
}
@keyframes orbGlow {
    from { transform: scale(1); box-shadow: 0 0 20px #00ffff; }
    to { transform: scale(1.1); box-shadow: 0 0 50px #ff00ff; }
}
@keyframes orbListening {
    from { transform: scale(1.05); box-shadow: 0 0 40px #ff00ff; }
    to { transform: scale(1.2); box-shadow: 0 0 70px #00ffff; }
}

/* Buttons */
div.stButton > button {
    font-family: 'Poppins';
    border: none;
    color: white;
    background: linear-gradient(90deg, #ff00ff, #00ffff);
    padding: 1em 2.5em;
    border-radius: 50px;
    box-shadow: 0 0 20px rgba(0,255,255,0.4);
    transition: 0.3s ease;
}
div.stButton > button:hover {
    transform: scale(1.07);
    box-shadow: 0 0 35px rgba(255,0,255,0.8);
}

/* Chat bubble animation */
@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(10px);}
    100% {opacity: 1; transform: translateY(0);}
}
.user-bubble, .ai-bubble {
    margin-top: 1em;
    padding: 1em 1.5em;
    border-radius: 20px;
    max-width: 70%;
    animation: fadeIn 0.8s ease;
}
.user-bubble {
    background: rgba(0,255,255,0.1);
    border-left: 3px solid #00ffff;
    align-self: flex-end;
    margin-left: auto;
}
.ai-bubble {
    background: rgba(255,0,255,0.1);
    border-left: 3px solid #ff00ff;
}

.response-card {
    background: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 1.5rem;
    margin-top: 1.5rem;
    box-shadow: 0 0 20px rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
}
</style>
""", unsafe_allow_html=True)

# --- JAVASCRIPT: Web Speech API for browser mic ---
st.markdown("""
<script>
function recordVoice() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.start();

    const orb = window.parent.document.querySelector('.mic-orb');
    if (orb) orb.classList.add('listening');

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        const inputBox = window.parent.document.querySelector("textarea[data-testid='stTextArea']");
        inputBox.value = transcript;
        inputBox.dispatchEvent(new Event("input", { bubbles: true }));

        if (orb) orb.classList.remove('listening');
    };

    recognition.onerror = function() {
        alert("Voice input failed. Please try again.");
        if (orb) orb.classList.remove('listening');
    };
}
</script>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
selected_mode = sidebar_ui()

# --- HEADER ---
st.markdown('<h1 class="main-title">🧠 StudyBuddy</h1>', unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Your futuristic AI study companion</h4>", unsafe_allow_html=True)

# --- Voice Orb + Input Area ---
orb_html = '<div class="mic-orb" id="micOrb"></div>'
st.markdown(orb_html, unsafe_allow_html=True)

# Text box where recognized text will appear
text = st.text_area("🎙️ Speak or type your question below:", "")

# Voice button triggers JS
if st.button("🎧 Speak Now"):
    st.markdown("<script>recordVoice();</script>", unsafe_allow_html=True)

# --- Process Input with Gemini ---
if text:
    st.markdown(f"<div class='user-bubble'>🗣️ {text}</div>", unsafe_allow_html=True)
    st.markdown("<div class='ai-bubble'><em>🤖 Thinking...</em></div>", unsafe_allow_html=True)

    response = generate_response(text)
    st.markdown(f"<div class='ai-bubble'>{response}</div>", unsafe_allow_html=True)

    # Voice output
    tts = gTTS(text=response, lang='en')
    tts.save("response.mp3")
    audio_file = open("response.mp3", "rb")
    st.audio(audio_file.read(), format='audio/mp3')

# --- Divider + Chat UI ---
st.markdown("<hr style='border: 1px solid rgba(255,255,255,0.1);'/>", unsafe_allow_html=True)
chat_ui(selected_mode)
