import streamlit as st
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
import os

# 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🧠 AI Function
def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# UI
st.set_page_config(page_title="Voice AI", layout="centered")
st.title("🎙️ My First Voice AI")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

if st.button("🎤 Speak"):
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")

            reply = ask_ai(text)
            st.info(f"AI: {reply}")

            engine.say(reply)
            engine.runAndWait()

        except sr.UnknownValueError:
            st.error("Sorry, I could not understand.")