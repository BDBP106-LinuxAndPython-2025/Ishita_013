#!/bin/bash

	if [ $# -ne 4 ]; then
		echo "Please provide 4 values"
	else
		echo " Argument1: " $1
		echo " Argument2: " $2
		echo " Argument3: " $3
		echo " Argument4: " $4
	fi




	#the output was something like:
# bash que4.sh 5 5 6 6
# Argument1:  5
#  Argument2:  5
#  Argument3:  6
#  Argument4:  6
# ibab@IBAB-RA-Comp203:~/IA1_Practicals_MOCK$ vi que4.sh
# ibab@IBAB-RA-Comp203:~/IA1_Practicals_MOCK$ bash que4.sh 
# Please provide 4 values
# ibab@IBAB-RA-Comp203:~/IA1_Practicals_MOCK$ bash que4.sh 8845
# Please provide 4 values

#when no values were put we were guven the non xero exit command and similarly on putting 1/2/3 values we got the same error message
