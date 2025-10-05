#!/bin/bash
#script that counts the number of words, lines and characters in a given text file.

file="examplefile"
if [ -e "$file" ]; then
	w=$(wc -w < "$file") 
	echo "words $w"
	l=$(wc -l < "$file")
	echo "lines= $l"
	c=$(wc -m < "$file")
	echo "char= $c"
else
	echo "FIle does not exist"
fi

