# backend

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

def extract_video_id(url: str) -> str:
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    return ""

def process_video(video_id: str):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        transcript = " ".join(chunk["text"] for chunk in transcript_list)
        doc = Document(page_content=transcript)

        # Splitting transcript
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents([doc])

        # Generating and storing embeddings into a vector store
        embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                            model_kwargs={'device': 'cpu'})
        db = FAISS.from_documents(chunks, embed_model)

        # Loading a LLM
        llm = OllamaLLM(model = "llama3.1:8b")

        # Creating a QA Chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=False
        )

        return qa_chain, None

    except (TranscriptsDisabled, NoTranscriptFound):
        return None, "Transcript is not available for this video."
    except Exception as e:
        return None, str(e)
