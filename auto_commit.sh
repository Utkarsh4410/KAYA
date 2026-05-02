#!/bin/bash

# Configuration
PROJECT_DIR="/Users/subodh/KAYA"
LOG_FILE="$PROJECT_DIR/daily_log.txt"

# Navigate to project directory
cd "$PROJECT_DIR" || exit

# Append date to log file
echo "Automated daily commit: $(date)" >> "$LOG_FILE"

# Git operations
git add "$LOG_FILE"
git commit -m "chore: automated daily update $(date +'%Y-%m-%d %H:%M')"
git push origin main
