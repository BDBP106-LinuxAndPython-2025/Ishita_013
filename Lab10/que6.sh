#!/bin/bash

#echo "Input a number"
#read n
#
#if [[ "$n" -gt 100); then
#	echo "The number is greater than 100."
#else 
#	echo "The number is not greater than 100."
#fi
#if [[ "$n" -gt 100 }] then 
#	echo "The number is greater than 100"
#fi

#there are multiple errors in this code
#the syntax errors show 1. use of ) in line 6- unexpected token and if condition not completed.
#2. syntax error 2. syntax error in line 11- unexpected token } 
#3. Unnecessary third if statemwnt at the end gives a error


echo "Input a number"
read n
if [ "$n" -gt 100 ]; then
	echo "The number is greater than 100"
else
	echo "The number is not greater than 100"
fi
 
