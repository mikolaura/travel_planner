# 🌍 Multi-Agent Travel Planner

A LangGraph-based **multi-agent AI system** that helps users plan trips end-to-end.  
The system uses specialized agents for destinations, flights, hotels, activities, budgeting, and more — working together to generate a complete, personalized travel plan.  

## ✨ Features
- 📌 Personalized destination recommendations  
- 💰 Budget-aware trip optimization  
- 🌦️ Weather-aware activity adjustments  

Built with **LangGraph** to support parallel agent execution, retries, and modular workflows.

---

## 🚀 Getting Started

### 📋 Requirements
- [Python](https://www.python.org/) (>=3.10 recommended)  
- [uv](https://github.com/astral-sh/uv) (fast Python package manager)  

---

### 🔹 Option 1: Run via Web UI
This will start a **Streamlit web app** for interactive usage.

```bash
# Install dependencies
uv sync

# Start the web app
streamlit run web.py
```

Then open the link shown in your terminal (usually `http://localhost:8501/`).

---

### 🔹 Option 2: Run via LangGraph Studio
This lets you explore and run the workflow in **LangGraph Studio**.

```bash
# Install dependencies
uv sync

# Launch LangGraph Studio
uvx --from "langgraph-cli[inmem]" --with-editable . langgraph dev
```

This opens the LangGraph Studio UI, where you can inspect and run the DAG of agents.

---




## ⚖️ License
MIT License © 2025
