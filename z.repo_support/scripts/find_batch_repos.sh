#!/bin/bash
# Wrapper script to find highly rated batch script repositories

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="${SCRIPT_DIR}/identify_batch_repos.py"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if requests library is installed
if ! python3 -c "import requests" &> /dev/null; then
    echo "Error: Python 'requests' library is not installed"
    echo "Install it with: pip install requests"
    exit 1
fi

# Check if GITHUB_TOKEN is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Warning: GITHUB_TOKEN environment variable is not set"
    echo "API rate limits will be lower without authentication"
    echo ""
    echo "To set a token, visit: https://github.com/settings/tokens"
    echo "Then run: export GITHUB_TOKEN=your_token_here"
    echo ""
fi

# Run the Python script with all arguments passed through
python3 "$PYTHON_SCRIPT" "$@"
