import streamlit as st
import random

# List of growth mindset challenges
challenges = [
    "Embrace failure as a learning opportunity.",
    "Try something new outside your comfort zone.",
    "Give constructive feedback to yourself or others.",
    "Practice positive self-talk for the day.",
    "Identify one strength and use it to solve a problem.",
]

# App layout
st.title("🌱 Growth Mindset Challenge")
st.write("Welcome to the Growth Mindset Challenge! This app is designed to help you adopt a growth mindset and track your progress.")

# Set learning goal
st.subheader("Set Your Learning Goals ✨")
learning_goal = st.text_input("What is your learning goal for today?")

# Reflect on learning
st.subheader("Reflect on Your Learning 📝")
reflection = st.text_area("What did you learn today?")

# Seek feedback
st.subheader("Seek Feedback 💬")
feedback = st.text_area("What feedback have you received recently?")

# Show daily challenge
st.subheader("Your Challenge for Today:")
st.info(random.choice(challenges))

st.write("\n💡 *Keep pushing forward! A growth mindset leads to success.*")
