#!/bin/bash
#
#until <test-condition-is-false>
#do
#   commands
#done
#
n=10
until [ "$n" -eq 0 ]
do
	echo $n
	n=$[$n-1]
done
