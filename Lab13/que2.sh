#!/bin/bash

gawk '{if ($2<25) print $1 }' textfile.txt
#-F',' sets the field separator to comma. $2 < 25 checks marks, { print $1 } prints the name


gawk '{if ($3=="Physics") print $1 }' data2.csv
#This prints the name if the third column is "Physics"

gawk '{ print $1" "  $2" "  $3 }' textfile.txt > data2.csv
#This saves the data the way it is in a csv file.

