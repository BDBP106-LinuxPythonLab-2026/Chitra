#!/bin/bash
#
function db1 {
	#value=$[4+8] 
	local value=$[4+8]  #local command will make the variable value local
	echo $value
}

result=$(db1) 
echo 'Result is '$result
#db1
echo 'Value is '$value
