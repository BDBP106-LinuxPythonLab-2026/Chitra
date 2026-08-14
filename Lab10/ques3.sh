#!/bin/bash
echo "Enter filename :"
read file
if [ -e $file ];then
	echo "File exists:)"
	echo "$exit 200"

else
	echo "File doesn't exits and the exit code is:"

	echo "$exit 201"
fi

