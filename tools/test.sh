#!/bin/bash

#set -ex

# check for cards in given file not already printed

# search command
SEARCH="ack -i --ignore-dir=tools"

trim() {
    local var="$*"
    # remove leading whitespace characters
    var="${var#"${var%%[![:space:]]*}"}"
    # remove trailing whitespace characters
    var="${var%"${var##*[![:space:]]}"}"   
    echo -n "$var"
}

while IFS='' read -r line || [[ -n "$line" ]]; do
    if $SEARCH -i "\b$(trim $line)\b" > /dev/null
    then 
        :
    else
        echo "$line"
    fi
done < "$1"


