### **🎥 YouTube Blog Writer AI (CrewAI + Streamlit)**


An AI-powered end-to-end application that automatically extracts content from YouTube videos and generates high-quality blog articles based on user-provided topics.

This project uses **CrewAI Agents**, **LangChain Tools**, and **Streamlit** to deliver a fully automated content creation pipeline from video transcription to blog post writing.

---

## 🚀 Features

- 🧠 Multi-agent architecture using CrewAI
- 🔎 YouTube video search and transcription extraction
- ✍️ AI-powered blog generation from video content
- 💬 Streamlit-based user interface for easy interaction
- 🔐 Secure API key management using `.env`
- ⚙️ Modular, extensible, and fully customizable codebase

---

## 📂 Project Structure
┣ 📄 app.py # Streamlit frontend

┣ 📄 crew_module.py # CrewAI orchestration logic

┣ 📄 agents.py # CrewAI agents (Researcher & Writer)

┣ 📄 tasks.py # CrewAI tasks assigned to agents

┣ 📄 tools.py # YouTube search tool

┣ 📄 .env # Environment variables for API keys

┣ 📄 requirements.txt # Required Python packages

## Authors

- [@vishalrajput](https://github.com/vishalrajput29)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. OPENAPI |





## Project Demo

https://drive.google.com/file/d/15vQwak3p4TmzlpRSbqml5bzc3E_DTqbQ/view?usp=sharing

