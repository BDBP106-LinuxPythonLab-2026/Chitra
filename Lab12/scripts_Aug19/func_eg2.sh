#!/bin/bash
#
function db1 {
	value=2
	#echo $[$value*2]
	echo $(echo "scale=4;$value*3.7"| bc)
}

result=$(db1)
echo 'Result is '$result
