#!/usr/bin/env python3
import requests
import json
import os
import sys
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path

# Configuration
JIRA_URL = "https://redhat.atlassian.net"

# Set target directory to ./target in current working directory
TARGET_DIR = Path('./target')

# Create target directory if it doesn't exist
TARGET_DIR.mkdir(parents=True, exist_ok=True)

# Get auth string from environment variable (required, base64-encoded)
AUTH_STRING = os.environ.get('RH_MESSAGING_CI_JIRA_AUTH_STRING')
if not AUTH_STRING:
    raise ValueError("RH_MESSAGING_CI_JIRA_AUTH_STRING environment variable is required. Format: base64-encoded 'email:api_token'")

# Calculate date 7 days ago
seven_days_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

# JQL query for issues that are:
# 1. In Progress status OR
# 2. Moved to Dev Complete in the last 7 days
jql = f'project in (ENTMQBR, ENTMQCL) AND (status = "In Progress" OR (status = "Dev Complete" AND status changed to "Dev Complete" after {seven_days_ago}))'

# API endpoint
search_url = f"{JIRA_URL}/rest/api/2/search/jql"

# Request parameters
params = {
    'jql': jql,
    'fields': 'summary,assignee,versions,status',
    'maxResults': 100
}

# Make the request
print(f"Using AUTH_STRING: {AUTH_STRING}")
response = requests.get(
    search_url,
    params=params,
    headers={'Accept': 'application/json', 'Authorization': f'Basic {AUTH_STRING}'}
)

if response.status_code == 200:
    data = response.json()
    issues = data.get('issues', [])
    
    # Group issues by assignee
    issues_by_assignee = defaultdict(list)
    
    for issue in issues:
        key = issue['key']
        summary = issue['fields']['summary']
        assignee = issue['fields'].get('assignee')
        assignee_name = assignee['displayName'] if assignee else 'Unassigned'
        status = issue['fields']['status']['name']
        
        # Try to get target release from versions field
        versions = issue['fields'].get('versions', [])
        if versions and isinstance(versions, list) and len(versions) > 0:
            # Get the first version's name
            target_release = versions[0].get('name', 'N/A')
        else:
            target_release = 'N/A'
        
        issue_url = f"{JIRA_URL}/browse/{key}"
        issue_line = f"| [{key}]({issue_url}) | {summary} | {assignee_name} | {target_release} | {status} |"
        issues_by_assignee[assignee_name].append(issue_line)
    
    # Create markdown output as a table
    markdown_lines = ["# ENTMQBR & ENTMQCL Issues Report\n"]
    markdown_lines.append(f"*Issues In Progress or moved to Dev Complete in the last 7 days*\n")
    markdown_lines.append("| Issue | Summary | Assignee | Target Release | Status |")
    markdown_lines.append("|-------|---------|----------|----------------|--------|")
    
    # Sort by assignee and add all issues to table
    for assignee in sorted(issues_by_assignee.keys()):
        markdown_lines.extend(issues_by_assignee[assignee])
    
    # Write to file
    output_file = TARGET_DIR / 'entmqbr_issues_by_assignee.md'
    with open(output_file, 'w') as f:
        f.write('\n'.join(markdown_lines))
    
    print(f"Successfully fetched {len(issues)} issues")
    print(f"Grouped by {len(issues_by_assignee)} assignees")
    print(f"Output written to {output_file}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)