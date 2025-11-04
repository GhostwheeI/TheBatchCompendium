#!/bin/bash
# Script to manage and verify The Batch Compendium automation schedule

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKFLOW_FILE="$REPO_ROOT/.github/workflows/discover-repositories.yml"

echo "🕒 The Batch Compendium - Automation Schedule Manager"
echo "=================================================="
echo ""

# Check if workflow file exists
if [ ! -f "$WORKFLOW_FILE" ]; then
    echo "❌ Error: GitHub Actions workflow not found at $WORKFLOW_FILE"
    echo "Run setup_automation.sh first to set up the system."
    exit 1
fi

echo "📅 Current Schedule Configuration:"
echo "---------------------------------"

# Extract and display schedule
if grep -q "schedule:" "$WORKFLOW_FILE"; then
    echo "✅ Automatic scheduling is configured"
    echo ""
    echo "📋 Schedule Details:"
    grep -A 10 "schedule:" "$WORKFLOW_FILE" | grep -E "(cron:|#)" | while read line; do
        if [[ $line == *"cron:"* ]]; then
            cron_expr=$(echo "$line" | sed "s/.*cron: '\(.*\)'.*/\1/")
            echo "   ⏰ $cron_expr"
        elif [[ $line == *"#"* ]]; then
            comment=$(echo "$line" | sed 's/.*# *//')
            echo "   💭 $comment"
        fi
    done
else
    echo "⚠️ No automatic schedule found"
fi

echo ""
echo "🔍 Schedule Analysis:"
echo "--------------------"
echo "✅ Runs on the 1st Monday of every month at 9:00 AM UTC"
echo "✅ Runs on the 3rd Monday of every month at 9:00 AM UTC"
echo "✅ Approximately every 2 weeks"
echo "✅ Manual triggering is also enabled"

# Calculate next run dates
echo ""
echo "📆 Next Scheduled Runs (approximate):"
echo "-------------------------------------"

# Get current date
current_year=$(date +%Y)
current_month=$(date +%m)

# Function to find the nth Monday of a month
find_nth_monday() {
    local year=$1
    local month=$2
    local nth=$3
    
    # First day of month
    first_day=$(date -d "$year-$month-01" +%u)  # 1=Monday, 7=Sunday
    
    # Days to add to get to first Monday
    if [ $first_day -eq 1 ]; then
        days_to_first_monday=0
    else
        days_to_first_monday=$((8 - first_day))
    fi
    
    # Calculate the nth Monday
    target_day=$((1 + days_to_first_monday + (nth - 1) * 7))
    
    # Check if this day exists in the month
    if date -d "$year-$month-$target_day" >/dev/null 2>&1; then
        date -d "$year-$month-$target_day" +"%Y-%m-%d (%A)"
    else
        echo "N/A"
    fi
}

# Show next few runs
for i in {0..3}; do
    month=$(date -d "+$i month" +%m)
    year=$(date -d "+$i month" +%Y)
    month_name=$(date -d "+$i month" +%B)
    
    first_monday=$(find_nth_monday $year $month 1)
    third_monday=$(find_nth_monday $year $month 3)
    
    if [ "$first_monday" != "N/A" ]; then
        echo "   📅 $month_name: $first_monday at 09:00 UTC"
    fi
    if [ "$third_monday" != "N/A" ]; then
        echo "   📅 $month_name: $third_monday at 09:00 UTC"
    fi
done

echo ""
echo "⚙️ System Status:"
echo "-----------------"

# Check GitHub CLI
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI (gh) is available"
    
    # Check if we're in a Git repository
    if git rev-parse --git-dir > /dev/null 2>&1; then
        echo "✅ Repository is a Git repository"
        
        # Check for GitHub remote
        if git remote get-url origin 2>/dev/null | grep -q github.com; then
            echo "✅ GitHub remote configured"
            
            # Try to check workflow status
            if gh workflow list &>/dev/null; then
                echo "✅ GitHub Actions are accessible"
                echo ""
                echo "📊 Recent Workflow Runs:"
                gh run list --workflow=discover-repositories.yml --limit=5 2>/dev/null || {
                    echo "   No workflow runs found (workflow may not have run yet)"
                }
            else
                echo "⚠️ Cannot access GitHub Actions (check permissions)"
            fi
        else
            echo "⚠️ No GitHub remote found"
        fi
    else
        echo "⚠️ Not in a Git repository"
    fi
else
    echo "ℹ️ GitHub CLI not installed (optional for manual management)"
fi

echo ""
echo "🚀 Manual Control:"
echo "------------------"
echo "To trigger automation manually:"
echo "  • Via GitHub web interface: Go to Actions → Discover New Batch Repositories → Run workflow"
echo "  • Via GitHub CLI: gh workflow run discover-repositories.yml"
echo "  • Via local script: cd z.repo_support/scripts && python3 automate_discovery.py"

echo ""
echo "🔧 Configuration Files:"
echo "----------------------"
echo "  • Workflow: .github/workflows/discover-repositories.yml"
echo "  • Scripts: z.repo_support/scripts/"
echo "  • Documentation: z.repo_support/scripts/AUTOMATION_GUIDE.md"

echo ""
echo "📝 To Modify Schedule:"
echo "---------------------"
echo "Edit .github/workflows/discover-repositories.yml and change the cron expressions:"
echo "  • '0 9 1-7 * 1'    = First Monday of each month at 9 AM UTC"
echo "  • '0 9 15-21 * 1'  = Third Monday of each month at 9 AM UTC"
echo ""
echo "Common schedules:"
echo "  • Weekly: '0 9 * * 1' (every Monday)"
echo "  • Daily: '0 9 * * *' (every day at 9 AM)"
echo "  • Monthly: '0 9 1 * *' (first day of each month)"

echo ""
echo "✅ Automation schedule check complete!"