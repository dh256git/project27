#!/bin/bash

# script to automate HTML proofing

## Go to project source directory
cd ~/Documents/self/informatics/projects/project27/src

## execute run Jekyll build with empty baseurl to generate testable _site output
jekyll build --baseurl=''

## pause for 2 seconds
sleep 2

## run htmlproofer on generated output
htmlproofer ./_site
