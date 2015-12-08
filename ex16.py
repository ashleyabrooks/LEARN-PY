#imports argv from the system
from sys import argv
#adds variables to the argument variables
script, filename = argv

#prints a sentence and drops in filename variable named above
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#gives the user a ? prompt to do one of the options above
raw_input("?")

print "Opening the file..."
#opens the file and uses 'w' to allow user to write on file
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#erases everything in the file
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input ("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
