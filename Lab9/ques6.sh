#!/bin/bash
echo "$HOME"
calculation=$(bc << EOF
scale=4
23934/44343
EOF
)
echo "The output is:$calculation"
ls $HOME | grep "^D"
grep "$USER" /etc/passwd





