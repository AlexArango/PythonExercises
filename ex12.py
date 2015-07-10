# In this exercise, we will rewrite the entire last exercise in a more efficient way

# This simply just writes the strings that ask the questions inside the (and) characters 
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)