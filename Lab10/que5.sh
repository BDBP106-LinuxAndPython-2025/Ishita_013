#!/bin/bash

echo "Input a number:"
read n
echo $n

if [ "$n" -gt 0 ]; then
	echo " THe number is positive"
elif [ "$n" -eq 0 ]; then
	echo " The number is zero."
else
	echo " The number is negative"
fi

