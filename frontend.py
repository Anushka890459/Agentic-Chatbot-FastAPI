import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered", page_icon="🤖")
st.title("🤖 AI Chatbot Agents (LangGraph)")
st.write("Configure and interact with dynamic reasoning AI Agents in real-time!")

system_prompt = st.text_area(
    "Define your AI Agent's Persona:", 
    height=80, 
    value="You are a helpful and precise AI assistant.",
    placeholder="Type your system prompt here..."
)

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Infrastructure Provider:", ["Groq", "OpenAI"])

if provider == "Groq":
    selected_model = st.selectbox("Select Target Groq Model:", MODEL_NAMES_GROQ)
else:
    selected_model = st.selectbox("Select Target OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search (Incorporate live data via Tavily API)")

st.markdown("---")

API_URL = "http://127.0.0.1:9999/chat"

user_query = st.text_area("Enter your query:", height=100, placeholder="Ask anything to invoke the agent loop...")

if st.button("Ask Agent", type="primary"):
    if user_query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }
        
        with st.spinner("Agent is analyzing prompt, executing tools, and formulating feedback..."):
            try:
                response = requests.post(API_URL, json=payload)
                
                if response.status_code == 200:
                    response_data = response.json()
                    
                    if isinstance(response_data, dict) and "error" in response_data:
                        st.error(response_data["error"])
                    else:
                        st.subheader("🤖 Agent Evaluation Response")
                        final_result = response_data.get("response", "No valid payload response block captured.")
                        st.markdown(final_result)
                else:
                    st.error(f"Backend Server Failure: Returned status code {response.status_code}")
                    
            except Exception as e:
                st.error(f"Network Connection Failed: {e}. Please ensure backend.py is active on port 9999.")
    else:
        st.warning("Please input a logical query instruction before executing!")