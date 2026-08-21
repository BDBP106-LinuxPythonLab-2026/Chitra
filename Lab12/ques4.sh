#!/bin/bash
read -ra numbers < nums.txt
echo ${numbers[*]}
len=${#numbers[@]}
for (( i=0 ; i<=$len ; i++ ))
do
	echo $((numbers[i] + numbers[i]))

done

