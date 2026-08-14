#!/bin/bash
#Geting the username of the logged-in user
logged_in_user= $whoami
#checking if the user is logged in
if [ -n $logged_in_user ];then
	echo "The logged-in-user is: $USER"
else
	echo "User is not logged in"
fi

