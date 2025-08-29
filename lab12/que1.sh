#!/bin/bash

# Using while loop
i=0
while [ $i -le 10 ]; do
    echo $i
    i=$[i+1]
done

#This loop will print numbers 0 to 10 inclusively, each on a new line. The while loop manually increments the i variable.
