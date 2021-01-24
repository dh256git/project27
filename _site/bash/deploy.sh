#!/bin/bash

# script to automate git add, commit, and push
cd ~/Documents/self/informatics/projects/project27/src/
echo "Add commit message"
read commitMessage
git add .
git commit -m "$commitMessage"
git push origin master
echo "Deployment initiated. Confirm status."