#!/bin/bash
# Auto-commit and push wiki changes to GitHub
# Runs every hour via cron

cd /home/go/wiki

# Check if there are changes
if [ -n "$(git status --porcelain)" ]; then
    git add -A
    git commit -m "auto-update: $(date '+%Y-%m-%d %H:%M')" --quiet
    git push origin main --quiet 2>/dev/null
    echo "Wiki pushed: $(date '+%Y-%m-%d %H:%M')"
else
    echo "No wiki changes: $(date '+%Y-%m-%d %H:%M')"
fi
