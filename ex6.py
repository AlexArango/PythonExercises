# Just trying things out
#print "%r print = 'does this work?' and again 'works?' "+'let us see'+' "no?"'

# Declaring variables in Python. It seems like there are not different types
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Combines the previous strings declared above
print "I said: %r." % x
print "I also said: '%s'." % y

# Toying with Boolean values
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Long way of writing: print "Isn't that joke so funny?! %r" % hilarious
print joke_evaluation % hilarious

# Adding strings like they're math
w = "This is the left side of..."
e = "a string with a right side."

# Shorter way of writing: 
# print "This is the left side of..." + "a string with a right side."
print w + e