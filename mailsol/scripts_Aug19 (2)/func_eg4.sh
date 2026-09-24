#!/bin/bash
#
function db1 {
	value1=$1 #$1 refers to the argument to the function, not to the main script
	value2=$2
	summ=$[$value1+$value2]
	echo $summ
}

value1=$1
value2=$2
result=$(db1 $value1 $value2)  #$1 here refers to the argument to the main script and must be entered in the shell command line.
echo 'Result is '$result

echo 'Is summ variable known outside the function? '$summ
