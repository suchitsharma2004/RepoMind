# import os
# import json
# from pathlib import Path
# from src.config import get_gemini_model
# from src.rag import build_vector_db

# CACHE_DIR = Path("cache")
# CACHE_DIR.mkdir(exist_ok=True)

# def summarize_issues(issues, repo, label):
#     """
#     Summarizes all issues using Gemini with caching to avoid quota limits.
#     """
#     if not issues:
#         return "No issues to summarize."

#     cache_file = CACHE_DIR / f"{repo.replace('/', '_')}_{label}.json"
#     if cache_file.exists():
#         with open(cache_file, "r") as f:
#             return json.load(f)["summary"]

#     model = get_gemini_model()
#     db = build_vector_db(issues)
#     docs = db.similarity_search("Summarize all open bug issues", k=min(10, len(issues)))
#     content = "\n\n".join([doc.page_content for doc in docs])
#     prompt = f"Please provide a concise overall summary of these GitHub issues:\n\n{content}"

#     response = model.generate_content(prompt)
#     summary_text = getattr(response, "text", str(response))

#     # Save summary to cache
#     with open(cache_file, "w") as f:
#         json.dump({"summary": summary_text}, f)

#     return summary_text

import json
from pathlib import Path

CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

def summarize_issues(issues, repo, label):
    """
    Temporary stub function.
    Skips Gemini API calls and just returns a placeholder summary.
    """
    if not issues:
        return "No issues to summarize."

    cache_file = CACHE_DIR / f"{repo.replace('/', '_')}_{label}.json"
    if cache_file.exists():
        with open(cache_file, "r") as f:
            return json.load(f)["summary"]

    # 🚫 Skip Gemini API, just hardcode text
    summary_text = f"Summary skipped for repo {repo} with label '{label}'."

    # Save summary to cache
    with open(cache_file, "w") as f:
        json.dump({"summary": summary_text}, f)

    return summary_text
