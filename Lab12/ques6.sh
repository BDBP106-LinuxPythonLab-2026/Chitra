#!/bin/bash
function maximum {
	a=$1
	b=$2
	if [ $a -gt $b ];then
		echo "$a is greater"
	else
		echo "$b is greater"
	fi
}
maximum 5 6
