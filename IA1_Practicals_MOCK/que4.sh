#!/bin/bash

while IFS=[,] read -r col1 col2 col3 col4 
do
	echo " Column1= col1 "
       	echo " Column2= col2"
	echo " Column3= col3"
        echo " Column4= col4"

done < que4.txt


