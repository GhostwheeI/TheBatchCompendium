# Repository Discovery Tool - Usage Guide

This guide explains how to use the tools in this directory to identify highly-rated Windows batch script repositories on GitHub.

## Overview

The repository discovery tools help you:
- Find new Windows batch script repositories with high star counts
- Analyze existing repository collections
- Generate reports on batch script repositories
- Filter and organize repository data

## Available Tools

### 1. `identify_batch_repos.py`

A standalone Python script that searches GitHub for batch repositories using the GitHub API.

**Features:**
- Direct GitHub API integration
- Multiple search strategies
- Rate limit handling
- CSV export

**Requirements:**
- Python 3.6+
- `requests` library: `pip install requests`
- GitHub API token (optional but recommended)

**Usage:**
```bash
# Basic usage with environment variable token
export GITHUB_TOKEN="your_token_here"
python3 identify_batch_repos.py

# With command-line options
python3 identify_batch_repos.py \
    --token YOUR_TOKEN \
    --min-stars 100 \
    --max-results 200 \
    --output found_repos.csv

# Without token (lower rate limits)
python3 identify_batch_repos.py --min-stars 50 --output repos.csv
```

**Getting a GitHub Token:**
1. Visit https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: Only `public_repo` or no scopes needed for public searches
4. Copy the token and save it securely

### 2. `batch_repo_finder.py`

Analyzes and filters existing CSV files containing repository data.

**Features:**
- Load and analyze CSV files
- Filter by star count
- Remove duplicates
- Generate statistical reports
- Export filtered results

**Usage:**
```bash
# Generate a report from existing data
python3 batch_repo_finder.py repo_results.csv --report --min-stars 50

# Filter and save results
python3 batch_repo_finder.py repo_results.csv \
    --min-stars 100 \
    --output highly_rated.csv

# Both report and export
python3 batch_repo_finder.py repo_results.csv \
    --report \
    --min-stars 50 \
    --output filtered_repos.csv
```

### 3. `process_github_search.py`

Processes JSON responses from GitHub's Search API.

**Usage:**
```bash
# Save GitHub API response to a JSON file first, then:
python3 process_github_search.py search_results.json \
    --report \
    --min-stars 100 \
    --output processed_repos.csv

# Include archived repositories
python3 process_github_search.py search_results.json \
    --include-archived \
    --output all_repos.csv
```

### 4. `find_highly_rated_repos.sh`

A bash script that demonstrates the search methodology and analyzes existing data.

**Usage:**
```bash
bash find_highly_rated_repos.sh
```

This script:
- Shows recommended GitHub search queries
- Analyzes existing `repo_results.csv`
- Displays statistics about the current collection
- Lists top repositories by star count

### 5. `find_batch_repos.sh` (Root directory)

A convenient wrapper script for running `identify_batch_repos.py`.

**Usage:**
```bash
# From the repository root
./find_batch_repos.sh --min-stars 100 --max-results 50
```

## Manual GitHub Search

You can also manually search GitHub using these strategies:

### Search Queries

1. **By Language:**
   ```
   language:Batchfile stars:>100
   ```
   https://github.com/search?q=language:Batchfile+stars:%3E100&type=repositories&s=stars&o=desc

2. **By Keywords:**
   ```
   batch script windows stars:>50
   ```
   
3. **By File Extensions:**
   ```
   .bat OR .cmd stars:>50 language:Batchfile
   ```

4. **Specific Topics:**
   ```
   topic:batch-scripts stars:>50
   topic:windows-automation stars:>50
   ```

### Advanced Filters

- `stars:>N` - Repos with more than N stars
- `forks:>N` - Repos with more than N forks
- `language:Batchfile` - Only Batchfile repositories
- `pushed:>YYYY-MM-DD` - Recently updated repos
- `created:>YYYY-MM-DD` - Recently created repos
- `archived:false` - Exclude archived repositories

### Example Advanced Search
```
language:Batchfile stars:>100 pushed:>2023-01-01 archived:false
```

## Workflow for Adding New Repositories

1. **Search for Repositories:**
   ```bash
   # Using the Python script
   export GITHUB_TOKEN="your_token"
   python3 identify_batch_repos.py --min-stars 100 --output new_finds.csv
   ```

2. **Analyze Results:**
   ```bash
   # Generate a report
   python3 batch_repo_finder.py new_finds.csv --report
   ```

3. **Filter and Merge:**
   ```bash
   # Filter by higher star count
   python3 batch_repo_finder.py new_finds.csv \
       --min-stars 100 \
       --output high_quality.csv
   ```

4. **Review Manually:**
   - Open the CSV file
   - Check each repository for relevance
   - Verify it contains actual batch scripts
   - Ensure it's not a duplicate

5. **Add to Main Collection:**
   - Merge with existing `repo_results.csv`
   - Remove duplicates
   - Update the main repository structure

## Tips and Best Practices

### Search Strategy

1. **Start Broad, Then Narrow:**
   - Begin with `language:Batchfile stars:>100`
   - Then refine with specific keywords

2. **Multiple Searches:**
   - Run several searches with different criteria
   - Combine results and remove duplicates

3. **Check for Activity:**
   - Look for recently updated repos (`pushed:>YYYY-MM-DD`)
   - Active projects are more likely to be maintained

### Quality Criteria

When evaluating repositories, consider:

- ✅ **Star Count:** Higher stars indicate popularity
- ✅ **Recent Activity:** Recently updated (within last year)
- ✅ **Clear Purpose:** Good description and README
- ✅ **Actual Scripts:** Contains real .bat/.cmd files
- ✅ **Documentation:** Has usage instructions
- ❌ **Archived:** Avoid archived/unmaintained projects
- ❌ **Malicious:** Check for malware or suspicious scripts
- ❌ **Low Quality:** Avoid test repos or experiments

### Rate Limiting

- **Without Token:** 60 requests/hour
- **With Token:** 5,000 requests/hour
- **Best Practice:** Always use a token for serious searches

### Data Management

1. **Keep backups** of CSV files
2. **Track search dates** in filenames
3. **Document your search criteria**
4. **Regular updates:** Re-run searches monthly

## Troubleshooting

### "403 Forbidden" Error
- **Cause:** Rate limit exceeded or no authentication
- **Solution:** Use a GitHub token or wait for rate limit reset

### "requests module not found"
- **Cause:** Python requests library not installed
- **Solution:** `pip install requests`

### Empty Results
- **Cause:** Too restrictive search criteria
- **Solution:** Lower the minimum star count or broaden search terms

### Duplicates in Results
- **Cause:** Different search queries finding same repos
- **Solution:** Use `batch_repo_finder.py` to remove duplicates

## Example Session

Here's a complete example of finding and analyzing repos:

```bash
# 1. Set up environment
export GITHUB_TOKEN="ghp_your_token_here"

# 2. Search for repos
python3 identify_batch_repos.py \
    --min-stars 50 \
    --max-results 100 \
    --output search_results.csv

# 3. Analyze results
python3 batch_repo_finder.py search_results.csv --report

# 4. Filter high-quality ones
python3 batch_repo_finder.py search_results.csv \
    --min-stars 100 \
    --output top_repos.csv

# 5. Review and manually validate top_repos.csv
```

## Contributing Back

After finding new repositories:

1. Review each repository manually
2. Test some of the scripts if possible
3. Add appropriate categorization
4. Update the main repository documentation
5. Submit your findings via pull request

## Additional Resources

- [GitHub Search Documentation](https://docs.github.com/en/search-github/searching-on-github)
- [GitHub REST API](https://docs.github.com/en/rest)
- [Creating GitHub Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

## Support

For issues or questions:
- Check the repository README
- Review existing issues on GitHub
- Open a new issue with details about your problem
