#!/bin/bash

echo "Contents of the current directory:"
ls

echo
echo "Largest file:"

ls -lh  | sort -nr -k5,5 | head -1

#Note this is only one way to get this task done, there are many ways of doing this!
