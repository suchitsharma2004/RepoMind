import streamlit as st
import pandas as pd
from github_client import GitHubClient
from agent import summarize_issues
from utils import map_prs_to_issues

def run_ui():
    st.title("🐙 GitHub Issues & PR Tracker")
    st.write("Fetch issues and PRs summary for a repository.")

    # User input for repo and label
    repo = st.text_input("Enter GitHub repo (owner/repo):", "suchitsharma2004/Chatapp")
    label = st.text_input("Enter label to filter issues:", "bug")

    if st.button("Fetch Data"):
        try:
            client = GitHubClient(repo)

            # Fetch issues
            issues = client.get_issues(label=label)
            if not issues:
                st.warning("⚠️ No issues found with this label.")
                return

            # Summarize issues
            summary = summarize_issues(issues)
            st.subheader("📝 Summary of Issues")
            st.write(summary)

            # Show issues in table
            st.subheader("📋 Bug Issues")
            issues_df = pd.DataFrame([
                {"Number": i["number"], 
                 "Title": i["title"], 
                 "URL": i["url"], 
                 "Body": i["body"][:100] + ("..." if len(i["body"])>100 else "")} 
                for i in issues
            ])
            st.dataframe(issues_df)

            # Fetch PRs
            prs = client.get_pull_requests()
            if not prs:
                st.warning("⚠️ No pull requests found.")
                return

            # Map PRs to issues
            mapping = map_prs_to_issues(prs, issues)
            st.subheader("🔗 Issue → PR Mapping")
            mapping_data = []
            for issue_num, pr_list in mapping.items():
                for pr in pr_list:
                    mapping_data.append({
                        "Issue #": issue_num,
                        "PR #": pr["number"],
                        "PR Title": pr["title"],
                        "PR URL": pr["url"]
                    })
            if mapping_data:
                mapping_df = pd.DataFrame(mapping_data)
                st.dataframe(mapping_df)
            else:
                st.info("No PRs are linked to the fetched issues.")

        except Exception as e:
            st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    run_ui()
