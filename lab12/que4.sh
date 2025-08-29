#!/bin/bash

read -ra numbers < nums.txt
#-r: Prevents backslash escapes from being interpreted.
#-a numbers: Puts each item into an array named numbers.
#< nums.txt: Reads numbers from the file.
for num in "${numbers[@]}";
do
  echo "Original:" $num
  echo "Double: $((num * 2))"
done

