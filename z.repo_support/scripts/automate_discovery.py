#!/usr/bin/env python3
"""
Complete automation script for The Batch Compendium repository discovery and integration.
This script orchestrates the entire process from discovery to integration.
"""

import os
import sys
import json
import argparse
import subprocess
from typing import Dict, List, Optional
from datetime import datetime
from pathlib import Path


class BatchCompendiumAutomation:
    """Complete automation system for batch repository discovery and integration."""
    
    def __init__(self, base_path: str = "."):
        """
        Initialize the automation system.
        
        Args:
            base_path: Base path of the repository collection
        """
        self.base_path = Path(base_path)
        self.scripts_path = self.base_path / "z.repo_support" / "scripts"
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Ensure Python scripts are executable
        self._ensure_script_permissions()
        
    def _ensure_script_permissions(self):
        """Ensure Python scripts have execute permissions."""
        python_scripts = [
            'identify_batch_repos.py',
            'process_new_discoveries.py',
            'integrate_repositories.py',
            'generate_highly_rated_docs.py',
            'update_collection.py',
            'quality_filter.py',
            'notification_manager.py'
        ]
        
        for script in python_scripts:
            script_path = self.scripts_path / script
            if script_path.exists():
                os.chmod(script_path, 0o755)
    
    def run_discovery(self, min_stars: int = 50, max_results: int = 100, 
                     github_token: Optional[str] = None) -> Dict:
        """Run repository discovery process."""
        print(f"🔍 Starting repository discovery...")
        print(f"   Min stars: {min_stars}, Max results: {max_results}")
        
        try:
            # Prepare command
            cmd = [
                'python3',
                str(self.scripts_path / 'identify_batch_repos.py'),
                '--min-stars', str(min_stars),
                '--max-results', str(max_results),
                '--output', f'discovered_repos_{self.timestamp}.csv'
            ]
            
            if github_token:
                cmd.extend(['--token', github_token])
            
            # Run discovery
            result = subprocess.run(
                cmd,
                cwd=self.scripts_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            discovery_file = self.scripts_path / f'discovered_repos_{self.timestamp}.csv'
            
            if discovery_file.exists():
                # Count discovered repositories
                with open(discovery_file, 'r') as f:
                    line_count = sum(1 for line in f) - 1  # Subtract header
                
                print(f"✅ Discovery completed: {line_count} repositories found")
                return {
                    'success': True,
                    'file': str(discovery_file),
                    'count': line_count,
                    'output': result.stdout
                }
            else:
                return {
                    'success': False,
                    'error': 'Discovery file not created',
                    'output': result.stdout
                }
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Discovery failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'stderr': e.stderr
            }
    
    def run_processing(self, discovery_file: str, min_stars: int = 50) -> Dict:
        """Run repository processing and filtering."""
        print(f"🔄 Processing discovered repositories...")
        
        try:
            existing_file = self.scripts_path / 'repo_results.csv'
            filtered_file = self.scripts_path / f'filtered_new_repos_{self.timestamp}.csv'
            
            cmd = [
                'python3',
                str(self.scripts_path / 'process_new_discoveries.py'),
                '--new-repos', discovery_file,
                '--existing-repos', str(existing_file),
                '--output', str(filtered_file),
                '--min-stars', str(min_stars),
                '--report'
            ]
            
            result = subprocess.run(
                cmd,
                cwd=self.scripts_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            if filtered_file.exists():
                # Count filtered repositories
                with open(filtered_file, 'r') as f:
                    line_count = sum(1 for line in f) - 1  # Subtract header
                
                print(f"✅ Processing completed: {line_count} quality repositories")
                return {
                    'success': True,
                    'file': str(filtered_file),
                    'count': line_count,
                    'output': result.stdout
                }
            else:
                return {
                    'success': True,
                    'file': str(filtered_file),
                    'count': 0,
                    'output': result.stdout
                }
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Processing failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'stderr': e.stderr
            }
    
    def run_integration(self, filtered_file: str) -> Dict:
        """Run repository integration process."""
        print(f"🔧 Integrating repositories into collection...")
        
        try:
            cmd = [
                'python3',
                str(self.scripts_path / 'integrate_repositories.py'),
                '--new-repos', filtered_file,
                '--base-path', str(self.base_path),
                '--update-collection'
            ]
            
            result = subprocess.run(
                cmd,
                cwd=self.scripts_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            print(f"✅ Integration completed")
            return {
                'success': True,
                'output': result.stdout
            }
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Integration failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'stderr': e.stderr
            }
    
    def run_documentation_update(self, new_repos_count: int = 0) -> Dict:
        """Update documentation and statistics."""
        print(f"📝 Updating documentation and statistics...")
        
        try:
            # Update HIGHLY_RATED_REPOS.md
            cmd1 = [
                'python3',
                str(self.scripts_path / 'generate_highly_rated_docs.py'),
                '--input', str(self.scripts_path / 'repo_results.csv'),
                '--output', str(self.scripts_path / 'HIGHLY_RATED_REPOS.md')
            ]
            
            result1 = subprocess.run(
                cmd1,
                cwd=self.scripts_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            # Update collection statistics and main README
            cmd2 = [
                'python3',
                str(self.scripts_path / 'update_collection.py'),
                '--base-path', str(self.base_path),
                '--new-repos-count', str(new_repos_count)
            ]
            
            result2 = subprocess.run(
                cmd2,
                cwd=self.scripts_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            print(f"✅ Documentation updated")
            return {
                'success': True,
                'output': result1.stdout + "\n" + result2.stdout
            }
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Documentation update failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'stderr': e.stderr
            }
    
    def send_notification(self, notification_data: Dict, 
                         channels: List[str] = None) -> Dict:
        """Send notification about automation results."""
        print(f"📢 Sending notifications...")
        
        if channels is None:
            channels = ['console', 'file']
        
        try:
            # Save notification data to temporary file
            notification_file = self.scripts_path / f'notification_data_{self.timestamp}.json'
            with open(notification_file, 'w') as f:
                json.dump(notification_data, f, indent=2)
            
            cmd = [
                'python3',
                str(self.scripts_path / 'notification_manager.py'),
                '--type', notification_data.get('type', 'discovery'),
                '--data', str(notification_file),
                '--channels'
            ] + channels
            
            # Add file path for file notifications
            if 'file' in channels:
                cmd.extend(['--file-path', str(self.scripts_path / 'automation_notifications.log')])
            
            # Add GitHub options if available
            github_token = os.getenv('GITHUB_TOKEN')
            github_repo = os.getenv('GITHUB_REPOSITORY')
            
            if 'github_issue' in channels and github_token and github_repo:
                cmd.extend([
                    '--github-token', github_token,
                    '--github-repo', github_repo
                ])
            
            result = subprocess.run(
                cmd,
                cwd=self.scripts_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            # Clean up temporary file
            notification_file.unlink()
            
            print(f"✅ Notifications sent")
            return {
                'success': True,
                'output': result.stdout
            }
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Notification failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'stderr': e.stderr
            }
    
    def run_upstream_updates(self, github_token: Optional[str] = None, limit: Optional[int] = None) -> Dict:
        """Run upstream repository updates."""
        print(f"🔄 Updating existing repositories from upstream sources...")
        
        try:
            cmd = [
                'python3',
                str(self.scripts_path / 'update_upstream_repos.py'),
                '--base-path', str(self.base_path)
            ]
            
            if github_token:
                cmd.extend(['--github-token', github_token])
            
            if limit:
                cmd.extend(['--limit', str(limit)])
            
            result = subprocess.run(
                cmd,
                cwd=self.scripts_path,
                capture_output=True,
                text=True,
                timeout=3600  # 1 hour timeout for updates
            )
            
            # Check if there were any updates (ignore non-zero exit if only due to skips)
            if result.returncode == 0 or 'Successfully Updated' in result.stdout:
                print(f"✅ Upstream updates completed")
                return {
                    'success': True,
                    'output': result.stdout
                }
            else:
                print(f"⚠️ Upstream updates completed with warnings")
                return {
                    'success': True,
                    'output': result.stdout,
                    'warnings': result.stderr
                }
                
        except subprocess.TimeoutExpired:
            print(f"⚠️ Upstream updates timed out but continuing...")
            return {
                'success': False,
                'error': 'Update operation timed out',
                'timeout': True
            }
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Upstream updates failed but continuing...")
            return {
                'success': False,
                'error': str(e),
                'stderr': e.stderr
            }
    
    def run_complete_automation(self, 
                               min_stars: int = 50,
                               max_results: int = 100,
                               github_token: Optional[str] = None,
                               notification_channels: List[str] = None,
                               update_existing: bool = True,
                               update_limit: Optional[int] = None) -> Dict:
        """Run the complete automation process."""
        
        print(f"""
{'=' * 60}
🤖 Starting Complete Batch Compendium Automation
{'=' * 60}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
Min Stars: {min_stars}
Max Results: {max_results}
Update Existing: {update_existing}
{'=' * 60}
""")
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'success': False,
            'steps': {}
        }
        
        try:
            # Step 0: Update existing repositories (if requested)
            if update_existing:
                upstream_result = self.run_upstream_updates(github_token, update_limit)
                results['steps']['upstream_updates'] = upstream_result
                # Don't fail if upstream updates have issues, just log them
                if not upstream_result.get('success'):
                    print(f"⚠️ Some upstream updates failed, but continuing with discovery...")
            
            # Step 1: Repository Discovery
            discovery_result = self.run_discovery(min_stars, max_results, github_token)
            results['steps']['discovery'] = discovery_result
            
            if not discovery_result['success']:
                raise Exception(f"Discovery failed: {discovery_result.get('error')}")
            
            discovered_count = discovery_result['count']
            
            # Step 2: Processing and Filtering
            processing_result = self.run_processing(discovery_result['file'], min_stars)
            results['steps']['processing'] = processing_result
            
            if not processing_result['success']:
                raise Exception(f"Processing failed: {processing_result.get('error')}")
            
            filtered_count = processing_result['count']
            
            # Step 3: Integration (only if we have new repositories)
            if filtered_count > 0:
                integration_result = self.run_integration(processing_result['file'])
                results['steps']['integration'] = integration_result
                
                if not integration_result['success']:
                    raise Exception(f"Integration failed: {integration_result.get('error')}")
                
                # Step 4: Documentation Update
                docs_result = self.run_documentation_update(filtered_count)
                results['steps']['documentation'] = docs_result
                
                if not docs_result['success']:
                    print(f"⚠️ Documentation update failed but continuing...")
            else:
                print(f"ℹ️ No new repositories to integrate")
                results['steps']['integration'] = {'success': True, 'skipped': True}
                results['steps']['documentation'] = {'success': True, 'skipped': True}
            
            # Create notification data
            notification_data = {
                'type': 'discovery_complete',
                'timestamp': datetime.now().isoformat(),
                'summary': {
                    'total_discovered': discovered_count,
                    'new_repositories': filtered_count,
                    'quality_filtered': filtered_count,
                    'success_rate': (filtered_count / discovered_count * 100) if discovered_count > 0 else 0
                },
                'categories': {},
                'top_repositories': [],
                'status': 'success' if filtered_count > 0 else 'no_new_repos'
            }
            
            # Step 5: Send Notifications
            if notification_channels:
                notification_result = self.send_notification(notification_data, notification_channels)
                results['steps']['notification'] = notification_result
            
            results['success'] = True
            results['summary'] = {
                'upstream_updated': results['steps'].get('upstream_updates', {}).get('success', False),
                'discovered': discovered_count,
                'filtered': filtered_count,
                'integrated': filtered_count if filtered_count > 0 else 0
            }
            
            print(f"""
{'=' * 60}
✅ Automation Completed Successfully!
{'=' * 60}
📊 Summary:
  • Upstream Updates: {'✓ Completed' if update_existing else '⏭️ Skipped'}
  • Repositories Discovered: {discovered_count}
  • Quality Filtered: {filtered_count}
  • Successfully Integrated: {filtered_count if filtered_count > 0 else 0}
  • Success Rate: {(filtered_count / discovered_count * 100) if discovered_count > 0 else 0:.1f}%

🎯 Status: {'New repositories added!' if filtered_count > 0 else 'No new repositories found.'}
{'=' * 60}
""")
            
        except Exception as e:
            results['success'] = False
            results['error'] = str(e)
            
            print(f"""
{'=' * 60}
❌ Automation Failed
{'=' * 60}
Error: {e}
{'=' * 60}
""")
            
            # Send error notification
            if notification_channels:
                error_notification = {
                    'type': 'error',
                    'timestamp': datetime.now().isoformat(),
                    'error_type': 'automation_error',
                    'error_message': str(e),
                    'context': results,
                    'status': 'error'
                }
                
                self.send_notification(error_notification, notification_channels)
        
        return results
    
    def cleanup_temp_files(self):
        """Clean up temporary files created during automation."""
        print(f"🧹 Cleaning up temporary files...")
        
        patterns = [
            f'discovered_repos_{self.timestamp}.csv',
            f'filtered_new_repos_{self.timestamp}.csv',
            f'notification_data_{self.timestamp}.json'
        ]
        
        for pattern in patterns:
            file_path = self.scripts_path / pattern
            if file_path.exists():
                file_path.unlink()
                print(f"   Removed: {pattern}")


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Complete automation for The Batch Compendium"
    )
    parser.add_argument(
        '--min-stars',
        type=int,
        default=50,
        help='Minimum star count for repositories (default: 50)'
    )
    parser.add_argument(
        '--max-results',
        type=int,
        default=100,
        help='Maximum number of results per search (default: 100)'
    )
    parser.add_argument(
        '--github-token',
        help='GitHub API token (or set GITHUB_TOKEN env var)'
    )
    parser.add_argument(
        '--base-path',
        default='../..',
        help='Base path of the repository collection (default: ../..)'
    )
    parser.add_argument(
        '--notifications',
        nargs='+',
        choices=['console', 'file', 'webhook', 'github_issue'],
        default=['console', 'file'],
        help='Notification channels (default: console file)'
    )
    parser.add_argument(
        '--cleanup',
        action='store_true',
        help='Clean up temporary files after automation'
    )
    parser.add_argument(
        '--update-existing',
        action='store_true',
        default=True,
        help='Update existing repositories from upstream (default: True)'
    )
    parser.add_argument(
        '--no-update-existing',
        action='store_false',
        dest='update_existing',
        help='Skip updating existing repositories'
    )
    parser.add_argument(
        '--update-limit',
        type=int,
        help='Limit number of repositories to update from upstream (for testing)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    
    args = parser.parse_args()
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
        print(f"Would run automation with:")
        print(f"  Min stars: {args.min_stars}")
        print(f"  Max results: {args.max_results}")
        print(f"  Base path: {args.base_path}")
        print(f"  Update existing: {args.update_existing}")
        print(f"  Notifications: {args.notifications}")
        return
    
    # Get GitHub token
    github_token = args.github_token or os.getenv('GITHUB_TOKEN')
    if not github_token:
        print("⚠️ Warning: No GitHub token provided. API rate limits will be lower.")
    
    # Initialize automation
    automation = BatchCompendiumAutomation(base_path=args.base_path)
    
    try:
        # Run complete automation
        results = automation.run_complete_automation(
            min_stars=args.min_stars,
            max_results=args.max_results,
            github_token=github_token,
            notification_channels=args.notifications,
            update_existing=args.update_existing,
            update_limit=args.update_limit
        )
        
        # Save results
        results_file = automation.scripts_path / f'automation_results_{automation.timestamp}.json'
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"📄 Results saved to: {results_file}")
        
        # Cleanup if requested
        if args.cleanup:
            automation.cleanup_temp_files()
        
        # Exit with appropriate code
        sys.exit(0 if results['success'] else 1)
        
    except KeyboardInterrupt:
        print(f"\n⚠️ Automation interrupted by user")
        if args.cleanup:
            automation.cleanup_temp_files()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        if args.cleanup:
            automation.cleanup_temp_files()
        sys.exit(1)


if __name__ == "__main__":
    main()