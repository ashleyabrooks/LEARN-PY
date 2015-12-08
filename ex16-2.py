from sys import argv

script, filename = argv

bs = open(filename)

print "Here's your file mothafucka %r:" % filename
print bs.read()
