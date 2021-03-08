import re # regular expression

## read text file content to string variable
path = "source.txt"
with open(path, 'r') as file:
    myFile = file.read()

## split text source into a list of items separated by newline, and loop through items looking for a string match. If match found, assign line to string variable.
for item in myFile.split("\n"):
	if "commit" in item:
		myLine = item.strip()

## search for two digit sequence in source string, group match sequence into a string.
commit = re.search(r'\d\d', myLine).group()

## increase commit number by 1
newCommit = str(int(commit) + 1)

## define original and replacement commit sub-strings
original = 'commit="' + commit + '"'
replacement = 'commit="' + newCommit + '"'

## replace old commit string with updated commit string
newText = myFile.replace(original, replacement)

## write updated text into file
with open(path, 'w') as file:
    file.write(newText)
    file.close()