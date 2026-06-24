# 🤖 Agentic AI Chatbot

An intelligent, stateful AI Chatbot built with **FastAPI** and **LangGraph**. It can reason through tasks, search the web in real-time, and seamlessly supports runtime switching between multiple AI models.

🌐 **Live Backend API Gateway:** https://agentic-chatbot-fastapi-a9u4.onrender.com/

---

## ✨ Key Features

* **🧠 Smart Reasoning:** Uses **LangGraph** to create a stateful, cyclic AI agent that "thinks" and plans workflows before responding.
* **🌐 Real-Time Web Search:** Deeply integrated with **Tavily API** to fetch latest live information from the internet, bypassing static LLM data limits.
* **🔌 Multi-Model Support:** Easily switch execution engines between low-latency open-source models (**Groq / Llama 3.3**) and advanced commercial reasoning platforms (**OpenAI / GPT-4o**).
* **🎨 Modern Analytics UI:** A clean, interactive conversational dashboard built over **Streamlit** for real-time tracking.
* **⚡ High-Performance Backend:** Powered by **FastAPI** utilizing native async routing for fast, concurrent client responses.

---

## 🛠️ Tech Stack & Architecture

| Layer | Technology | Role |
| :--- | :--- | :--- |
| **Backend Framework** | FastAPI | Async REST API orchestration & endpoint management |
| **Agentic Core** | LangGraph & LangChain | Conversational state management & tool-calling graph |
| **Search Engine** | Tavily Python SDK | Real-time web search grounding |
| **Frontend UI** | Streamlit | Clean user interactive portal & streaming tokens render |
| **Data Validation** | Pydantic v2 | Strict type safety and environment configurations |

---

## 🐳 Cloud Deployment & Containerization

* **Cloud Architecture:** Deployed using multi-stage build logs over optimized `python:3.11-slim` image configurations on **Render**.
* **Auto-Sync Pipeline:** Integrated with GitHub workflows for automatic continuous delivery (`CD`) upon main branch updates.
