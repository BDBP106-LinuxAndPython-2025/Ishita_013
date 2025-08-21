#!/bin/bash 

var=$(bc << EOF
scale=8
m=1
s=299792458
e=m*s*s
e
EOF
)
echo "The final energy value is:" $var

