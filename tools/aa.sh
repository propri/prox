#!/bin/bash

SEARCH="${1}"

ack -i "${SEARCH}"

cd ~/magic/inventory

ack -i "${SEARCH}"

