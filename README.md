# 🎙️ YT-Video-QnA-System

An AI-powered **RAG-based YouTube Video Q&A Chatbot** that allows users to ask questions about a YouTube video and receive context-aware answers based on its transcript.

The application extracts the YouTube transcript, splits it into meaningful chunks, converts the chunks into embeddings, stores them in a FAISS vector database, and uses a local **Llama 3.2 model through Ollama** to generate answers.

## 🚀 Features

- 🎥 YouTube video transcript extraction
- ✂️ Transcript chunking using Recursive Character Text Splitter
- 🧠 Hugging Face sentence embeddings
- 🔎 Semantic similarity search using FAISS
- 🤖 Local LLM inference using Ollama
- 💬 Question-answering over video content
- 🖥️ Interactive Streamlit chat interface
- 🗑️ Chat history management

---

## 🏗️ Architecture

```text
             YouTube Video URL
                    │
                    ▼
          Extract Video ID
                    │
                    ▼
        YouTube Transcript API
                    │
                    ▼
           Video Transcript
                    │
                    ▼
     Recursive Character Splitter
                    │
                    ▼
             Text Chunks
                    │
                    ▼
        Hugging Face Embeddings
                    │
                    ▼
             FAISS Vector DB
                    │
                    ▼
              Retriever
                    │
                    ▼
          RetrievalQA Chain
                    │
                    ▼
           Ollama Llama 3.2
                    │
                    ▼
             Final Answer
                    │
                    ▼
             Streamlit UI
```

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **FAISS**
- **Hugging Face Embeddings**
- **Ollama**
- **Llama 3.2**
- **YouTube Transcript API**
- **Streamlit**

---

## 📁 Project Structure

```text
YouTube-QnA/
│
├── app.py
├── QnA.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama and pull the required model:

```bash
ollama pull llama3.2:3b
```

Verify:

```bash
ollama list
```

---

## ▶️ Run the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 How It Works

1. Enter a valid YouTube video URL.
2. Click **Process Video**.
3. The application extracts the video's transcript.
4. The transcript is split into smaller chunks.
5. Hugging Face embeddings are generated for each chunk.
6. Embeddings are stored in a FAISS vector database.
7. User questions are matched against relevant transcript chunks.
8. Retrieved context is passed to the Llama 3.2 model through Ollama.
9. The model generates an answer based on the video content.

---

## 📌 Example

**Question:**

```text
What is this video about?
```

**Answer:**

The chatbot retrieves relevant portions of the transcript and generates a concise answer describing the main topics discussed in the video.

---

## 🔑 Key Concepts

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Text Embeddings
- Document Chunking
- Context-Aware Question Answering
- Local LLM Inference
- Streamlit Application Development

---

## 🔮 Future Improvements

- Support videos with multiple transcript languages
- Add source citations for retrieved transcript chunks
- Add conversation-aware follow-up questions
- Improve transcript preprocessing
- Add timestamp-based answers
- Support YouTube playlists
- Add transcript download functionality

---

## ⚠️ Disclaimer

This project is developed for educational and demonstration purposes. The quality of generated answers depends on the availability and quality of the YouTube transcript.

---

## 👨‍💻 Author

**Devank Verma**

National Institute of Technology, Rourkela

⭐ If you found this project useful, consider giving the repository a star!
