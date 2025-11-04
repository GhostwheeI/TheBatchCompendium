#!/usr/bin/env python3
"""
Notification system for repository discovery and integration results.
Supports multiple notification channels and formats.
"""

import os
import json
import argparse
import requests
from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path


class NotificationManager:
    """Manage notifications for repository discovery system."""
    
    def __init__(self):
        """Initialize the notification manager."""
        self.supported_channels = ['console', 'file', 'webhook', 'github_issue']
        
    def create_discovery_notification(self, 
                                    total_discovered: int,
                                    new_repos: int,
                                    quality_filtered: int,
                                    categories: Dict[str, int],
                                    top_repos: List[Dict]) -> Dict:
        """Create a notification for discovery results."""
        
        notification = {
            'type': 'discovery_complete',
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_discovered': total_discovered,
                'new_repositories': new_repos,
                'quality_filtered': quality_filtered,
                'success_rate': (quality_filtered / total_discovered * 100) if total_discovered > 0 else 0
            },
            'categories': categories,
            'top_repositories': top_repos[:5],  # Top 5 only for notifications
            'status': 'success' if new_repos > 0 else 'no_new_repos'
        }
        
        return notification
    
    def create_integration_notification(self,
                                      integrated_count: int,
                                      failed_count: int,
                                      created_paths: List[str],
                                      errors: List[str] = None) -> Dict:
        """Create a notification for integration results."""
        
        notification = {
            'type': 'integration_complete',
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'integrated_repositories': integrated_count,
                'failed_integrations': failed_count,
                'success_rate': (integrated_count / (integrated_count + failed_count) * 100) if (integrated_count + failed_count) > 0 else 0
            },
            'created_structures': len(created_paths),
            'errors': errors or [],
            'status': 'success' if integrated_count > 0 and failed_count == 0 else 'partial_success' if integrated_count > 0 else 'failed'
        }
        
        return notification
    
    def create_error_notification(self, error_type: str, error_message: str, context: Dict = None) -> Dict:
        """Create a notification for errors."""
        
        notification = {
            'type': 'error',
            'timestamp': datetime.now().isoformat(),
            'error_type': error_type,
            'error_message': error_message,
            'context': context or {},
            'status': 'error'
        }
        
        return notification
    
    def format_console_message(self, notification: Dict) -> str:
        """Format notification for console output."""
        
        timestamp = datetime.fromisoformat(notification['timestamp'].replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M:%S')
        
        if notification['type'] == 'discovery_complete':
            summary = notification['summary']
            
            message = f"""
🤖 Repository Discovery Complete - {timestamp}
{'=' * 60}

📊 Summary:
  • Total Discovered: {summary['total_discovered']}
  • New Repositories: {summary['new_repositories']}
  • Quality Filtered: {summary['quality_filtered']}
  • Success Rate: {summary['success_rate']:.1f}%

📂 Categories:"""
            
            for category, count in notification.get('categories', {}).items():
                message += f"\n  • {category}: {count}"
            
            if notification.get('top_repositories'):
                message += f"\n\n⭐ Top New Repositories:"
                for i, repo in enumerate(notification['top_repositories'], 1):
                    name = repo.get('name', 'Unknown')
                    stars = repo.get('stars', 0)
                    message += f"\n  {i}. {name} ({stars:,} ⭐)"
            
            status_emoji = "✅" if notification['status'] == 'success' else "ℹ️"
            message += f"\n\n{status_emoji} Status: {notification['status'].replace('_', ' ').title()}"
            
        elif notification['type'] == 'integration_complete':
            summary = notification['summary']
            
            message = f"""
🔧 Repository Integration Complete - {timestamp}
{'=' * 60}

📊 Summary:
  • Integrated: {summary['integrated_repositories']}
  • Failed: {summary['failed_integrations']}
  • Success Rate: {summary['success_rate']:.1f}%
  • Structures Created: {notification['created_structures']}"""
            
            if notification.get('errors'):
                message += f"\n\n⚠️ Errors ({len(notification['errors'])}):"
                for error in notification['errors'][:3]:  # Show max 3 errors
                    message += f"\n  • {error}"
                if len(notification['errors']) > 3:
                    message += f"\n  • ... and {len(notification['errors']) - 3} more"
            
            status_emoji = "✅" if notification['status'] == 'success' else "⚠️" if notification['status'] == 'partial_success' else "❌"
            message += f"\n\n{status_emoji} Status: {notification['status'].replace('_', ' ').title()}"
            
        elif notification['type'] == 'error':
            message = f"""
❌ Error Notification - {timestamp}
{'=' * 60}

Error Type: {notification['error_type']}
Message: {notification['error_message']}"""
            
            if notification.get('context'):
                message += f"\nContext: {json.dumps(notification['context'], indent=2)}"
        
        else:
            message = f"\n📢 Notification - {timestamp}\n{json.dumps(notification, indent=2)}"
        
        return message
    
    def format_markdown_message(self, notification: Dict) -> str:
        """Format notification as Markdown."""
        
        timestamp = datetime.fromisoformat(notification['timestamp'].replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M:%S UTC')
        
        if notification['type'] == 'discovery_complete':
            summary = notification['summary']
            
            status_emoji = "✅" if notification['status'] == 'success' else "ℹ️"
            
            message = f"""## {status_emoji} Repository Discovery Complete

**Timestamp:** {timestamp}

### 📊 Summary
- **Total Discovered:** {summary['total_discovered']}
- **New Repositories:** {summary['new_repositories']}
- **Quality Filtered:** {summary['quality_filtered']}
- **Success Rate:** {summary['success_rate']:.1f}%

### 📂 Categories"""
            
            for category, count in notification.get('categories', {}).items():
                message += f"\n- **{category}:** {count}"
            
            if notification.get('top_repositories'):
                message += f"\n\n### ⭐ Top New Repositories"
                for i, repo in enumerate(notification['top_repositories'], 1):
                    name = repo.get('name', 'Unknown')
                    url = repo.get('url', '')
                    stars = repo.get('stars', 0)
                    description = repo.get('description', 'No description')[:80]
                    
                    if url:
                        message += f"\n{i}. **[{name}]({url})** ({stars:,} ⭐)"
                    else:
                        message += f"\n{i}. **{name}** ({stars:,} ⭐)"
                    message += f"\n   {description}..."
            
        elif notification['type'] == 'integration_complete':
            summary = notification['summary']
            
            status_emoji = "✅" if notification['status'] == 'success' else "⚠️" if notification['status'] == 'partial_success' else "❌"
            
            message = f"""## {status_emoji} Repository Integration Complete

**Timestamp:** {timestamp}

### 📊 Summary
- **Integrated:** {summary['integrated_repositories']}
- **Failed:** {summary['failed_integrations']}
- **Success Rate:** {summary['success_rate']:.1f}%
- **Structures Created:** {notification['created_structures']}"""
            
            if notification.get('errors'):
                message += f"\n\n### ⚠️ Errors"
                for error in notification['errors'][:5]:  # Show max 5 errors
                    message += f"\n- {error}"
        
        elif notification['type'] == 'error':
            message = f"""## ❌ Error Notification

**Timestamp:** {timestamp}
**Type:** {notification['error_type']}

### Error Details
```
{notification['error_message']}
```"""
            
            if notification.get('context'):
                message += f"\n\n### Context\n```json\n{json.dumps(notification['context'], indent=2)}\n```"
        
        return message
    
    def send_console_notification(self, notification: Dict):
        """Send notification to console."""
        message = self.format_console_message(notification)
        print(message)
    
    def send_file_notification(self, notification: Dict, file_path: str):
        """Send notification to file."""
        try:
            message = self.format_console_message(notification)
            
            # Ensure directory exists
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            
            # Append to file with timestamp
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(message + "\n\n")
                
            print(f"Notification saved to: {file_path}")
            
        except Exception as e:
            print(f"Error saving notification to file: {e}")
    
    def send_webhook_notification(self, notification: Dict, webhook_url: str):
        """Send notification via webhook."""
        try:
            # Format as a simple webhook payload
            payload = {
                'text': self.format_markdown_message(notification),
                'notification': notification
            }
            
            response = requests.post(
                webhook_url,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            
            if response.status_code == 200:
                print(f"Webhook notification sent successfully")
            else:
                print(f"Webhook notification failed: {response.status_code}")
                
        except Exception as e:
            print(f"Error sending webhook notification: {e}")
    
    def send_github_issue_notification(self, notification: Dict, 
                                     repo: str, token: str, 
                                     label: str = "automation"):
        """Send notification as GitHub issue."""
        try:
            # Only create issues for significant events
            if notification['type'] not in ['discovery_complete', 'error']:
                return
            
            title_prefix = "🤖 Automated Discovery" if notification['type'] == 'discovery_complete' else "❌ Error"
            title = f"{title_prefix} - {datetime.now().strftime('%Y-%m-%d')}"
            
            body = self.format_markdown_message(notification)
            
            # Add automation footer
            body += f"""

---
*This issue was automatically created by the Repository Discovery system.*
*Timestamp: {notification['timestamp']}*
"""
            
            # Create issue via GitHub API
            url = f"https://api.github.com/repos/{repo}/issues"
            headers = {
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            }
            
            payload = {
                'title': title,
                'body': body,
                'labels': [label]
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            
            if response.status_code == 201:
                issue_data = response.json()
                print(f"GitHub issue created: {issue_data['html_url']}")
            else:
                print(f"Failed to create GitHub issue: {response.status_code}")
                
        except Exception as e:
            print(f"Error creating GitHub issue: {e}")
    
    def send_notification(self, notification: Dict, channels: List[str], **kwargs):
        """Send notification through specified channels."""
        
        for channel in channels:
            if channel == 'console':
                self.send_console_notification(notification)
                
            elif channel == 'file':
                file_path = kwargs.get('file_path', 'notifications.log')
                self.send_file_notification(notification, file_path)
                
            elif channel == 'webhook':
                webhook_url = kwargs.get('webhook_url', os.getenv('WEBHOOK_URL'))
                if webhook_url:
                    self.send_webhook_notification(notification, webhook_url)
                else:
                    print("Warning: No webhook URL provided")
                    
            elif channel == 'github_issue':
                repo = kwargs.get('github_repo', os.getenv('GITHUB_REPOSITORY'))
                token = kwargs.get('github_token', os.getenv('GITHUB_TOKEN'))
                
                if repo and token:
                    self.send_github_issue_notification(
                        notification, repo, token, 
                        kwargs.get('github_label', 'automation')
                    )
                else:
                    print("Warning: GitHub repo or token not provided")
                    
            else:
                print(f"Warning: Unknown notification channel: {channel}")


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Send notifications for repository discovery system"
    )
    parser.add_argument(
        '--type',
        choices=['discovery', 'integration', 'error'],
        required=True,
        help='Type of notification'
    )
    parser.add_argument(
        '--channels',
        nargs='+',
        choices=['console', 'file', 'webhook', 'github_issue'],
        default=['console'],
        help='Notification channels'
    )
    parser.add_argument(
        '--data',
        help='JSON file with notification data'
    )
    parser.add_argument(
        '--file-path',
        default='notifications.log',
        help='File path for file notifications'
    )
    parser.add_argument(
        '--webhook-url',
        help='Webhook URL (or set WEBHOOK_URL env var)'
    )
    parser.add_argument(
        '--github-repo',
        help='GitHub repository (owner/repo format)'
    )
    parser.add_argument(
        '--github-token',
        help='GitHub token (or set GITHUB_TOKEN env var)'
    )
    
    # Quick notification options
    parser.add_argument(
        '--discovered',
        type=int,
        help='Number of repositories discovered'
    )
    parser.add_argument(
        '--new-repos',
        type=int,
        help='Number of new repositories'
    )
    parser.add_argument(
        '--error-msg',
        help='Error message for error notifications'
    )
    
    args = parser.parse_args()
    
    manager = NotificationManager()
    
    # Create notification based on type and data
    if args.data:
        # Load notification from JSON file
        try:
            with open(args.data, 'r', encoding='utf-8') as f:
                notification = json.load(f)
        except Exception as e:
            print(f"Error loading notification data: {e}")
            return
    else:
        # Create notification from command line args
        if args.type == 'discovery':
            if args.discovered is None or args.new_repos is None:
                print("Error: --discovered and --new-repos required for discovery notifications")
                return
            
            notification = manager.create_discovery_notification(
                total_discovered=args.discovered,
                new_repos=args.new_repos,
                quality_filtered=args.new_repos,  # Simplified
                categories={},
                top_repos=[]
            )
            
        elif args.type == 'error':
            if not args.error_msg:
                print("Error: --error-msg required for error notifications")
                return
            
            notification = manager.create_error_notification(
                error_type='automation_error',
                error_message=args.error_msg
            )
            
        else:
            print(f"Error: Notification type '{args.type}' requires --data file")
            return
    
    # Send notification
    manager.send_notification(
        notification,
        args.channels,
        file_path=args.file_path,
        webhook_url=args.webhook_url,
        github_repo=args.github_repo,
        github_token=args.github_token
    )


if __name__ == "__main__":
    main()