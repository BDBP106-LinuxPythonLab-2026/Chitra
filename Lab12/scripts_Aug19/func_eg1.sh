#!/bin/bash
#
#function <name> {
#    commands
#}

function func1 {
	echo 'This is my first function'
}

echo 'Calling my first function'
#func1
n=10
while [ "$n" -gt 0 ]
do
	func1
	n=$[$n-1]
done
