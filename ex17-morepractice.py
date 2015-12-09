from sys import argv

script, fullname = argv
# creates variable to open file named in argv
presentname = open(fullname)

# prints prompt
print "Your name is..."
#reads file mentioned by user
print presentname.read()

# prints prompt to ask for mom's name
print "Now let's add your mom's name to the file."
#creates a raw input variable to ask for mom's name
mom_name = raw_input("What's her name? ")

presentname = open(fullname, 'w')

# present mom's name
presentname.write(mom_name)
