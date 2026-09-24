#!/bin/bash
#
function db1 {
	value=$1 #$1 refers to the argument to the function, not to the main script
	#echo $[$value*2]
	echo $(echo "scale=4;$value*3.7"| bc)
}

result=$(db1 $1) #$1 here refers to the argument to the main script and must be entered in the shell command line.
echo 'Result is '$result
