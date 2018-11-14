#!/usr/bin/env python

import os
import sys

def get_data():
    if len(sys.argv) < 3:
        raise Exception('expect two filenames')
    files = sys.argv[1:3]
    data = []
    for f in files:
        if not os.path.isfile(f):
            raise Exception('not a file: %s' % f)

        o = open(f, 'r')
        lines = o.readlines()
        # trim?
        o.close()
        data.append(lines)

    return data

def main():
    data = get_data()
    result = []

    for l in data[0]:
        if l in data[1]:
            result.append(l)

    sys.stdout.writelines(result)

if __name__ == '__main__':
    main()

