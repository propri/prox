#!/bin/bash

import time
import urllib
import json
import sys
import re
import os

REGEX = '^\s*(\d+)[x* ]\s*(.*)$'

MAX_CARDS = 100

DELAY = 0.1 # 100ms between requests

API_URL = 'https://api.scryfall.com/cards/search?q='

last_request = time.time()

def load_list(fn):
    f = open(fn, 'r')
    lines = f.readlines()
    f.close()

    result = {}
    for l in lines:
        matches = re.match(REGEX, l)
        if not matches:
            continue
        count = matches.group(1)
        name = matches.group(2)
        if result.has_key(name):
            sys.stderr.write("double entry: %s\n" % name)
            result[name] += count
        else:
            result[name] = count

    return result

def check_partial(names):
    global last_request

    exact_names = ['!"' + x + '"' for x in names]
    clear_query = ' or '.join(exact_names)

    print clear_query

    query = urllib.quote(clear_query)

    req_url = API_URL + query

    if time.time() < last_request + DELAY:
        print 'sleep'
        time.sleep(DELAY)

    last_request = time.time()

    print req_url

    result = urllib.urlopen(req_url)

    text = result.readlines()
    print text

    jsonStr = text[0]
    print jsonStr
    result = json.loads(jsonStr)

    data = result['data']

    result_names = [x['name'].lower() for x in data]

    not_found = False

    for name in names:
        if not name.lower() in result_names:
            print "%s not found!" % name 
            not_found = True

    if not_found:
        print clear_query
        print req_url
        print names
        print jsonStr
        sys.exit(1)
    
def check_names(names):
    i = 0
    partial = []
    for name in names:
        partial.append(name)
        i += 1
        if i == MAX_CARDS:
            check_partial(partial)
            i = 0

    if len(partial):
        check_partial(partial)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "file name missing"
        sys.exit(1)
    fn = sys.argv[1]
    if not os.path.isfile(fn):
        print "not a file: %s" % fn
        sys.exit(1)

    cards = load_list(fn)
    names = cards.keys()

    check_names(names)

