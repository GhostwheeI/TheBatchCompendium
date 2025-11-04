#!/bin/bash
# Setup script for The Batch Compendium Automation System
# This script prepares the automation system for use

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"

echo "🚀 Setting up The Batch Compendium Automation System"
echo "=================================================="
echo "Script directory: $SCRIPT_DIR"
echo "Base directory: $BASE_DIR"
echo ""

# Check Python version
echo "🐍 Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ $PYTHON_VERSION found"
else
    echo "❌ Python 3 is required but not found"
    echo "Please install Python 3.6 or higher"
    exit 1
fi

# Check and install Python dependencies
echo ""
echo "📦 Checking Python dependencies..."
if python3 -c "import requests" &> /dev/null; then
    echo "✅ requests library is installed"
else
    echo "📦 Installing requests library..."
    pip3 install requests || {
        echo "❌ Failed to install requests. Try: pip3 install --user requests"
        exit 1
    }
fi

# Make Python scripts executable
echo ""
echo "🔧 Setting up script permissions..."
PYTHON_SCRIPTS=(
    "identify_batch_repos.py"
    "process_new_discoveries.py"
    "integrate_repositories.py"
    "generate_highly_rated_docs.py"
    "update_collection.py"
    "quality_filter.py"
    "notification_manager.py"
    "automate_discovery.py"
    "batch_repo_finder.py"
    "process_github_search.py"
)

for script in "${PYTHON_SCRIPTS[@]}"; do
    if [ -f "$SCRIPT_DIR/$script" ]; then
        chmod +x "$SCRIPT_DIR/$script"
        echo "✅ Made $script executable"
    else
        echo "⚠️ Warning: $script not found"
    fi
done

# Make shell scripts executable
SHELL_SCRIPTS=(
    "find_highly_rated_repos.sh"
    "find_batch_repos.sh"
    "update_script_count.sh"
    "update_description.sh"
    "add_topics.sh"
)

for script in "${SHELL_SCRIPTS[@]}"; do
    if [ -f "$SCRIPT_DIR/$script" ]; then
        chmod +x "$SCRIPT_DIR/$script"
        echo "✅ Made $script executable"
    else
        echo "⚠️ Warning: $script not found"
    fi
done

# Create necessary directories
echo ""
echo "📁 Creating necessary directories..."
mkdir -p "$SCRIPT_DIR/.github/workflows"
echo "✅ Created .github/workflows directory"

# Check for required files
echo ""
echo "📋 Checking required files..."
REQUIRED_FILES=(
    "repo_results.csv"
    "README.md"
    "USAGE_GUIDE.md"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$SCRIPT_DIR/$file" ]; then
        echo "✅ Found $file"
    else
        echo "⚠️ Warning: $file not found"
    fi
done

# Test GitHub token (if available)
echo ""
echo "🔑 Checking GitHub token..."
if [ -n "$GITHUB_TOKEN" ]; then
    echo "✅ GITHUB_TOKEN environment variable is set"
    
    # Test token validity
    if curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user > /dev/null; then
        echo "✅ GitHub token is valid"
    else
        echo "⚠️ Warning: GitHub token may be invalid"
    fi
else
    echo "⚠️ GITHUB_TOKEN not set. You can set it with:"
    echo "   export GITHUB_TOKEN='your_token_here'"
    echo "   Get a token at: https://github.com/settings/tokens"
fi

# Test basic functionality
echo ""
echo "🧪 Testing basic functionality..."
cd "$SCRIPT_DIR"

# Test help output
if python3 automate_discovery.py --help > /dev/null 2>&1; then
    echo "✅ Main automation script works"
else
    echo "❌ Main automation script has issues"
    exit 1
fi

# Test dry run
echo "🔍 Testing dry run..."
if python3 automate_discovery.py --dry-run --min-stars 100 --max-results 10 > /dev/null 2>&1; then
    echo "✅ Dry run test passed"
else
    echo "❌ Dry run test failed"
    exit 1
fi

# Create example usage script
echo ""
echo "📝 Creating usage examples..."
cat > "$SCRIPT_DIR/run_automation_example.sh" << 'EOF'
#!/bin/bash
# Example script to run The Batch Compendium automation

# Set your GitHub token (get one at https://github.com/settings/tokens)
export GITHUB_TOKEN="ghp_your_token_here"

# Navigate to scripts directory
cd "$(dirname "$0")"

# Run automation with custom settings
python3 automate_discovery.py \
  --min-stars 50 \
  --max-results 100 \
  --notifications console file \
  --cleanup

echo "Automation completed! Check the logs for results."
EOF

chmod +x "$SCRIPT_DIR/run_automation_example.sh"
echo "✅ Created run_automation_example.sh"

# Create status check script
cat > "$SCRIPT_DIR/check_status.sh" << 'EOF'
#!/bin/bash
# Check the status of the automation system

cd "$(dirname "$0")"

echo "📊 The Batch Compendium Automation Status"
echo "========================================"

# Check last automation run
if [ -f "automation_notifications.log" ]; then
    echo "📅 Last automation run:"
    tail -n 10 automation_notifications.log | head -n 3
    echo ""
fi

# Check repository count
if [ -f "repo_results.csv" ]; then
    REPO_COUNT=$(tail -n +2 repo_results.csv | wc -l)
    echo "📈 Current repository count: $REPO_COUNT"
else
    echo "⚠️ Repository database not found"
fi

# Check for recent discovery files
echo ""
echo "📁 Recent discovery files:"
ls -lt discovered_repos_*.csv 2>/dev/null | head -n 3 || echo "No recent discovery files found"

echo ""
echo "✅ Status check complete"
EOF

chmod +x "$SCRIPT_DIR/check_status.sh"
echo "✅ Created check_status.sh"

# Summary
echo ""
echo "🎉 Setup Complete!"
echo "=================="
echo ""
echo "✅ All scripts are now executable"
echo "✅ Dependencies are installed"
echo "✅ Directory structure is ready"
echo "✅ Example scripts created"
echo ""
echo "📖 Next Steps:"
echo "1. Set your GitHub token: export GITHUB_TOKEN='your_token_here'"
echo "2. Test the system: python3 automate_discovery.py --dry-run"
echo "3. Run automation: python3 automate_discovery.py"
echo "4. Check results: ./check_status.sh"
echo ""
echo "📚 Documentation:"
echo "- AUTOMATION_GUIDE.md - Complete system documentation"
echo "- USAGE_GUIDE.md - Detailed usage instructions"
echo "- README.md - Overview and quick start"
echo ""
echo "🔧 Example Scripts:"
echo "- run_automation_example.sh - Example automation run"
echo "- check_status.sh - Check system status"
echo ""
echo "🤖 GitHub Actions:"
echo "The system will automatically run every 2 weeks via GitHub Actions."
echo "You can also trigger it manually from the Actions tab on GitHub."
echo ""
echo "Happy automating! 🚀"