#!/bin/bash

#set -ex

# check for cards in given file not already printed

# use stdin or file argument
[ $# -ge 1 -a -f "$1" ] && input="$1" || input="/dev/stdin"
normalized=$(< $input)

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
done <<< "$normalized"


