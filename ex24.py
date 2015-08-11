# Combining the skills previously learnt
print "Let's practice everything."

# I guess the way to ignore a symbol that otherwise does something when printing is 
# By putting one of them back slashes (\) before said symbol
print 'You\'d need to know \'bout escapes with \\ that do \n new \n newline and \t tabs.' 

# Printing a poem that combines that tab and new-line symbols when printing
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition 
and requires an explanation
\n\t\twhere there is none.
"""

# Lines that divide the weird, but insightful, poem from the rest of the weird stuff
print "-------------"
print poem
print "-------------"

# Setting a variable with an arithmetic equation
five = 10 - 2 + 3 - 6
print "This should be five: %s " % five

# Function that manipulates the variables passed in with math equations
# Then returns the variable values. It returns 3 values (in the last line)
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
# Sets a variable to be passed into the function defined above
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# Prints out the variable set above
print "With a starting point of: %d" % start_point

# Prints out the manipulated values taken from the starting_point variable
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# Setting the same variable with a different value
start_point = start_point / 10

print "We can also do that this way:"
# Wow! The function can also return even though it's in a print statement! 
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)