#!/bin/bash

echo "Input card names, one per line (^D to quit)"
echo -n "> "

while read search
do
    if [[ -n "$search" ]]
    then
        echo "==============================="
        ./tools/aa.sh "$search"
        echo "==============================="
    fi
    echo -n "> "
done

