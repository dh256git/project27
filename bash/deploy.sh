#!/bin/bash

# script to automate deployment of static site files

## Go to project root directory
cd ~/Documents/archive/work/Project27/Project27\ Skills/

## execute version-counter python script to increment commit count
python3 bash/version-counter.py

## build site from source using config default baseurl
cd src/
JEKYLL_ENV=production jekyll build

## Pause for 3 seconds
sleep 3

## copy site files to deployed docs
cp -r _site/* ../docs/

## initiate git deployment to master
git add _layouts/default.html # add default.html from source to the commit of deployment, so after deployment a clean local repository is the output, given all other changes of source have been committed before.
cd ../docs/
git add . # add all docs files to deployed content.
echo "Add commit message"
read commitMessage
git commit -m "$commitMessage"
git push origin master
echo "Deployment initiated. Confirm status."