import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

st.title("Chatbot")

# Get user input
user_input = st.text_input("You:", "")

if user_input:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY"))
    response = llm.invoke(user_input)
    st.write("Chatbot:", response.content)
