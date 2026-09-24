#!/bin/bash

read -p "Enter the filename: " filename

if [ -f "$filename" ]; then
    lines=$(wc -l < "$filename")
    words=$(wc -w < "$filename")
    characters=$(wc -m < "$filename")
    echo "Number of lines      : $lines"
    echo "Number of words      : $words"
    echo "Number of characters : $characters"
else
    echo "File does not exist."
fi

#Note: The use of < in 
# wc -l < "$filename"
# is to prevent the output of filename along with the count.
# Otherwise the wc command also prints the filename.
