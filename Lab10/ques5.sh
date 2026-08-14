#!/bin/bash
echo "Enter you score:"
read n
if [ $n -ge 90 ];then
	echo "Your Grade is A"
elif [ $n -ge 80 ] && [ $n -le 89 ]; then
	echo "Your Grade is B"
elif [ $n -ge 70 ] && [ $n -le 79 ]; then
	echo "Your Grade is C"
else
	echo "FAIL"
fi

