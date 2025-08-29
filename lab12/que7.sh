#!/bin/bash

DIR="Lab5"
if [ ! -d "$DIR" ]; then
  mkdir $DIR
  echo "Directory created newly"
else
  echo "Directory exists"
fi
ls $DIR

