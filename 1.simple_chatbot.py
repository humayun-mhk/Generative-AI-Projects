from dotenv import load_dotenv
import os
import streamlit as st
from langchain_groq import ChatGroq

# Load environment and key
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("gorq_api_key")

# Initialize Groq model
model = ChatGroq(model="llama3-8b-8192", max_tokens=1000, temperature=0.7)

# Page settings
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="centered")

# Load external CSS
def load_css(path="styles.css"):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Chat UI
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.markdown('<div class="chat-title">🤖  Simple ChatBot</div>', unsafe_allow_html=True)

user_query = st.text_input("Your Message", placeholder="Type here and press Enter...")

if user_query:
    with st.spinner("Thinking..."):
        try:
            reply = model.invoke(user_query).content
            st.markdown(f'<div class="chat-box user-box">👤 <b>You:</b><br>{user_query}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="chat-box">🤖 <b>GroqBot:</b><br>{reply}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ {e}")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="footer">Built with ❤️ by Humayun</div>', unsafe_allow_html=True)
