# Repository Support & Maintenance Tools

This directory contains all the maintenance scripts, utilities, and supporting files for The Batch Compendium repository management.

## 📁 Directory Structure

```
z.repo_support/
├── .assets/              # Supporting assets and resources
├── scripts/              # Maintenance and automation scripts
│   ├── find_batch_repos.sh          # Find new batch repositories on GitHub
│   ├── identify_batch_repos.py      # Python script for repository discovery
│   ├── update_script_count.sh       # Update batch script count in README
│   ├── update_description.sh        # Update GitHub repository description
│   ├── add_topics.sh               # Add topics/tags to GitHub repository
│   └── [other utility scripts]
├── batch_repos_found.csv # Latest repository discovery results
└── README.md            # This file
```

## 🛠️ Available Scripts

### Repository Discovery
- **`find_batch_repos.sh`** - Wrapper script to discover new batch repositories
- **`identify_batch_repos.py`** - Core Python script for GitHub API interaction and repository analysis

### Repository Maintenance  
- **`update_script_count.sh`** - Automatically counts and updates the batch script count in README.md
- **`update_description.sh`** - Updates the GitHub repository description
- **`add_topics.sh`** - Manages repository topics and tags

### Utility Scripts
- **Various other scripts** - Additional utilities for repository management and maintenance

## 🚀 Quick Start

### Using the Maintenance Launcher

From the repository root, use the `maintenance` script for easy access:

```bash
# Show available commands
./maintenance help

# Find new repositories (100+ stars)
./maintenance find-repos --min-stars 100 --max-results 50

# Update script count in README
./maintenance update-count

# Update repository description
./maintenance update-desc

# Add repository topics
./maintenance add-topics
```

### Direct Script Usage

You can also run scripts directly from the `z.repo_support/scripts/` directory:

```bash
# Find repositories directly
./z.repo_support/scripts/find_batch_repos.sh --min-stars 100

# Update script count
./z.repo_support/scripts/update_script_count.sh

# Update repository description  
./z.repo_support/scripts/update_description.sh
```

## 📋 Script Requirements

### Python Scripts
- **Python 3.x** required
- **requests** library: `pip install requests`
- **GitHub API token** (optional but recommended): Set `GITHUB_TOKEN` environment variable

### Bash Scripts
- **bash** shell environment
- **git** command line tools
- **gh** GitHub CLI (for some operations)

## 🔧 Configuration

### GitHub Token Setup
For higher API rate limits and full functionality:

1. Create a GitHub Personal Access Token: https://github.com/settings/tokens
2. Export the token: `export GITHUB_TOKEN=your_token_here`
3. Add to your shell profile for persistence

### Repository Discovery Configuration

The `find_batch_repos.sh` script accepts these parameters:

- `--min-stars N` - Minimum star count (default: 10)
- `--max-results N` - Maximum results to return (default: 100)
- `--output filename` - Output CSV file (default: batch_repos_found.csv)
- `--token TOKEN` - GitHub API token (can also use GITHUB_TOKEN env var)

## 📊 Output Files

### Repository Discovery Results
- **`batch_repos_found.csv`** - Complete results from repository discovery
- **Format**: name, url, description, stars, forks, language, created_at, updated_at

### Script Logs
- Most scripts provide console output with progress and results
- Error messages include helpful troubleshooting information

## 🔄 Maintenance Workflow

### Regular Maintenance Tasks

1. **Monthly Repository Discovery**:
   ```bash
   ./maintenance find-repos --min-stars 100 --max-results 50
   ```

2. **Update Documentation**:
   ```bash
   ./maintenance update-count
   ./maintenance update-desc
   ```

3. **Repository Organization**:
   ```bash
   ./maintenance add-topics
   ```

### Adding New Repositories

1. Run repository discovery to find candidates
2. Review the results CSV file
3. Manually filter and categorize high-quality repositories
4. Clone repositories into appropriate categories
5. Create documentation and update indexes
6. Commit and push changes

## 📝 Development Notes

### Script Conventions
- All bash scripts include proper error checking and help text
- Python scripts follow PEP 8 conventions
- Scripts are designed to be run from any directory
- Relative paths are resolved correctly

### Error Handling
- Scripts validate dependencies before execution  
- Clear error messages with suggested solutions
- Graceful handling of API rate limits and network issues

### Future Enhancements
- Automated repository quality assessment
- Batch processing for multiple repository operations  
- Integration with CI/CD pipelines
- Enhanced filtering and categorization algorithms

## 🤝 Contributing

When adding new maintenance scripts:

1. Follow existing naming conventions
2. Include comprehensive help text and documentation
3. Add error checking and validation
4. Update this README with script descriptions
5. Test scripts in various environments

## 📞 Support

For issues with maintenance scripts:

1. Check script help text: `script_name --help`
2. Verify all dependencies are installed
3. Check GitHub token permissions and rate limits
4. Review script output for specific error messages

---

*This directory keeps all maintenance tools organized and the main repository clean and professional.*