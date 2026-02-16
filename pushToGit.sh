#!/bin/sh

# Show current status
git status

echo "Please write the commit message for the commit:"
read commit_message

# Check for empty commit message
if [ -z "$commit_message" ]; then
    echo "Commit message cannot be empty. Aborting."
    exit 1
fi

# Stage changes
git add .

echo "Staged changes:"
git status

# Commit changes
git commit -m "$commit_message"

# Check if commit was successful
if [ $? -ne 0 ]; then
    echo "Commit failed. Aborting."
    exit 1
fi

# Ask to push
echo "Do you want to push the changes to the remote repository? (y/n)"
read push_choice

case "$push_choice" in
    y|Y|yes|YES)
        # Get current branch dynamically
        current_branch=$(git branch --show-current)
        git push -u origin "$current_branch"
        ;;
    *)
        echo "Changes not pushed."
        ;;
esac
