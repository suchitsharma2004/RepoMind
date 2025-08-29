from src.config import get_gemini_model
from src.rag import build_vector_db

def summarize_issues(issues):
    model = get_gemini_model()
    db = build_vector_db(issues)

    docs = db.similarity_search("summarize open bug issues", k=5)

    content = "\n\n".join([doc.page_content for doc in docs])
    prompt = f"Summarize these GitHub issues:\n\n{content}"

    response = model.generate_content(prompt)
    return response.text
