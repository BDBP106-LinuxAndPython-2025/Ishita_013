#a script to take integer input and check if it is prime or not

#!/bin/bash
read -p "Enter an integer: " num

if (( num <= 1 )); then
    echo "$num is not a prime number."
    exit
fi

is_prime=1
for (( i=2; i*i<=num; i++ )); do
    if (( num % i == 0 )); then
        is_prime=0
        break
    fi
done

if (( is_prime == 1 )); then
    echo "$num is a prime number."
else
    echo "$num is not a prime number."
fi

