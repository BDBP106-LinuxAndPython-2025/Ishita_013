#!/bin/bash

function maximum {
  if [ "$1" -gt "$2" ]; then
    echo "The greater number is:" $1
  else
    echo "The greater number is:" $2
  fi
}
maximum 8 12     # Output: 12
maximum 44 5     # Output: 12

