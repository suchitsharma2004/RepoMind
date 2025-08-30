from src.github_client import GitHubClient
# from src.agent import summarize_issues
from src.utils import map_prs_to_issues

def main(repo="suchitsharma2004/Chatapp", label="bug"):
    client = GitHubClient(repo)

    # Fetch issues
    issues = client.get_issues(label=label)
    if not issues:
        return {"issues": [], "mapping": {}, "summary_text": "⚠️ No issues found."}

    # Summarize with RAG + Gemini
    # summary_text = summarize_issues(issues, repo=repo, label=label)
    summary_text = "⏩ Summary skipped for testing."

    # Fetch PRs and map
    prs = client.get_pull_requests()
    mapping = map_prs_to_issues(prs, issues)

    return {
        "issues": issues,
        "mapping": mapping,
        "summary_text": summary_text
    }

# from src.github_client import GitHubClient
# from src.utils import map_prs_to_issues

# def main(repo="suchitsharma2004/Chatapp", label="bug"):
#     client = GitHubClient(repo)

#     # Fetch issues
#     issues = client.get_issues(label=label)
#     if not issues:
#         return {"issues": [], "mapping": {}, "summary_text": "⚠️ No issues found."}

#     # 🚫 Skip summarization for now
#     summary_text = "⏩ Summary skipped for testing."

#     # Fetch PRs and map
#     prs = client.get_pull_requests()
#     mapping = map_prs_to_issues(prs, issues)

#     return {
#         "issues": issues,
#         "mapping": mapping,
#         "summary_text": summary_text
#     }
