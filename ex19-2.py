def name_dropper(firstname, lastname):
    print "Your first name is %s." % firstname
    print "Your last name is %s." % lastname
    print "Which means your full name is %s %s." % (firstname, lastname)
    print "Maybe some people just call you %s." % lastname

print "Let's keep it simple:"
name_dropper("Ashley", "Brooks")

print "But we can also make it more complicated:"
SB_firstname = "Sarah"
SB_lastname = "Brooks"

name_dropper(SB_firstname, SB_lastname)
