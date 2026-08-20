#!/bin/bash

echo "Enter a filename"
read file
#1
if [ -e $file ]; then
	echo "File exists:)"
else
	echo "File doesn't exists:("
fi

#2
if [ -s $file ]; then
	echo "File has content"
	
else
	echo "File is empty"
fi
#3
if [ -f $file ]; then
	echo "It is a regular file"
else
	echo "It's a directory"
fi

