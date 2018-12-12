#!/usr/bin/env python

from subprocess import call

silent = open('/dev/null')

result = call(["ack", "-i", "omnath"], stdout=silent)

print result

print "=" * 50

result = call(["ack", "-i", "wurstdueunidaternu" + "nudirtaen"], stdout=silent)

print result
