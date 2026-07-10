# StudyAI 🚀

An offline AI-powered Study Assistant built using FastAPI, React, Ollama, FAISS, and Local LLMs.

StudyAI helps students chat with AI, analyze PDFs, solve math problems, understand images, and switch between fast and deep reasoning models — all running locally on their own machine.

---

# Features

## 💬 AI Chat

- Normal AI conversations
- Local LLM powered
- Works offline
- Fast and Deep modes

---

## 📄 PDF Assistant

Upload PDFs and ask questions about them.

Features:

- PDF text extraction
- FAISS vector search
- Retrieval Augmented Generation (RAG)
- Large PDF support
- Chapter-wise querying

Example:

> Summarize Chapter 2

> What are the advantages of OOP?

---

## 🖼️ Vision Assistant

Upload images and ask questions.

Examples:

- Explain this diagram
- Describe this image
- Analyze this screenshot
- Understand handwritten notes

Powered by:

- Qwen2.5VL

---

## ➗ Math Solver

Solve mathematical expressions locally.

Examples:

```text
x^2 - 5*x + 6

sin(x)

diff(x^2)

integrate(x^3)
```

Powered by:

- SymPy

---

## ⚡ Fast Mode

Uses:

```text
qwen2.5vl:7b
```

Best for:

- Quick questions
- Coding help
- Notes
- Fast responses

---

## 🧠 Deep Mode

Uses:

```text
qwen3:30b
```

Best for:

- Assignments
- Long explanations
- Deep reasoning
- Exam preparation

---

## 💾 Saved Chats

Chats are automatically saved in browser storage.

Refresh-safe conversation history.

---

# Tech Stack

## Frontend

- React
- Vite
- Axios
- CSS

## Backend

- FastAPI
- Python

## AI

- Ollama
- Qwen2.5VL 7B
- Qwen3 30B

## Search

- FAISS
- Nomic Embeddings

## Math

- SymPy

---

# Project Structure

```text
AI-Study-Assistant
│
├── backend
│   ├── api
│   ├── pdf
│   ├── vision
│   ├── math
│   ├── search
│   ├── router
│   └── main.py
│
├── frontend
│   ├── src
│   └── public
│
├── uploads
├── exports
├── vector_db
│
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/starktitan009/StudyAI.git
```

```bash
cd StudyAI
```

---

# Backend Setup

Create virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn backend.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

```bash
cd frontend
```

Install:

```bash
npm install
```

Run:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# Ollama Setup

Install Ollama:

https://ollama.com

Pull required models:

```bash
ollama pull qwen2.5vl:7b
```

```bash
ollama pull qwen3:30b
```

```bash
ollama pull nomic-embed-text
```

Start Ollama:

```bash
ollama serve
```

---

# Supported Modes

| Mode | Model |
|--------|--------|
| Fast | Qwen2.5VL 7B |
| Deep | Qwen3 30B |
| PDF | FAISS + LLM |
| Vision | Qwen2.5VL |
| Math | SymPy |

---

# Current Status

## Completed

- [x] Chat
- [x] PDF Upload
- [x] PDF RAG
- [x] Image Analysis
- [x] Math Solver
- [x] Fast Mode
- [x] Deep Mode
- [x] Model Switching
- [x] Saved Chats
- [x] Local AI

---

## Planned Features

- [ ] OCR
- [ ] Vision → Deep Pipeline
- [ ] Multiple Chat Sessions
- [ ] Code Highlighting
- [ ] Export Notes to PDF
- [ ] Multi-PDF Support
- [ ] Web Search

---
## 🤝 Contributing

Contributions are welcome and greatly appreciated.

If you'd like to contribute:

1. Fork the repository.
2. Create a new feature or bug-fix branch.
3. Commit your changes with clear commit messages.
4. Test your changes before submitting.
5. Open a Pull Request describing your improvements.

Please ensure that your code follows the project's coding standards and does not introduce breaking changes.
# Author

Lohith

Built as a personal AI-powered Study Assistant project using local LLMs and modern AI tooling.

---

# License

MIT License
