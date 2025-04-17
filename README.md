# (IBM-DOCASSIST) AI Assistant for Internal Docs (RAG + LLM + Docker)

A fully containerized, production-style **AI assistant** that helps users query internal documents (PDFs, DOCX, etc.) using **natural language**. Built with **Retrieval-Augmented Generation (RAG)**, this system uses a vector database for semantic search and an LLM for answering questions contextually.

This project is ideal for enterprise environments (e.g. IBM, internal tools) where access to information across documents is crucial and must be deployed reliably via Docker.

---

## Features

- Upload internal documents (e.g. manuals, HR policies, research papers)
- Chunk + embed text into a vector DB
- Ask natural language questions
- AI responds with factual, human-like answers using LLM
- Fully containerized with Docker + orchestrated services

---

## Architecture

```
📄 Docs Upload     👤 User Question
     |                   |
     v                   v
[ Doc Ingestion API ]   [ Query API ]
       |                     |
       v                     v
[ Text Chunking + Embedding Pipeline ]
       |                     |
       v                     v
🗂️ Vector DB (FAISS/OpenSearch) <-> 🔍 Search Engine
                 |
                 v
         [ LLM Response Builder ]
                 |
                 v
           💬 Final Answer
```

---

## Tech Stack

| Layer        | Tools                                       |
|--------------|---------------------------------------------|
| API Server   | FastAPI (Python)                            |
| Embeddings   | HuggingFace (MiniLM / BGE), IBM embeddings  |
| LLM          | Watsonx.ai             |
| Vector Store | FAISS (local) or OpenSearch (cloud)         |
| Storage      | Local filesystem or IBM Cloud Object Storage|
| Orchestration| Docker + Docker Compose                     |
| CI/CD        | GitHub Actions (with pytest + linter)       |

---

## ✅ To-Do

- [ ] Add frontend or simple UI for uploads + chat
- [ ] Add support for IBM watsonx.ai endpoints
- [ ] Docker healthchecks + logging
- [ ] Deploy to IBM Cloud / Kubernetes
- [ ] Add basic authentication for endpoints
- [ ] Auto-retraining on new document uploads
