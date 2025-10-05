#!/bin/bash
#List the contents of the current directory and also the name and size of the largest file.


echo "Contents of the current directory"
ls -lhs | sort -rh | head -n 1



