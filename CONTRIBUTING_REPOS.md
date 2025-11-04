# Contributing New Batch Script Repositories

This guide explains how to find and contribute new highly-rated Windows batch script repositories to this collection.

## Quick Start

The easiest way to find new repositories is to use our automated tools:

```bash
# 1. Run the discovery script
./find_batch_repos.sh --min-stars 100 --max-results 50

# 2. Review the results in batch_repos_found.csv

# 3. Submit high-quality finds via pull request
```

## Tools Available

We provide several tools to help identify highly-rated batch repositories:

### Automated Search Tools

1. **`find_batch_repos.sh`** - Main wrapper script
2. **`z.repo_support/scripts/identify_batch_repos.py`** - Python search tool
3. **`z.repo_support/scripts/batch_repo_finder.py`** - CSV analyzer
4. **`z.repo_support/scripts/find_highly_rated_repos.sh`** - Demo/analysis script

See `z.repo_support/scripts/USAGE_GUIDE.md` for detailed usage instructions.

## Manual Search Method

### GitHub Search Queries

Use these search queries on GitHub to find batch repositories:

1. **Primary Search:**
   ```
   language:Batchfile stars:>100
   ```
   [🔍 Search GitHub](https://github.com/search?q=language:Batchfile+stars:%3E100&type=repositories&s=stars&o=desc)

2. **Topic-Based:**
   ```
   topic:batch-scripts stars:>50
   topic:windows-automation stars:>50
   ```

3. **Keyword-Based:**
   ```
   batch script windows stars:>50
   windows automation .bat stars:>50
   ```

### Evaluation Criteria

When evaluating repositories, look for:

✅ **High Quality Indicators:**
- ⭐ High star count (50+ for notable, 100+ for popular)
- 📅 Recent activity (updated within last year)
- 📝 Clear documentation (README with usage instructions)
- 🎯 Specific purpose (solves a real problem)
- ✅ Active maintenance (responds to issues)
- 💻 Actual batch scripts (.bat or .cmd files)

❌ **Red Flags:**
- 🗄️ Archived repositories
- 🐛 No documentation or unclear purpose
- 🧪 Test/experimental repos with no real value
- ⚠️ Potential malware or suspicious code
- 📁 No actual batch files in the repo

## Star Count Tiers

Repositories are typically categorized by popularity:

- **🌟 Highly Popular:** 1,000+ stars
- **⭐ Popular:** 100-999 stars
- **✨ Notable:** 50-99 stars
- **💫 Active:** 10-49 stars

Focus on repositories with 50+ stars for this collection.

## Submission Process

### 1. Find Repositories

Use the automated tools or manual search:

```bash
# Option A: Automated search
export GITHUB_TOKEN="your_github_token"
python3 z.repo_support/scripts/identify_batch_repos.py --min-stars 100

# Option B: Manual GitHub search
# Visit the search links above and collect repository info
```

### 2. Verify Quality

For each repository found:

1. Visit the repository on GitHub
2. Check star count and last update date
3. Review the README and documentation
4. Verify it contains actual batch scripts
5. Check it's not already in our collection
6. Ensure it's not archived or abandoned

### 3. Collect Information

Gather this information for each repository:

- **Name:** `owner/repository-name`
- **URL:** Full GitHub URL
- **Description:** Brief description of what it does
- **Stars:** Current star count
- **Category:** Where it fits in our structure

### 4. Submit Contribution

**Option A: Via Pull Request (Preferred)**

1. Fork this repository
2. Add new repos to `z.repo_support/scripts/repo_results.csv`
3. Update relevant category READMEs
4. Create a pull request with your additions

**Option B: Via Issue**

1. Open a new issue
2. Title: "New Repository Suggestion: [repo-name]"
3. Include all collected information
4. Tag with `enhancement` label

## File Organization

When adding repositories to the collection:

### CSV Format

Add entries to `z.repo_support/scripts/repo_results.csv`:

```csv
name,url,description,stars,category
owner/repo-name,https://github.com/owner/repo-name,Description here,150,System Tweaks & Performance Enhancements
```

### Category Assignment

Match repositories to these categories:

- **Activation, Licensing & Update Scripts**
- **Automation & Installers**
- **Cleanup & Maintenance**
- **File, Media & Conversion Tools**
- **Game Server & Mod Utilities**
- **Network, Connectivity & Hardware Tweaks**
- **Privacy & Debloating**
- **Scripting Libraries, Examples & Tutorials**
- **Security, Hardening & Diagnostics**
- **Single-Function Scripts**
- **System Optimization & Performance**
- **Other & Uncategorized**

## Best Practices

### Search Strategy

1. **Start with high-quality repos** (100+ stars)
2. **Check for recent activity** (updated in last 12 months)
3. **Verify actual batch content** (not just tagged with batch)
4. **Look for unique solutions** (not duplicates)

### Documentation

When submitting:

1. **Accurate descriptions** - Clearly explain what the repository does
2. **Correct categorization** - Place in appropriate category
3. **Complete information** - Include all required fields
4. **No duplicates** - Check existing entries first

### Quality Over Quantity

- Focus on **useful, well-maintained** repositories
- Prioritize **active projects** over abandoned ones
- Include **diverse solutions** covering different use cases
- Ensure **quality documentation** in submitted repos

## GitHub API Token

For automated searches, you'll need a GitHub token:

### Creating a Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name it (e.g., "Batch Repo Search")
4. Select scopes: `public_repo` (or none for public searches)
5. Generate and copy the token
6. Store it securely

### Using the Token

```bash
# Set environment variable
export GITHUB_TOKEN="ghp_your_token_here"

# Or pass directly to script
python3 identify_batch_repos.py --token ghp_your_token_here
```

**Security Note:** Never commit tokens to Git or share them publicly!

## Example Workflow

Complete example of finding and submitting new repos:

```bash
# 1. Set up GitHub token
export GITHUB_TOKEN="your_token_here"

# 2. Search for repos
python3 z.repo_support/scripts/identify_batch_repos.py \
    --min-stars 100 \
    --max-results 100 \
    --output new_discoveries.csv

# 3. Analyze results
python3 z.repo_support/scripts/batch_repo_finder.py \
    new_discoveries.csv \
    --report \
    --min-stars 100

# 4. Review the CSV file manually
# - Check each repository on GitHub
# - Verify quality and relevance
# - Remove duplicates and low-quality entries

# 5. Add to main collection
# - Edit z.repo_support/scripts/repo_results.csv
# - Add your new entries
# - Update category READMEs if needed

# 6. Submit via pull request
git checkout -b add-new-repos
git add z.repo_support/scripts/repo_results.csv
git commit -m "Add newly discovered batch repositories"
git push origin add-new-repos
# Then create a pull request on GitHub
```

## Questions?

- 📖 Read the detailed guide: `z.repo_support/scripts/USAGE_GUIDE.md`
- 🐛 Report issues on GitHub
- 💬 Discuss in repository discussions

## Thank You!

Your contributions help make this the most comprehensive collection of Windows batch scripts on GitHub! 🎉
