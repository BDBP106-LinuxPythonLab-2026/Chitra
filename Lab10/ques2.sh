
#!/bin/bash
echo "ENTER FILE NAME YOU WANT TO SEARCH:"
read file
if [ -e $file ];then
	echo "$file exists:)"
	if [ -x $file ];then
			echo "$file is executable"
		else
			echo "$file is not executable"
	fi
else
	echo "$file doesn't exists"
fi 



