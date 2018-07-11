#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
	if ack "$line" > /dev/null ; then
		:
	else
		echo $line
	fi
done < "$1"

