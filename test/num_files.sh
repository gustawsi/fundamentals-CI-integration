#!/bin/bash
path=$1
size=$(ls -l ${path}| egrep "^." -c)
echo $((${size} - 1))