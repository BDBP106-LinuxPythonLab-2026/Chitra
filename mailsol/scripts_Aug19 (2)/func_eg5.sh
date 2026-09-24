#!/bin/bash
#
# passing variable arrays to a function
#
function passarray {
	newarray=($(echo "$@"))
	echo "The array in the function is "${newarray[*]}
}
myarray=( 1 2 3 4 5 )
echo "The array in the script is "${myarray[*]}
passarray ${myarray[*]}

