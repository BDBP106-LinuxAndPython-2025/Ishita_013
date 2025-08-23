#!/bin/bash


var1="Testing"
var2="testing"

if [ "$var1" \> "$var2" ]; then
    echo "$var1 is greater than $var2"
else
    echo "$var1 is lesser than $var2"
fi

#Testing is lesser than testing is the result we get after running this command.
#after saving the variable in a new file and sorting then the result is testing then Testing as it interprets the values according to their ASCII values.
##Both if and sort handle upper and lower cases differently.
