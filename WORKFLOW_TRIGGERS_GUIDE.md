# GitHub Actions Workflow Triggers Guide

This guide explains all the different ways your repository discovery workflow can be triggered.

## 🎯 Currently Configured Triggers

Your workflow now supports **5 different trigger types**:

### 1. ⏰ **Scheduled Runs** (`schedule`)
```yaml
schedule:
  - cron: '0 9 1-7 * 1'     # First Monday of each month
  - cron: '0 9 15-21 * 1'   # Third Monday of each month
```
- **When**: Automatically every ~2 weeks on Mondays at 9:00 AM UTC
- **Purpose**: Regular maintenance and discovery
- **Next runs**: November 17, December 1, December 15, etc.

### 2. 🖱️ **Manual Trigger** (`workflow_dispatch`)
```yaml
workflow_dispatch:
  inputs:
    min_stars: 50
    max_results: 100
```
- **When**: Click "Run workflow" button on GitHub
- **Purpose**: On-demand execution with custom parameters
- **How to use**:
  - Go to GitHub.com → Actions → "Discover New Batch Repositories"
  - Click "Run workflow" button
  - Optionally adjust min_stars and max_results

### 3. 📝 **Code Changes** (`push`)
```yaml
push:
  branches: [ main ]
  paths:
    - 'z.repo_support/scripts/**'
    - '.github/workflows/discover-repositories.yml'
```
- **When**: You push changes to automation scripts or workflow file
- **Purpose**: Test changes and ensure system works after updates
- **Triggers on**: Changes to any file in `z.repo_support/scripts/` or the workflow file

### 4. 🔍 **Pull Requests** (`pull_request`)
```yaml
pull_request:
  branches: [ main ]
  paths:
    - 'z.repo_support/scripts/**'
    - '.github/workflows/discover-repositories.yml'
```
- **When**: Someone creates a PR modifying automation files
- **Purpose**: Test automation changes before merging
- **Runs**: As a check on the PR (doesn't create new PRs)

### 5. 🔌 **API Trigger** (`repository_dispatch`)
```yaml
repository_dispatch:
  types: [discover-repositories]
```
- **When**: Triggered via GitHub API or other workflows
- **Purpose**: Integration with other systems or workflows
- **How to use**: See API section below

## 🛠️ Additional Trigger Options Available

Here are other triggers you could add if needed:

### 📅 **Issue Events** (`issues`)
```yaml
on:
  issues:
    types: [opened, labeled]
```
- Trigger when issues are created or labeled
- Example: Run discovery when someone creates an issue with "request-repos" label

### ⭐ **Star Events** (`watch`)
```yaml
on:
  watch:
    types: [started]
```
- Trigger when someone stars your repository
- Could run discovery when repo gains popularity

### 🍴 **Fork Events** (`fork`)
```yaml
on:
  fork:
```
- Trigger when someone forks your repository
- Could update statistics when community grows

### 📋 **Project Board Events** (`project`)
```yaml
on:
  project:
    types: [created, updated]
```
- Trigger when project boards are modified
- Could integrate with project management

### 🏷️ **Release Events** (`release`)
```yaml
on:
  release:
    types: [published]
```
- Trigger when you publish releases
- Could run discovery for special releases

## 🎮 How to Use Each Trigger

### 1. **Automatic Schedule** (No action needed)
- Runs automatically every ~2 weeks
- Check with: `./check_automation_schedule.sh`

### 2. **Manual Web Interface**
```
1. Go to GitHub.com → Your Repository
2. Click "Actions" tab
3. Click "Discover New Batch Repositories"  
4. Click "Run workflow" button
5. Optionally adjust parameters
6. Click "Run workflow"
```

### 3. **Manual via GitHub CLI**
```bash
# Basic run
gh workflow run discover-repositories.yml

# With custom parameters
gh workflow run discover-repositories.yml \
  -f min_stars=100 \
  -f max_results=50
```

### 4. **Trigger via API**
```bash
# Using curl
curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/repos/GhostwheeI/TheBatchCompendium/dispatches \
  -d '{"event_type":"discover-repositories"}'

# Using GitHub CLI
gh api repos/GhostwheeI/TheBatchCompendium/dispatches \
  -f event_type=discover-repositories
```

### 5. **Trigger from Another Workflow**
```yaml
# In another workflow file
- name: Trigger Repository Discovery
  run: |
    gh workflow run discover-repositories.yml
```

### 6. **Push Trigger** (Automatic)
```bash
# Any changes to automation files will trigger the workflow
cd z.repo_support/scripts
echo "# Updated" >> README.md
git add . && git commit -m "Update automation" && git push
```

## 🚨 **Smart Trigger Configuration**

### Conditional Execution
You can make the workflow smarter by adding conditions:

```yaml
jobs:
  discover-repositories:
    runs-on: ubuntu-latest
    # Only run on schedule or manual trigger, not on pushes to avoid loops
    if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'
```

### Environment-Based Triggers
```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
    
jobs:
  test:
    if: github.event_name == 'pull_request'
    # Only test on PRs
    
  deploy:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    # Only run discovery on main branch pushes
```

## 📊 **Monitoring Triggers**

### View Recent Triggers
```bash
# See recent workflow runs and their triggers
gh run list --workflow=discover-repositories.yml

# Get details about a specific run
gh run view RUN_ID
```

### Check Trigger History
```bash
# View workflow runs with trigger information
gh api repos/GhostwheeI/TheBatchCompendium/actions/workflows/discover-repositories.yml/runs \
  --jq '.workflow_runs[] | {id: .id, event: .event, status: .status, created_at: .created_at}'
```

## 🎛️ **Trigger Management Commands**

### Enable/Disable Workflow
```bash
# Disable workflow (stops all triggers)
gh workflow disable discover-repositories.yml

# Enable workflow
gh workflow enable discover-repositories.yml
```

### List All Triggers
```bash
# View current workflow configuration
gh workflow view discover-repositories.yml
```

## ⚡ **Quick Reference**

| Trigger Type | When It Runs | Use Case |
|--------------|--------------|----------|
| `schedule` | Every 2 weeks automatically | Regular maintenance |
| `workflow_dispatch` | Manual button click | On-demand execution |
| `push` | Code changes to automation files | Test after updates |
| `pull_request` | PRs with automation changes | Validate changes |
| `repository_dispatch` | API/external trigger | Integration |

## 🔧 **Customization Examples**

### Daily Discovery
```yaml
schedule:
  - cron: '0 9 * * *'  # Every day at 9 AM UTC
```

### Weekly Discovery
```yaml
schedule:
  - cron: '0 9 * * 1'  # Every Monday at 9 AM UTC
```

### Multiple Time Zones
```yaml
schedule:
  - cron: '0 9 * * 1'   # 9 AM UTC (Monday)
  - cron: '0 17 * * 1'  # 5 PM UTC (Monday)
```

### Issue-Triggered Discovery
```yaml
on:
  issues:
    types: [opened]
  schedule:
    - cron: '0 9 1-7,15-21 * 1'
  workflow_dispatch:

jobs:
  discover-repositories:
    if: |
      (github.event_name == 'issues' && contains(github.event.issue.labels.*.name, 'discover-repos')) ||
      github.event_name == 'schedule' ||
      github.event_name == 'workflow_dispatch'
```

Your workflow is now set up with multiple trigger options for maximum flexibility! 🚀