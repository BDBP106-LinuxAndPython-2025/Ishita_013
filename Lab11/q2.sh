#!/bin/bash

filename="testfile.sh"

if [ -e "$filename" ]; then
    echo "File exists"
else
	echo "FIle does not exist"
fi

if [ -s "$filename" ]; then
        echo "File is not empty"
else
	echo "FIle is empty"
fi

if [ -f "$filename" ]; then
    echo "It is a regular file"
else 
	echo "The file is a not regular file"
fi


# -e checks if a file exists
# -s checks if a file exists and is not empty
# -f checks if a file exists and is a regular file
