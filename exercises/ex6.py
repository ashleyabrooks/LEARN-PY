# This is the variable that will allow us to print the string later on.
x = "There are %d types of people." % 10
# variable. Although I'm not sure why we're doing this because it takes just as much work to write it.
binary = "binary"
# Variable
do_not = "don't"
# Variable that will allow us to print the string later on.
y = "Those who know %s and those who %s." % (binary, do_not)

print x # Here's the string
print y # Here's the other string

print "I said: %r." % x # %r is a formatting character that recalls the variable x.
print "I also said: '%s'." % y

hilarious = False # Defining the variable for later use
joke_evaluation = "Isn't that joke so funny?! %r" # Another variable but this one has a formatting character so we can answer the question later on

print joke_evaluation % hilarious # Now using the two variables above. Didn't know you could use random words as formatting characters

w = "This is the left side of..." # I feel like these next three lines were obvious and unnecessary. 
e = "a string with a right side."

print w + e
