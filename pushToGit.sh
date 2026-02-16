#!/bin/bash

git status

echo "Please write the commit message for the commit:"
read -r commit_message

if [ -z "$commit_message" ]; then
    echo "Commit message cannot be empty. Aborting."
    exit 1
fi

git add .
git status

git commit -m "$commit_message" || exit 1

echo "Do you want to push the changes to the remote repository? (y/n)"
read -r push_choice

case "$push_choice" in
    y|Y|yes|YES)
        current_branch=$(git branch --show-current)
        git push -u origin "$current_branch"
        ;;
    *)
        echo "Changes not pushed."
        ;;
esac
