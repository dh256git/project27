# Commit counter

This python script increments the commit count by 1.

1. Read text from file.
2. Search for line of interest i.e. containing string "commit".
3. Search for two digit commit number, and group to string.
4. Increment commit number.
5. Define original commit substring and replacement commit substring in the line of interest.
6. Perform replacement in text.
7. Write text into file.