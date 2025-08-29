import re

def map_issues_to_prs(issues, prs):
    """
    Try to map issues <-> PRs based on references in PR body/title.
    - issues: list of dicts from GitHubClient.get_issues()
    - prs: list of dicts from GitHubClient.get_pull_requests()

    Returns: dict -> {issue_number: [list_of_prs]}
    """
    issue_map = {issue["number"]: [] for issue in issues}

    for pr in prs:
        text_to_search = f"{pr['title']} {pr['body']}"
        mentioned_issues = re.findall(r"#(\d+)", text_to_search)  # matches "#123"

        for num in mentioned_issues:
            num = int(num)
            if num in issue_map:
                issue_map[num].append(pr)

    return issue_map


def pretty_print_mapping(issues, issue_map):
    """Nicely print which PRs solve which issues."""
    for issue in issues:
        print(f"\n🪲 Issue #{issue['number']}: {issue['title']}")
        prs = issue_map.get(issue["number"], [])
        if prs:
            for pr in prs:
                print(f"   ↳ 🔧 PR #{pr['number']}: {pr['title']} ({pr['url']})")
        else:
            print("   ↳ ❌ No PR linked yet.")
