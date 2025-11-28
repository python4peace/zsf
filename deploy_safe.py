#!/usr/bin/env python3
import os
import subprocess
TOKEN = os.getenv("GITHUB_TOKEN")
if not TOKEN:
    print("❌ Set: export GITHUB_TOKEN='your_token'")
    exit(1)
REPO = "python4peace/zsf"

# Always add files (even if no changes)
subprocess.run(["git", "add", "."], check=True)

# Force commit even if no changes
try:
    subprocess.run(["git", "commit", "-m", "🕊️ Force Deploy ZSF Store"], check=True)
except subprocess.CalledProcessError:
    subprocess.run(["git", "commit", "--allow-empty", "-m", "🕊️ Force Deploy ZSF Store (empty)"], check=True)

# Force push
subprocess.run(["git", "push", f"https://{TOKEN}@github.com/{REPO}.git", "gh-pages", "--force"], check=True)
print("✅ DEPLOYED: https://python4peace.github.io/zsf/")
