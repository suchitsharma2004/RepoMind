from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

def build_vector_db(issues, persist_dir="data/chroma_db"):
    # Combine issue title + body into single text
    texts = [f"{i['title']} {i['body']}" for i in issues]
    metadatas = [{"url": i["url"]} for i in issues]

    # Use Gemini embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Build Chroma DB
    db = Chroma.from_texts(
        texts,
        embedding=embeddings,
        metadatas=metadatas,
        persist_directory=persist_dir
    )
    return db
