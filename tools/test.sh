#!/bin/bash

#set -ex

# check for cards in given file not already printed

trim() {
    local var="$*"
    # remove leading whitespace characters
    var="${var#"${var%%[![:space:]]*}"}"
    # remove trailing whitespace characters
    var="${var%"${var##*[![:space:]]}"}"   
    echo -n "$var"
}

while IFS='' read -r line || [[ -n "$line" ]]; do
    if ack -i "\b$(trim $line)\b" > /dev/null
    then 
        :
    else
        echo "$line"
    fi
done < "$1"


