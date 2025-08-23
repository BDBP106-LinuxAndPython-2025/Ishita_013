#!/bin/bash
#to check if a file exists


echo "Input the file name" 
read n
echo "The file to be checked is:" $n

if [ -f "$n" ]; then
	echo "The file is exists"
elif [ -x "$n" ]; then 
	echo "The file is executable"
else 
	echo "The file does not exist or is not executable"
fi


  
