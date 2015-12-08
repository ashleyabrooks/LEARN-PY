name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm_height = height * 2.54 # centimeters
cm_weight = weight * 0.45 # kilograms

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's actually %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "In other countries, you could say Zed is %d centimeters tall." % cm_height
print "In those other countries you could also say Zed is %d kilograms heavy." % cm_weight
