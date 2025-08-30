import re
from typing import List, Dict
from langchain_google_genai import ChatGoogleGenerativeAI

# Use free Gemini model
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

import os
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()  # must be called before accessing os.getenv

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def map_prs_to_issues(issues: List[Dict], prs: List[Dict]):
    issue_map = {i["number"]: i for i in issues}   # quick lookup by issue number
    mapping = {i["number"]: [] for i in issues}

    for pr in prs:
        pr_text = f"{pr['title']} {pr.get('body', '')}"

        # --- Step 1: Regex match (#123) ---
        match = re.findall(r"#(\d+)", pr_text)
        if match:
            for issue_id in match:
                issue_id = int(issue_id)
                if issue_id in mapping:
                    mapping[issue_id].append(pr)
            continue  # move to next PR if regex worked

        # --- Step 2: Gemini fallback ---
        for issue in issues:
            prompt = f"""
            You are given a GitHub issue and a pull request.

            Issue:
            Title: {issue['title']}
            Body: {issue['body']}

            PR:
            Title: {pr['title']}
            Body: {pr.get('body','')}

            Question: Does this PR likely solve this issue? Answer with "YES" or "NO" only.
            """
            resp = llm.invoke(prompt)
            if "YES" in resp.content.upper():
                mapping[issue["number"]].append(pr)
                break  # assume one best match is enough

    return mapping
# utils.py

def print_issue_pr_report(mapping, return_str=False):
    """
    mapping: dict {issue_number: [list_of_prs]}
    return_str: if True, return string instead of printing
    """
    lines = []
    for issue_num, prs in mapping.items():
        if prs:
            lines.append(f"Issue #{issue_num} is addressed by PRs:")
            for pr in prs:
                lines.append(f"  - PR #{pr['number']}: {pr['title']} ({pr['url']})")
        else:
            lines.append(f"Issue #{issue_num} has no linked PRs.")
    
    if return_str:
        return "\n".join(lines)
    else:
        print("\n".join(lines))

    