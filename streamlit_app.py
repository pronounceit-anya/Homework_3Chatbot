import streamlit as st
from openai import OpenAI

from transformers import pipeline

st.title("Chatbot 2.0")

generator = pipeline('text-generation', model='gpt2')

prompt = st.text_input("What is your prompt today?", "Damascus is")

output = generator(prompt, max_length=20, num_return_sequences=10, truncation=True)[0]

st.write(
    output["generated_text"]
