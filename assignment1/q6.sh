# A script to generate the multiplication table for a given number from 1 to 20.
#!/bin/bash
read -p "Enter number: " num
for ((i=1; i<=20; i++)); do
  echo "$num x $i = $((num * i))"
done
