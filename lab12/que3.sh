#!/bin/bash

read -p "Enter a number: " num
i=1
until [ $i -gt 15 ];
do
  echo "$num * $i = $[num * i]"
  i=$[$i + 1]
done


#Allows the user to enter a number and prints the multiplication table up to 15. It takes the counter number and multiplies it with the number entered.
