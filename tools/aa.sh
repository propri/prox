#!/bin/bash

SEARCH="${1}"
ALT_DIR="~/magic/inventory"

ack -i "${SEARCH}"

if [[ -d $ALT_DIR ]]
then 
	cd ~/magic/inventory
	ack -i "${SEARCH}"
fi

