from src.github_api import fetch_issues
from src.agent import summarize_issues

def main():
    repo = "streamlit/streamlit"   # Example repo
    issues = fetch_issues(repo, label="bug")

    if not issues:
        print("No bug issues found.")
        return

    summary = summarize_issues(issues)
    print("=== Bug Issues Summary ===")
    print(summary)

if __name__ == "__main__":
    main()
