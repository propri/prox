#!/usr/bin/env python

import sys
import os
import re
import math

REGEX = '^\s*(\d+)[x* ]\s*(.*)$'

def load_list(fn):
    f = open(fn, 'r')
    lines = f.readlines()
    f.close()

    result = {}
    total = 0
    for l in lines:
        matches = re.match(REGEX, l)
        if not matches:
            continue
        count = int(matches.group(1))
        name = matches.group(2)
        if result.has_key(name):
            sys.stderr.write("double entry: %s\n" % name)
            result[name] += count
        else:
            result[name] = count
        total += count

    sys.stderr.write('%d total (%d pages, %d empty slots)\n' % (total, int(math.ceil(total / 9.0)), (9 - (total % 9)) % 9))

    return result

def sort_list(fn):
    cards = load_list(fn)

    card_names = cards.keys()

    card_names.sort()

    for name in card_names:
        print "%d %s" % (cards[name], name)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "file name required"
        sys.exit(1)

    fn = sys.argv[1]

    if not os.path.isfile(fn):
        print "not a file: %s" % fn
        sys.exit(1)

    sort_list(fn)


