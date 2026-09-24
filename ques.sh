1.
#!/bin/bash

is_happy() {
    n=$1
    declare -A seen

    while [ "$n" -ne 1 ]; do
        if [ "${seen[$n]}" = "1" ]; then
            echo "false"
            return
        fi

        seen[$n]=1
        sum=0

        while [ "$n" -gt 0 ]; do
            digit=$((n % 10))
            sum=$((sum + digit * digit))
            n=$((n / 10))
        done

        n=$sum
    done

    echo "true"
}

read -p "Enter a positive integer: " num

result=$(is_happy "$num")

echo "$result"

2.
#!/bin/bash

awk '
{
    for (i = 1; i <= NF; i++) {
        data[i, NR] = $i
    }

    if (NF > maxcol)
        maxcol = NF

    maxrow = NR
}

END {
    for (i = 1; i <= maxcol; i++) {
        for (j = 1; j <= maxrow; j++) {
            printf "%s%s", data[i, j], \
                (j == maxrow ? "\n" : " ")
        }
    }
}
' file.txt


