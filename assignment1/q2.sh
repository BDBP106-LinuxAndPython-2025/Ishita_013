#!/bin/bash
#Ask the user for a filename, and check if it exists. If it exists, is the file readable and writable.

echo "Input a filename"
read n
echo "The file name entered is: "$n
if [ -e  "$n" ]; then
	if [ -r "$n" ]; then
		echo "The file is readable"
	else
		echo "The file is not readable"
	fi
	if [ -w "$n" ]; then
		echo "The file is writable"
	else
		echo "The file is not writable"
	fi
else
	echo "The file does not exist"
fi

