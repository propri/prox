#!/usr/bin/env python3

import os
import sys
import re

# Beispiel Zeilen:
# 1x Wren's Run Packmaster (Prerelease Promos) - R - English - EX           0,29 EUR
# 1x Breakthrough [Playset] (Torment) - U - English - EX                    0,30 EUR
REGEX = '^\d+x ([^[(]+) [[(]'

def clean_lines(lines):
    for line in lines:
        match = re.match(REGEX, line)
        if match:
            print(match.group(1))

def main():
    if len(sys.argv) > 1:
        FILE_NAME = sys.argv[1]
        f = open(FILE_NAME, 'r')

        clean_lines(f.readlines())
        f.close()
    else:
        for line in sys.stdin:
            clean_lines([line])

if __name__ == '__main__':
    main()


