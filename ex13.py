# It's like importing a library in java (importing functions and tools to use here)
from sys import argv

# Defines how many arguments will need to be passed in 2 da command line to run the script
script, lettuce, do, the, argumenting = argv

# Just unwraps the arguments passed into the command line to print these sentences
print "The script is called:", script
print "Your first variable is:", lettuce
print "Your second variable is:", do
print "Your third variable is:", the
print "Your fourth variable is:", argumenting
 
# Playing with user input along with arguments in the command line
question = raw_input("What is another name for Haile Selassie I? ")
answer = "Jah"
if question == answer:
	print question + " Live"
if question == answer.lower():
	print question + " Live"
if question == answer.upper():
	print question + " Live"
if question != answer:
	if question == answer.lower():
		if question == answer.upper():
			print "Sorry, please read the following out loud: 'I am wrong'"