#!/bin/bash

# script to automate git add, commit, and push
echo "Add commit message"
read commitMessage
git add .
git commit -m "$commitMessage"
echo "git push origin master"
echo "Deployment initiated. Confirm status."