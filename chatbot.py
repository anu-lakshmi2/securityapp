import streamlit as st
import google.generativeai as genai

# Set up Gemini API
GEMINI_API_KEY = "AIzaSyANgFbC6Cb-JmSosn7npqfKRG7gVHsD5qk"
genai.configure(api_key=GEMINI_API_KEY)

# Function to get response from Gemini
def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(user_input)
        return response.text if response else "Sorry, I couldn't understand that."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("🛡️ Self-Security Chatbot")
st.write("Ask me anything related to your safety and security!")

# User input
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = get_gemini_response(user_input)
        st.text_area("Chatbot:", response, height=150)
    else:
        st.warning("Please enter a message.")


