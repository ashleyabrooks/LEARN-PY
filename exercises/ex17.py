from sys import argv
from os.path import exists

script, from_file, to_file = argv

raw_input("Ready to copy %s to %s? " % (from_file, to_file))

indata = open(from_file).read()
outdata = open(to_file, 'w').write(indata)

print "Boom."
