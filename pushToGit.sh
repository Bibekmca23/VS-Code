#!/bin/sh
git status
echo "Please write the commit message for the commit: "
read commit_message
git add .
git status
git commit -m "$commit_message"
git status
echo "Do you want to push the changes to the remote repository? (y/n)"
read push_choice
if [ "$push_choice" = "y" ]; then
git push -u origin main
