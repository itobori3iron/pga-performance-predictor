import os
import datetime

# Customize these
commit_message = f"Auto-commit on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
branch_name = "main"  # or "master" depending on your repo

# Git commands
os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system(f"git push origin {branch_name}")
