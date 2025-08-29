import requests
import os
from src.config import GITHUB_TOKEN

def fetch_issues(repo: str, label: str = "bug"):
    """
    Fetch issues from a GitHub repository with a given label.
    repo format: 'owner/repo'
    """
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    params = {"labels": label, "state": "open"}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}, {response.text}")
    
    issues = response.json()
    return [
        {
            "title": issue["title"],
            "body": issue.get("body", ""),
            "url": issue["html_url"]
        }
        for issue in issues if "pull_request" not in issue  # filter out PRs
    ]
