#!/bin/bash
# Script to find highly rated batch script repositories using GitHub search
# This script demonstrates how to identify batch-based solutions with high star counts

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_FILE="${SCRIPT_DIR}/newly_found_repos.csv"

echo "Finding highly rated Windows batch script repositories..."
echo ""

# Create CSV header
echo "name,url,description,stars,language" > "$OUTPUT_FILE"

# Note: This is a template script showing the approach
# In practice, you would use GitHub's search API or the gh CLI
# Example search queries to use:
# - language:Batchfile stars:>100
# - batch script windows stars:>50
# - .bat OR .cmd stars:>100

echo "Search strategy:"
echo "1. Search for repos with language:Batchfile and high stars"
echo "2. Search for repos with 'batch script' or 'windows batch' keywords"
echo "3. Filter for repos with .bat or .cmd files"
echo "4. Sort by star count to find the most popular ones"
echo ""

echo "To manually search GitHub, use these queries:"
echo "  - language:Batchfile stars:>100"
echo "  - language:Batchfile stars:>50 sort:stars"
echo "  - batch script windows stars:>100"
echo "  - .bat OR .cmd stars:>50 language:Batchfile"
echo ""

echo "Visit: https://github.com/search?q=language:Batchfile+stars:%3E100&type=repositories&s=stars&o=desc"
echo ""

# For demonstration, let's analyze the existing repo_results.csv
EXISTING_FILE="${SCRIPT_DIR}/repo_results.csv"

if [ -f "$EXISTING_FILE" ]; then
    echo "Analyzing existing repository data from repo_results.csv..."
    echo ""
    
    # Count total repos
    TOTAL_REPOS=$(tail -n +2 "$EXISTING_FILE" | wc -l)
    echo "Total repositories in collection: $TOTAL_REPOS"
    
    # Count repos by star ranges
    HIGHLY_POPULAR=$(tail -n +2 "$EXISTING_FILE" | awk -F',' '$4 >= 1000 {count++} END {print count+0}')
    POPULAR=$(tail -n +2 "$EXISTING_FILE" | awk -F',' '$4 >= 100 && $4 < 1000 {count++} END {print count+0}')
    NOTABLE=$(tail -n +2 "$EXISTING_FILE" | awk -F',' '$4 >= 50 && $4 < 100 {count++} END {print count+0}')
    
    echo "Highly Popular (1000+ stars): $HIGHLY_POPULAR"
    echo "Popular (100-999 stars): $POPULAR"
    echo "Notable (50-99 stars): $NOTABLE"
    echo ""
    
    echo "Top 10 repositories by stars:"
    tail -n +2 "$EXISTING_FILE" | sort -t',' -k4 -rn | head -10 | \
    while IFS=',' read -r name url desc stars rest; do
        echo "  - $name ($stars stars)"
    done
    echo ""
fi

echo "This script demonstrates the methodology for finding highly-rated repos."
echo "To collect new repositories, you would typically:"
echo "  1. Use GitHub API or gh CLI to search"
echo "  2. Filter results by star count and language"
echo "  3. Remove duplicates from existing collection"
echo "  4. Save new discoveries to CSV for review"
echo ""
echo "See identify_batch_repos.py for the full implementation."
