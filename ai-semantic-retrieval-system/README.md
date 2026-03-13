# AI Semantic Retrieval System using Vector Search (RAG)

## Overview
This project implements a Retrieval Augmented Generation (RAG) based semantic search system that enables users to query large technical documents and obtain context-grounded AI responses.

The system uses vector embeddings and similarity search to retrieve semantically relevant content and generate accurate answers, demonstrating core concepts used in modern AI infrastructure and vector databases.

## Problem Statement
Traditional keyword-based search fails to capture semantic meaning in large technical documents, leading to inefficient information retrieval.

This project aims to build an AI-driven semantic retrieval system that understands user intent and provides context-aware answers.

## Solution Approach
The system follows a RAG pipeline:

1. Document ingestion and preprocessing  
2. Semantic chunk generation  
3. Embedding generation using transformer models  
4. Vector storage and similarity search  
5. Context-grounded answer generation using local LLM  

## Key Features
- Semantic search using vector embeddings  
- Context-grounded AI responses  
- Efficient document chunking strategy  
- Local LLM inference  
- Interactive query interface  

## System Architecture
User Query → Embedding → Vector Search → Context Retrieval → LLM Response

## Tech Stack
- Python  
- FastAPI  
- Streamlit  
- Sentence Transformers  
- FAISS (Vector Search Concept)  
- Ollama (Local LLM Inference)  

## Relation to Vector Database Concepts
This project demonstrates core vector database principles such as high-dimensional embedding representation, similarity search, and semantic retrieval, aligning with AI infrastructure systems like Endee.

## How to Run
Install dependencies:


pip install -r requirements.txt


Run backend:

uvicorn app:app --reload


Run UI:

streamlit run ui.py


## Example Queries
- What is categorical cross entropy  
- Explain softmax function  
- Define neural networks  

## Limitations
- Retrieval accuracy depends on chunking strategy  
- Large documents increase embedding computation time  
- Local LLM performance depends on hardware capability  

## Future Improvements
- Integration with distributed vector database (Endee)  
- Hybrid search (semantic + keyword)  
- Multi-document reasoning

## Demo Workflow

- Upload document
- System generates embeddings
- Ask question
- System retrieves context
- AI generates grounded answer

## Author
Devang Varshney  
B.Tech CSE(AIML)
Galgotias University
