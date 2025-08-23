#!/bin/bash
#to check if a string is empty or not using -z and -n


str=""

if [ -z "$str" ]; then
    echo "String is empty"
else
    echo "String is not empty"
fi

if [ -n "$str" ]; then
    echo "String is not empty"
else
    echo "String is empty"
fi

