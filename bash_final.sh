#!/bin/bash

for second in $(seq 1 $2):
do
	if [[ -e $1 ]]
	then
		echo "File $1 arrived in server after $second seconds"
		exit 0
	else
		sleep 1
	fi
done
echo "Timeout"

