# Automated Cleanup System for TheBatchCompendium

## Overview

This document describes the automated cleanup and maintenance system implemented for The Batch Compendium repository to handle draft PRs, stale issues, and workflow failures with minimal manual intervention.

## Components

### 1. PR Janitor Workflow (`.github/workflows/pr-janitor.yml`)

**Schedule:** Daily at 00:00 UTC

**Purpose:** Automatically manage draft pull requests to reduce clutter and notification noise.

**Features:**
- **Stale PR Detection:** Identifies PRs inactive for 30+ days
- **Auto-Merge:** Merges green Copilot PRs when all checks pass
- **Obsolete PR Cleanup:** Closes PRs inactive for 60+ days
- **Conflict Detection:** Labels PRs with merge conflicts

**Configuration:**
```yaml
Default Settings:
- Stale after: 30 days
- Close after: 7 additional days
- Exemptions: keep-open, in-progress, blocked labels
```

**Manual Trigger:**
```bash
gh workflow run pr-janitor.yml -f stale_days=15 -f close_days=5
```

### 2. Issue Janitor Workflow (`.github/workflows/issue-janitor.yml`)

**Schedule:** Daily at 01:00 UTC

**Purpose:** Keep the issue tracker clean by closing inactive issues.

**Features:**
- **Stale Issue Detection:** Marks issues inactive for 60+ days as stale
- **Auto-Close:** Closes stale issues after 14 additional days
- **Smart Exemptions:** Never closes security, pinned, or in-progress issues
- **Automatic Label Removal:** Removes stale label when issues are updated

**Configuration:**
```yaml
Default Settings:
- Stale after: 60 days
- Close after: 14 additional days  
- Exemptions: keep-open, in-progress, blocked, pinned, security labels
```

**Manual Trigger:**
```bash
gh workflow run issue-janitor.yml -f stale_days=30 -f close_days=7
```

### 3. Workflow Optimizations

**Discovery Workflow Updates:**
- Skip CI checks on draft PRs
- Only run on `ready_for_review` events
- Reduce GitHub Actions minutes usage
- Minimize notification emails

**PR Types Filter:**
```yaml
pull_request:
  types: [opened, synchronize, reopened, ready_for_review]
```

## Lifecycle Diagrams

### Draft PR Lifecycle

```
┌─────────────────┐
│  Draft PR       │
│  Created        │
└────────┬────────┘
         │
         ▼
    ┌────────────────┐
    │ Checks Pass?   │
    │ Mergeable?     │
    └───┬────────┬───┘
        │        │
     Yes│        │No
        │        │
        ▼        ▼
  ┌─────────┐  ┌──────────────┐
  │Auto-    │  │ Wait for     │
  │Merge    │  │ Activity     │
  └─────────┘  └──────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ 30 Days Pass? │
              └───┬───────┬───┘
                  │       │
               Yes│       │No
                  │       │
                  ▼       └──┐
          ┌──────────┐      │
          │ Label    │      │
          │ "stale"  │      │
          └────┬─────┘      │
               │            │
               ▼            │
       ┌──────────────┐    │
       │ 7 More Days? │    │
       └───┬──────────┘    │
           │               │
        Yes│               │
           │               │
           ▼               │
    ┌──────────┐          │
    │ Close PR │◄─────────┘
    └──────────┘
```

### Issue Lifecycle

```
┌─────────────────┐
│  Issue          │
│  Created        │
└────────┬────────┘
         │
         ▼
    ┌────────────────┐
    │ 60 Days Pass?  │
    │ No Activity?   │
    └───┬────────┬───┘
        │        │
     Yes│        │No
        │        │
        ▼        └──────┐
  ┌─────────┐          │
  │ Label   │          │
  │ "stale" │          │
  └────┬────┘          │
       │               │
       ▼               │
┌──────────────┐       │
│ 14 More Days?│       │
│ No Update?   │       │
└───┬──────────┘       │
    │                  │
 Yes│                  │
    │                  │
    ▼                  │
┌────────────┐         │
│ Close Issue│◄────────┘
└────────────┘
```

## Benefits

### For Maintainers
- **Reduced Manual Work:** No need to manually close stale PRs/issues
- **Less Notification Noise:** Draft PRs don't trigger CI checks
- **Cleaner Repository:** Old, abandoned work is automatically archived
- **Lower Costs:** Reduced GitHub Actions minutes usage

### For Contributors
- **Clear Status:** Stale items are clearly labeled before closure
- **Fair Warning:** 7-14 day grace period before automatic closure
- **Easy Override:** Simple labels prevent automatic closure
- **Auto-Merge:** Good work gets merged automatically

## Configuration Options

### Exemption Labels

**For PRs:**
- `keep-open` - Never mark as stale
- `in-progress` - Active work in progress
- `blocked` - Waiting on external dependency

**For Issues:**
- `keep-open` - Never mark as stale
- `in-progress` - Active work in progress
- `blocked` - Waiting on external dependency
- `pinned` - Important issue to keep visible
- `security` - Security-related issues

### Customizing Thresholds

Edit the workflow files to change default values:

**PR Janitor (`.github/workflows/pr-janitor.yml`):**
```yaml
days-before-stale: '30'   # Change to desired value
days-before-close: '7'     # Change to desired value
```

**Issue Janitor (`.github/workflows/issue-janitor.yml`):**
```yaml
days-before-stale: '60'    # Change to desired value
days-before-close: '14'    # Change to desired value
```

## Monitoring

### Check Workflow Runs
```bash
# View recent PR janitor runs
gh run list --workflow=pr-janitor.yml --limit 10

# View recent issue janitor runs
gh run list --workflow=issue-janitor.yml --limit 10
```

### View Logs
```bash
# View logs for specific run
gh run view <run-id> --log

# View logs for latest run
gh run view --workflow=pr-janitor.yml --log
```

## Troubleshooting

### PRs Not Being Auto-Merged

**Check:**
1. Are all CI checks passing?
2. Is the PR mergeable (no conflicts)?
3. Is the PR from a bot account (Copilot)?
4. Does the PR have exemption labels?

**Solution:**
- Review PR checks and status
- Resolve any merge conflicts
- Verify PR author is recognized as bot

### Issues Not Being Closed

**Check:**
1. Has the issue been inactive for 60+ days?
2. Has the stale period (14 days) passed?
3. Does the issue have exemption labels?

**Solution:**
- Check issue labels
- Verify last activity date
- Remove exemption labels if no longer needed

### Workflows Not Running

**Check:**
1. Are workflows enabled for the repository?
2. Is the schedule correct (check timezone)?
3. Are there any workflow errors?

**Solution:**
```bash
# Check workflow status
gh workflow list

# Enable workflow if disabled
gh workflow enable pr-janitor.yml
gh workflow enable issue-janitor.yml

# Manually trigger workflow
gh workflow run pr-janitor.yml
```

## Security Considerations

1. **Permissions:** Workflows use `GITHUB_TOKEN` with minimal required permissions
2. **Bot Detection:** Multiple checks ensure only bot-created PRs are auto-managed
3. **Exemptions:** Security-labeled issues are never auto-closed
4. **Audit Trail:** All actions are logged and reversible

## Future Enhancements

Potential improvements for future iterations:

1. **Rebase Support:** Automatically rebase PRs before attempting merge
2. **Conflict Resolution:** Attempt basic conflict resolution strategies
3. **Priority Labeling:** Smart labeling based on PR content and impact
4. **Notifications:** Slack/Discord notifications for important actions
5. **Analytics:** Dashboard showing cleanup statistics over time

## Support

For questions or issues with the automation system:
1. Check this document first
2. Review workflow run logs
3. Check existing issues/PRs for similar problems
4. Open a new issue with label `automation`

---

**Last Updated:** December 20, 2025  
**Version:** 1.0.0  
**Maintainer:** @GhostwheeI
