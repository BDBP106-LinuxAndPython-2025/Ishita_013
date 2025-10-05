#A script that takes a word and a filename, then prints the lines where the word appears.
#!/bin/bash
read -p "Enter the word: " word
read -p "Enter the filename: " file
grep "$word" "$file"



