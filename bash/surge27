#!/bin/bash

# script to semi-automate deployment of static test site files onto Surge.

## Go to project root directory
cd ~/Documents/archive/work/Project27/Project27\ Skills/

## execute version-counter python script to increment commit count
# python3 bash/version-counter.py # commenting out for surge deployment

## build site from source using config default baseurl
cd src/
JEKYLL_ENV=production jekyll build

## Pause for 3 seconds
sleep 3

## copy site files to surge directory
cp -r _site/* ../surge/

## initiate git push to staging branch
# git add _layouts/default.html # comment out as version counter is not incremented.
cd ../surge/
git add . # add all docs files to deployed content.
echo "Add commit message"
read commitMessage
git commit -m "$commitMessage"
git push origin staging
echo "Unstable release is ready to surge."

# # Initiate the surge deployment
surge