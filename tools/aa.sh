#!/bin/bash

SEARCH="${1}"
ALT_DIR="${HOME}/magic/inventory"

ack -i "${SEARCH}"

if [[ -d $ALT_DIR ]]
then 
	cd $ALT_DIR
	ack -i "${SEARCH}"
fi

