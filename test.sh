#!/bin/bash

#set -ex

while IFS='' read -r line || [[ -n "$line" ]]; do
    if ack -i "$line" > /dev/null
    then 
        :
    else
        echo "$line"
    fi
done < "$1"


