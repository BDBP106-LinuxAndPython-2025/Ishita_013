#Create an array of 5 numbers. The script should print the largest number, smallest number and sum of all numbers in the array

#!/bin/bash
numbers=(3 7 2 9 5) # Example array
echo ${numbers[@]}
max=${numbers[0]}
min=${numbers[0]}
sum=0
for num in "${numbers[@]}"; do
    if (( num > max )); then
        max=$num
    fi
    if (( num < min )); then
        min=$num
    fi
    (( sum += num ))
done
echo "Largest: $max"
echo "Smallest: $min"
echo "Sum: $sum"

