#!/bin/bash
path=$1
size=$(du -c ${path} | tail -n1 | egrep -o "[0-9]*")
echo ${size}