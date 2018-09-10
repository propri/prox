#!/bin/bash

# get temporary file
COMPLETE_TEMP=$(mktemp)

# add all printed files together
find print -name '*txt' | xargs cat >> $COMPLETE_TEMP

# add not yet printed cards
cat new.txt >> $COMPLETE_TEMP

# sort all lines, removing doubles
tools/sort.py $COMPLETE_TEMP > tools/data/unique.txt

# remove temp file
rm $COMPLETE_TEMP

# remove number of cards
sed -r -i -e 's/^[0-9]+x? //' tools/data/unique.txt

