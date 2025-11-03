# 📘 **Study Buddy — AI-Powered Study Assistant**

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![Gemini API](https://img.shields.io/badge/Backend-Gemini%202.5%20Flash-blue?logo=google)
![Python](https://img.shields.io/badge/Language-Python-yellow?logo=python)
![IBM SkillsBuild](https://img.shields.io/badge/AICTE%20x%20IBM-SkillsBuild%20Internship-orange?logo=ibm)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-purple) 

---

## 🧠 **Project Overview**

Students often struggle to grasp difficult topics or summarize lengthy notes.  
**Study Buddy** is an AI-powered web app that acts as a **personal academic assistant**, capable of:

- 🧩 Explaining complex concepts in simple terms  
- 📄 Summarizing notes or uploaded PDFs  
- ❓ Generating quizzes or flashcards for quick revision  

It combines **Streamlit** for UI and **Gemini 2.5 Flash API** for fast, intelligent AI responses — all in a clean chat-based interface.

🔗 [Check out the live app here! 🏎️](https://sgpai-study-buddy.streamlit.app/) 

---

## ⚙️ **System Design**

### 🏗️ **Architecture**
A lightweight **Streamlit frontend** interacts with **Google’s Gemini 2.5 Flash** backend through secure API calls.  
All secrets are managed safely via `.env` and `st.secrets`.

### 🧩 **Core Features**
| Mode | Function | Example |
|------|-----------|----------|
| 🧠 **Explainer** | Simplifies academic concepts | “Explain Deadlock in OS” |
| 📄 **Summarizer** | Condenses notes or PDFs | Upload 20-page PDF → short summary |
| ❓ **Quizzer** | Generates MCQs & flashcards | “Create 10 questions on DBMS” |

Additional:
- 📂 PDF upload (text extraction via PyPDF2)
- 💬 Real-time chat interface
- 🔄 New chat reset option
- ☁️ Deployed on Streamlit Cloud

---

## 🧱 **Project Structure**

```
StudyBuddy/
├── main.py
├── requirements.txt
├── assets/
│ └── PROBLEM STATEMENTS.pdf
├── components/
│ ├── chat_ui.py
│ ├── pdf_handler.py
│ └── sidebar.py
├── core/
│ ├── ai_utils.py
│ ├── explainer.py
│ ├── pdf_handler.py
│ ├── quizzer.py
│ └── summarizer.py
└── utils/
└── gemini_helper.py
```

---

## 🪜 Workflow
<img width="5496" height="4080" alt="StudyBuddy Workflow" src="https://github.com/user-attachments/assets/ae8f9a61-c84b-4ebf-9081-f139b98cf441" />
©️🖼️ Diagram Credits: https://gitdiagram.com/

---

## 💡 **Tech Stack**

| Category | Technologies |
|-----------|---------------|
| **Frontend** | Streamlit |
| **Backend / AI Engine** | Google Gemini 2.5 Flash API |
| **Language** | Python |
| **Libraries** | PyPDF2, google-generativeai, streamlit, dotenv |
| **Deployment** | Streamlit Community Cloud |
| **Security** | `.env` + `st.secrets` key handling |

---

## 🧾 **Results**

- 🎯 Simple, modern, and interactive chat-based UI  
- 📑 Summarization and quiz generation from user input or PDFs  
- ⚡ Fast AI responses through Gemini 2.5 Flash  
- 🧩 Smooth multi-mode workflow for learning support  

---

## 🚀 **Future Scope**

- 🗣️ Speech-based interaction  
- 🌐 Multi-language explanations  
- 🧠 Flashcard & spaced-repetition support
- 👤 Implement memory-based personalization for users
- ☁️ Drive/Notion integration for saved sessions  

---

> 🧩 *“Integrating AI with Education — Making Learning Simpler, Smarter, and Accessible for All.”*

---

## 👨‍💻 Author
**Ammaar Ahmad Khan**  
- GitHub: [@GPA95](https://github.com/GPA95)

🌟 If you find this repository useful, please give it a star! 🌟

---
