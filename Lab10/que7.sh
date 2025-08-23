#!/bin/bash
#Getting the username of the logged-in user

loggedinuser=$(whoami)
#checking if the user is logged in
if [ -n "$loggedinuser" ];
then
	echo "The logged-in user is:" $loggedinuser
else
	echo "User is not logged in"

fi


#syntax error- ""not completed in if statement
#no variable- wrong variable name in if statement
#wrong variable name in echo statement
