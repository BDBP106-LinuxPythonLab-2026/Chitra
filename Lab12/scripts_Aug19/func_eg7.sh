#!/bin/bash
#
# passing variable arrays to a function
#
function passarray {
	local newarray=($(echo "$@"))
	newarray[2]=9
	echo "The array in the function is "${newarray[*]}
}
myarray=( 1 2 3 4 5 )
echo "The array in the script is "${myarray[*]}
passarray ${myarray[*]}
echo "Is the array newarray available to the main script?" ${newarray[*]}
