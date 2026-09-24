#!/bin/bash

#Using -p is better than -n because -n is actually meant to limit the number of characters you enter before the terminal submits your input to the script.
#By default, -n does not have a limit though and hence at present it will also work. In a standard BASH script however this should be there.
read -p "Enter the filename: " filename

if [ -e "$filename" ]; then
    echo "File exists."
    if [ -r "$filename" ]; then
        echo "The file is readable."
    else
        echo "The file is not readable."
    fi
    if [ -w "$filename" ]; then
        echo "The file is writable."
    else
        echo "The file is not writable."
    fi
else
    echo "File does not exist."
fi
