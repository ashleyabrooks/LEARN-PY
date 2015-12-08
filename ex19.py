# this defines the function and gives it two arguments
def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# prints cheese and crackers function with numbers written as arguments
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# now we're creating variables outside of the function, but we can still use them in the function later on
amount_of_cheese = 10
amount_of_crackers = 50

# now we're using the variables we just created as arguments in the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# now we're just showing off that the arguments don't have to just be integers or variables, they can be math problems too
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# this is really cool. we can use the variables we created AND add math problems too
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)
