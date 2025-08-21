#!/bin/bash

echo "The value of home variable is $HOME"

var=$(bc << EOF
scale=7
23934/44343
EOF
)
echo "The answer of the operation is:" $var

var1=$(ls $HOME/D*)
echo "All files in home starting with D are:" $var1

var2=$(grep "$USER" /etc/passwd)
echo "Lines in /etc/passwd with username are:" $var2


