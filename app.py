import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🤖 Voice AI (Cloud Version)")

user_input = st.text_input("Ask something:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content
    st.write("AI:", reply)
