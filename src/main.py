from .github_api import fetch_issues
from .agent import summarize_issues

def main():
    repo = "suchitsharma2004/Chatapp"   # Example repo
    issues = fetch_issues(repo, label="bug")

    if not issues:
        print("No bug issues found.")
        return

    summary = summarize_issues(issues)
    print("=== Bug Issues Summary ===")
    print(summary)

if __name__ == "__main__":
    main()
