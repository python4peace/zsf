#!/usr/bin/env python3
import os
import subprocess
TOKEN = os.getenv("GITHUB_TOKEN")
if not TOKEN:
    print("❌ Set: export GITHUB_TOKEN='your_token'")
    exit(1)
REPO = "python4peace/zsf"
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "🕊️ Deploy ZSF Store"], check=True)
subprocess.run(["git", "push", f"https://{TOKEN}@github.com/{REPO}.git", "gh-pages", "--force"], check=True)
print("✅ DEPLOYED: https://python4peace.github.io/zsf/")
