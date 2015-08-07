# Function that says it's adding two numbers, then adds said numbers
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

# Function that subtracts the second number passed in from the first	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
# Function that multiplies two numbers together and whatnot
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

# Divides a into b	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with these functions!"

age = add(30, 5)
height = subtract(97, 31)
weight = multiply(23, 5)
iq = divide(169, 13)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# Puzzle 4 'extra credit'
print "Here's the puzzle."

# Just embedding the functions since they all return an int
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?" 