import os
import subprocess

def sync_to_github():
    # Paths
    ledger_path = os.path.expanduser('~/Documents/Ledgers/REDA_TO_LEX_SIGNAL.txt')
    repo_path = os.path.expanduser('~/Documents/the_swerv_note')
    
    # 1. Update the repo copy
    if os.path.exists(ledger_path):
        # Using StaSh git logic via subprocess
        try:
            # Stage, Commit, and Push
            os.chdir(repo_path)
            subprocess.run(['git', 'add', ledger_path])
            subprocess.run(['git', 'commit', '-m', '"Automatic Ledger Update"'])
            subprocess.run(['git', 'push', 'origin', 'main'])
            print("✅ Ledger synced to The Swerv Note.")
        except Exception as e:
            print(f"❌ Sync failed: {e}")

if __name__ == "__main__":
    sync_to_github()
