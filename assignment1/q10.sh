# script that takes a .csv file and prints only the first and third columns
#!/bin/bash

read -p "Enter CSV filename: " file
awk -F, '{print $1","$3}' "$file"
