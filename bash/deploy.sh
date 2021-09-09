#!/bin/bash

# script to automate git add, commit, and push

## Go to project source directory
cd ~/Documents/self/informatics/projects/project27/src/

## execute version-counter python script to increment commit count
python3 ../bash/version-counter.py

## build site from source using config default baseurl
jekyll build

## Pause for 3 seconds
sleep 3

## copy site files to deployed docs
cp -r _site/* ../docs/

## initiate git deployment to master
cd ../docs/
echo "Add commit message"
read commitMessage
git add .
git commit -m "$commitMessage"
git push origin master
echo "Deployment initiated. Confirm status."
