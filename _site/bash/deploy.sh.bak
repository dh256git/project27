#!/bin/bash

# script to automate git add, commit, and push

## Go to project directory
cd ~/Documents/self/informatics/projects/project27/src/

## execute version-counter python script to increment commit count
python3 bash/version-counter.py

## initiate git process
echo "Add commit message"
read commitMessage
git add .
git commit -m "$commitMessage"
git push origin master
echo "Deployment initiated. Confirm status."