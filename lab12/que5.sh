#!/bin/bash

function divide {
   a=$1
   b=$2
  if [ "$b" -eq 0 ]; then
    echo "Error: Division by zero!"
  fi
  quotient=$(echo "scale=2; $a/$b" | bc)
  remainder=$[$a % $b]
  echo "Quotient:" $quotient
  echo "Remainder:" $remainder
}

divide 47 5



