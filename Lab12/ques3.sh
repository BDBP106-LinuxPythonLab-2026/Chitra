#!/bin/bash
echo "Enter a number"
read n
m=1
until [ $m -gt 15 ]
do
	echo "$n x $m = $((n * m))"
	m=$[m+1]
done
