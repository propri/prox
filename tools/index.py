#!/usr/bin/env python

import json
from subprocess import call
import os

f = open('scryfall-default-cards.json')
cards = json.load(f)
f.close()

by_name = {}

for card in cards:
    card_name = card.get('name').lower()
    if by_name.has_key(card_name):
        by_name[card_name].append(card)
    else:
        by_name[card_name] = [card]

#for card in by_name:
#    if 
#print by_name['omnath, locus of rage'][0]

dev_null = open('/dev/null')

os.chdir('..')

my_cards = {}

for card_name in by_name:
    if not call(['ack', '-i', '-1', card_name], stdout=dev_null):
        my_cards[card_name] = by_name[card_name]

os.chdir('data')
out = open('mycards.json', 'w')
json.dump(my_cards, out)
# json.dump(by_name, out)
out.close()

