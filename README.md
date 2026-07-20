# 🤖 Multi-Agent Financial Intelligence System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-009688?logo=fastapi)
![Next.js](https://img.shields.io/badge/Next.js-16-black?logo=next.js)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Railway](https://img.shields.io/badge/Railway-Backend-purple)
![Vercel](https://img.shields.io/badge/Vercel-Frontend-black)

</p>

An AI-powered financial research platform that leverages **LangGraph Multi-Agent Orchestration**, **Retrieval-Augmented Generation (RAG)**, and **FastAPI** to help users analyze financial reports through intelligent natural language conversations.

---

# 📚 Table of Contents

- About
- Why This Project?
- Live Demo
- Key Features
- System Architecture
- Multi-Agent Workflow
- Technology Stack
- Project Structure
- Getting Started
- Environment Variables
- API Endpoints
- Deployment
- Key Highlights
- Key Learnings
- Future Scope
- Author

---

# 📖 About

Multi-Agent Financial Intelligence System is a production-ready AI application that enables users to analyze financial reports through natural language conversations.

Unlike traditional AI chatbots, the application coordinates multiple specialized AI agents responsible for planning, execution, and response evaluation. The system combines Retrieval-Augmented Generation (RAG) with semantic document retrieval to produce responses grounded in financial documents instead of relying solely on LLM knowledge.

---

# 💡 Why This Project?

Financial reports are often lengthy and difficult to interpret quickly.

This project aims to simplify financial analysis by allowing users to ask natural language questions while an AI-powered multi-agent system retrieves relevant financial information, reasons over it, and produces contextual responses backed by uploaded documents.

---

# 🌐 Live Demo

### Frontend

https://multi-agent-financial-intelligence.vercel.app

### Backend API

https://multi-agent-financial-intelligence-system-production.up.railway.app

---

# ✨ Key Features

- 🔐 Secure authentication with Clerk
- 🤖 Multi-Agent AI workflow using LangGraph
- 📚 Retrieval-Augmented Generation (RAG)
- 📄 Financial PDF ingestion
- 🔍 Semantic search using ChromaDB
- 💬 Persistent multi-session chat history
- ⚡ Streaming AI responses
- 🗄 PostgreSQL-backed storage
- 🌐 Railway + Vercel deployment
- 📱 Responsive user interface

---

# 🏗 System Architecture

```text
                         Next.js Frontend
                     React • TypeScript • Clerk
                               │
                               │
                     JWT Authentication
                               │
                               ▼
                     FastAPI Backend API
                               │
      ┌────────────────────────┼────────────────────────┐
      │                        │                        │
      ▼                        ▼                        ▼
 PostgreSQL              LangGraph Engine          ChromaDB
(Session Storage)        Multi-Agent System     Vector Database
                               │
          Planner → Executor → Critic
                               │
                               ▼
                    OpenAI + Tavily Search
                               │
                               ▼
                     Financial PDF Documents
```

---

# 🤖 Multi-Agent Workflow

```text
User Query
     │
     ▼
Planner Agent
     │
     ▼
Executor Agent
     │
     ├────────► ChromaDB Retrieval
     │
     ├────────► Tavily Search
     │
     └────────► Financial Analysis
     │
     ▼
Critic Agent
     │
     ▼
Final AI Response
```

---

# 🚀 Technology Stack

| Category | Technology |
|-----------|------------|
| Frontend | Next.js, React, TypeScript |
| Backend | FastAPI |
| AI Framework | LangGraph |
| LLM Framework | LangChain |
| LLM | OpenAI |
| Vector Database | ChromaDB |
| Database | PostgreSQL |
| ORM | SQLAlchemy Async |
| Authentication | Clerk |
| Search | Tavily |
| Deployment | Railway & Vercel |

---

# 📂 Project Structure

```text
backend/
│
├── api/
├── auth/
├── core/
├── db/
├── graph/
├── models/
├── rag/
├── repositories/
├── schemas/
└── services/

frontend/
│
├── app/
├── components/
├── hooks/
├── lib/
└── public/
```

---

# ⚙️ Getting Started

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-financial-intelligence-system.git

cd multi-agent-financial-intelligence-system
```

---

## Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🔑 Environment Variables

## Backend

```env
DATABASE_URL=

OPENAI_API_KEY=

CLERK_SECRET_KEY=

TAVILY_API_KEY=

LANGSMITH_API_KEY=
```

---

## Frontend

```env
NEXT_PUBLIC_API_URL=

NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /api/chat | Generate AI Response |
| GET | /api/sessions | Fetch User Sessions |
| POST | /api/sessions | Create New Session |
| GET | /api/messages | Fetch Messages |
| DELETE | /api/sessions/{id} | Delete Session |

---

# 🚀 Deployment

| Service | Platform |
|----------|----------|
| Frontend | Vercel |
| Backend | Railway |
| Database | PostgreSQL |
| Authentication | Clerk |

---

# 📈 Key Highlights

- ✅ Production-ready full-stack AI application
- ✅ Multi-Agent AI architecture using LangGraph
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Asynchronous FastAPI backend
- ✅ Secure JWT authentication
- ✅ Persistent PostgreSQL chat storage
- ✅ Semantic document retrieval using ChromaDB
- ✅ Cloud deployment with Railway & Vercel

---

# 💡 Key Learnings

This project provided practical experience with:

- Designing multi-agent AI systems using LangGraph.
- Building asynchronous REST APIs using FastAPI.
- Implementing Retrieval-Augmented Generation (RAG).
- Integrating vector databases with ChromaDB.
- Developing secure authentication using Clerk.
- Deploying cloud-native applications on Railway and Vercel.
- Managing production environments and CORS configuration.

---

# 🚀 Future Scope

- 📄 Drag-and-drop PDF upload and automatic indexing.
- 📊 Multi-document financial comparison.
- 🧠 Long-term conversational memory.
- 🔍 Hybrid retrieval (vector + keyword search).
- ⚡ Redis caching.
- 📈 Interactive financial charts.
- 🔔 Background document processing.
- 🐳 Docker Compose support.
- ☸ Kubernetes deployment.
- 🔄 GitHub Actions CI/CD.
- 🧪 Unit & Integration testing.
- 🤖 Support for multiple LLM providers (OpenAI, Anthropic, Gemini).

---

# 👨‍💻 Author

**Ashutosh Kumar Pathak**

📧 ashutoshpathak1765@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/ashutosh-pathak-1397ba230/

💻 GitHub: https://github.com/AshutoshPathak1765

---

## ⭐ If you found this project useful, please consider giving it a star!
