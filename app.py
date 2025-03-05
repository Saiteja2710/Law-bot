import streamlit as st
import google.generativeai as genai
import os

# Set up the Gemini API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAqSWEvOGW46zSpaEptB9cfQalLKVSqFds"  # Replace with your actual API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to call Gemini API for legal advice
def get_legal_advice(prompt):
    try:
        system_prompt = (
            "You are an AI assistant specializing in Indian laws. When given a case scenario, "
            "identify the applicable laws, sections, and possible legal remedies."
        )

        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(system_prompt + "\n\n" + prompt)
        
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to clear user input
def clear_input():
    st.session_state["user_input"] = ""

def main():
    st.title('Smart Idea: An Interface for Legal Advise')

    # Initialize session state for user input
    if "user_input" not in st.session_state:
        st.session_state["user_input"] = ""

    # User input field
    user_input = st.text_area("Enter case details:", key="user_input")

    col1, col2 = st.columns([2, 1])  # Layout for buttons

    with col1:
        if st.button("Get Legal Advice"):
            if user_input:
                bot_output = get_legal_advice(user_input)

                # Display the result
                st.subheader("Legal Advice 📜")
                st.markdown(f'**⚖️ Bot:** {bot_output}')

    with col2:
        st.button("Clear Input", on_click=clear_input)  # Clears input separately

if __name__ == "__main__":
    main()
