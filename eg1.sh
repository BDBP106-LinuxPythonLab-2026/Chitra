#!/bin/bash
echo "enter filename"
read file
if [ -e $file ]; then
	echo "File exists" 
	if [ -r $file ];then 
		echo "File is readable"
	else 
		echo "File is not readable"
	if [ -w $file ];then
		echo "File can be edited"
	else
		echo "File cant be edited"
else 
	echo"File doesn't exists"
fi

