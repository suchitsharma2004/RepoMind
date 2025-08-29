# github_client.py
import os
import requests

GITHUB_API_URL = "https://api.github.com"

class GitHubClient:
    def __init__(self, repo):
        """
        repo: str -> in the format "owner/repo" (e.g., "tensorflow/tensorflow")
        """
        self.repo = repo
        self.token = os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("⚠️ Please set your GITHUB_TOKEN in the .env file.")
        
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_issues(self, label="bug", state="open", limit=50):
        """Fetch issues with a given label."""
        url = f"{GITHUB_API_URL}/repos/{self.repo}/issues"
        params = {"labels": label, "state": state, "per_page": limit}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        issues = response.json()

        # Filter out PRs (issues API also returns PRs sometimes)
        return [
            {
                "number": i["number"],
                "title": i["title"],
                "body": i.get("body", ""),
                "url": i["html_url"]
            }
            for i in issues if "pull_request" not in i
        ]

    def get_pull_requests(self, state="open", limit=50):
        """Fetch pull requests."""
        url = f"{GITHUB_API_URL}/repos/{self.repo}/pulls"
        params = {"state": state, "per_page": limit}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        prs = response.json()

        return [
            {
                "number": pr["number"],
                "title": pr["title"],
                "body": pr.get("body", ""),
                "url": pr["html_url"]
            }
            for pr in prs
        ]
