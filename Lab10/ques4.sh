#!/bin/bash
echo "ENTER A NUMBER"
read n
if [ $n -gt 0 ];then
	echo "$n is positive number"
elif [ $n -lt 0 ];then
	echo "$n is negative number"
else
	echo "The number is 0"
fi

