# Exercise to learn to define functions. def is the magic word here

# this one is like the scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# Apparently, the *args is pointless because we can just do the following:
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# This just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# This one takes no arguments
def print_none():
	print "I got nutn'."
	
print_two("Cornelius", "Schnublin")
print_two_again("Sacarecious", "Lequit")
print_one("1", '2', '73')
print_none()