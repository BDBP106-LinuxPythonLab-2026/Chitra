#!/bin/bash
function divide {
	local a=$1
	local b=$2
	if [ $b -eq 0 ];then
		echo "Cannot divide by zero"
		return
	fi
	local q=$(echo "scale=2 ; $a / $b"| bc)
	local r=$(echo "scale=2 ; $a % $b"| bc)
	echo "Quotient is: $q"
	echo "Remainder is: $r"
}
divide 6 3






