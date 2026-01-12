import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

# 1. System Prompt Input
system_prompt = st.text_area("Define your AI Agent:", height=70, placeholder="Type your system prompt here...")

# 2. Model Selection Logic
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
Model_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ["Groq", "OpenAI"])

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
else:
    selected_model = st.selectbox("Select OpenAI Model:", Model_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

# 3. User Query Input
user_query = st.text_area("Enter your query:", height=150, placeholder="Ask Anything")

# Backend URL
API_URL = "http://127.0.0.1:9999/chat"

# 4. Button Logic (Sara processing iske andar hoga)
if st.button("Ask Agent:"):
    if user_query.strip():
        # Payload taiyar karna
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }
        
        try:
            # API ko request bhejna
            response = requests.post(API_URL, json=payload)
            
            # Response check karna (Indentation yahan dhyan se dekhiye)
            if response.status_code == 200:
                response_data = response.json()
                
                if isinstance(response_data, dict) and "error" in response_data:
                    st.error(response_data["error"])
                else:
                    st.subheader("Agent Response")
                    # Backend se 'response' key nikalna
                    final_result = response_data.get("response", "No response key found")
                    st.markdown(f"**Final Response:** {final_result}")
            else:
                st.error(f"Backend Error: Status code {response.status_code}")
                
        except Exception as e:
            st.error(f"Could not connect to backend: {e}")
    else:
        st.warning("Please enter a query first!")