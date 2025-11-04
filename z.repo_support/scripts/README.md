# Repository Discovery Scripts

This directory contains scripts to identify and discover highly-rated Windows batch script repositories on GitHub.

## 📚 Documentation

- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Comprehensive guide on using all the tools
- **[HIGHLY_RATED_REPOS.md](HIGHLY_RATED_REPOS.md)** - List of top batch repositories found on GitHub
- **[../../CONTRIBUTING_REPOS.md](../../CONTRIBUTING_REPOS.md)** - Guide for contributing new repositories

## Scripts

### `identify_batch_repos.py`

A Python script that searches GitHub for repositories containing Windows batch scripts and filters them by star count to identify popular and well-maintained projects.

#### Features

- Searches GitHub using multiple query strategies to find batch script repositories
- Filters repositories by minimum star count
- Removes duplicates automatically
- Saves results to CSV format
- Respects GitHub API rate limits
- Supports GitHub API token for higher rate limits

#### Requirements

- Python 3.6 or higher
- `requests` library: `pip install requests`

#### Usage

Basic usage (requires GitHub token in environment):

```bash
export GITHUB_TOKEN="your_github_token_here"
python identify_batch_repos.py
```

With command-line options:

```bash
python identify_batch_repos.py --token YOUR_TOKEN --min-stars 50 --max-results 200 --output my_repos.csv
```

#### Command-line Options

- `--token`: GitHub API token (optional but recommended). Can also be set via `GITHUB_TOKEN` environment variable
- `--min-stars`: Minimum star count to consider a repository (default: 10)
- `--max-results`: Maximum number of results to return (default: 100)
- `--output`: Output CSV file name (default: batch_repos_found.csv)

#### Output Format

The script generates a CSV file with the following columns:

- `name`: Full repository name (owner/repo)
- `url`: Repository URL
- `description`: Repository description
- `stars`: Star count
- `forks`: Fork count
- `language`: Primary language
- `created_at`: Creation date
- `updated_at`: Last update date

#### Example Output

```
Found: massgravel/Microsoft-Activation-Scripts (140376 stars)
Found: awesome-windows11/windows11 (2723 stars)
Found: AveYo/MediaCreationTool.bat (9647 stars)
...
Saved 100 repositories to batch_repos_found.csv
```

#### GitHub Token

To avoid rate limiting, it's recommended to use a GitHub personal access token. You can create one at:
https://github.com/settings/tokens

The token only needs public repository read access (no special scopes required for public repos).

#### Rate Limits

- Without authentication: 60 requests per hour
- With authentication: 5000 requests per hour

The script automatically handles rate limiting and will wait if necessary.

## Existing Data

### `repo_results.csv`

Contains a curated list of batch script repositories that have already been identified and reviewed.

## Contributing

When adding new repositories to the collection:

1. Run the discovery script to find new repositories
2. Review the results manually
3. Filter out any inappropriate or low-quality repositories
4. Merge with existing `repo_results.csv`
5. Update the main repository structure with new scripts/repositories
