#!/bin/bash

#the orignal script
#val1=Jayashree
#val2=Nagesh
#if [ $val1 > $val2 ]; then
 #   echo "$val1 is greater than $val2"
#else
#    echo "$val1 is lesser than $val2"
#fi

#Using > in [ ] without escaping or quotes causes shell redirection, creating a file named Nagesh.
#Hence the new code must contain the variables within double quotes that are executed correctly
#Earlier the code was comparing the strings based on the lengths while later is uses ASCII values to go about the comparison.

#the new code should be the following

val1=Jayashree
val2=Nagesh

if [ "$val1" \> "$val2" ]; then
    echo "$val1 is greater than $val2"
else
    echo "$val1 is lesser than $val2"
fi


#the new output is Jayashree is lesser than Nagesh
