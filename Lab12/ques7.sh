#!/bin/bash
function filedir {
	echo "Enter a filename"
	read file
	if  [ -e $file ];then
		echo "File exists"
		ls $file	  
	else
		mkdir newdirectory
		echo "New directory is created"

	fi
}
filedir
