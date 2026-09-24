#!/bin/bash
#
# while <test-condition is true>
# do
#    commands
# done
#

n=10
while [ "$n" -gt 0 ]
do
	echo $n
        n=$[$n-1]
done
