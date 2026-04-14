# JIRA Issues Fetcher

This script fetches JIRA issues from the ENTMQBR and ENTMQCL projects and generates a markdown report in table format.

## What it does

The script connects to Red Hat's JIRA instance (https://redhat.atlassian.net) using the JIRA API v2 endpoint and retrieves issues that are either:
- Currently in "In Progress" status, OR
- Moved to "Dev Complete" status in the last 7 days

The results are displayed in a single table sorted by assignee, with each issue key as a clickable link to the JIRA page.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)

## Setup

### 1. Create the authentication token

The script requires a base64-encoded authentication string in the format `email:api_token`.

To create this:
```bash
# Create a file with your credentials (email:api_token format)
echo "your.email@redhat.com:YOUR_JIRA_API_TOKEN" > apitoken_clean.txt

# Encode it to base64
cat apitoken_clean.txt | base64 -w 0 > apitoken64.txt
```

### 2. Set the environment variable

```bash
export RH_MESSAGING_CI_JIRA_AUTH_STRING=$(cat apitoken64.txt)
```

Or set it directly:
```bash
export RH_MESSAGING_CI_JIRA_AUTH_STRING="YXRheWxvckByZWRoYXQuY29tOkFUQVRUM3hGZkdGMDFGWm1yY0IxX1ZtNE9rdlFVTHNZZVhaVi1MdTRkcjdHWHNJMDRSdjdFNVZiaHVUa1U4ZE1fcllBQUN4TGpCX1V2eUVIdk02XzBtRDZ0djh0a3YzdlZGOXZ3QlpHbFlscThzeFVqRWEyVnM0czhwZjQyXzFHSTdqeVo1SF9EUFZvWGk3RDlOdl9OMHJhcXFPNWZ3LWxxeGlzMDdJNVdLeERYNVBZUHFGeV9adG89RTQyNkQ2NDE="
```

## Usage

```bash
python3 fetch_jira_by_assignee.py
```

## Output

The script automatically creates a `target` directory in the current working directory and generates a file named `target/entmqbr_issues_by_assignee.md` containing:
- A header with the report title
- A single table with all issues sorted by assignee
- Each issue key is a clickable link to the JIRA page
- Columns: Issue, Summary, Assignee, Target Release, Status

Example output:
```markdown
# ENTMQBR & ENTMQCL Issues Report

*Issues In Progress or Dev Complete*

| Issue | Summary | Assignee | Target Release | Status |
|-------|---------|----------|----------------|--------|
| [ENTMQBR-12345](https://redhat.atlassian.net/browse/ENTMQBR-12345) | Fix authentication bug | John Doe | AMQ 7.13.0.GA | In Progress |
| [ENTMQBR-12346](https://redhat.atlassian.net/browse/ENTMQBR-12346) | Update documentation | John Doe | N/A | Dev Complete |
| [ENTMQCL-3122](https://redhat.atlassian.net/browse/ENTMQCL-3122) | Add TLS support | Jane Smith | N/A | In Progress |
```

## Troubleshooting

### Missing environment variable
If you see:
```
ValueError: RH_MESSAGING_CI_JIRA_AUTH_STRING environment variable is required
```

Make sure you've set the `RH_MESSAGING_CI_JIRA_AUTH_STRING` environment variable as described in the Setup section.

### Authentication errors
If you get authentication errors, verify:
1. Your JIRA API token is valid
2. The base64 encoding is correct
3. The format is `email:api_token` (with colon separator)

## Files

- `fetch_jira_by_assignee.py` - Main script
- `apitoken_clean.txt` - Plain text credentials (email:api_token)
- `apitoken64.txt` - Base64-encoded credentials
- `target/entmqbr_issues_by_assignee.md` - Generated report (output)
