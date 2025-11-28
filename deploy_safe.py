#!/usr/bin/env python3
import os
import subprocess

# Get token from environment only
TOKEN = os.getenv("GITHUB_TOKEN")
if not TOKEN:
    print("❌ Set your token: export GITHUB_TOKEN='your_token_here'")
    exit(1)

REPO = "python4peace/zsf"

# Always add files
subprocess.run(["git", "add", "."], check=True)

# Commit with empty allowed (for deployment triggers)
try:
    subprocess.run(["git", "commit", "-m", "🕊️ Deploy ZSF Store"], check=True)
except:
    subprocess.run(["git", "commit", "--allow-empty", "-m", "🕊️ Deploy ZSF Store"], check=True)

# Push using the URL method (token in URL, not commit)
push_url = f"https://{TOKEN}@github.com/{REPO}.git"
result = subprocess.run(["git", "push", push_url, "gh-pages", "--force"], 
                       capture_output=True, text=True)

if result.returncode == 0:
    print("✅ DEPLOYED: https://python4peace.github.io/zsf/")
else:
    print("❌ Push failed:", result.stderr)
