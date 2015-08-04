# Function that prints out the two number parameters passed in to it
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
# A call to the function above 	
print "We can just give the function numbers directly:"
cheese_and_crackers(19,23)

# Assigning ints to variables to use as parameters for the function above
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 31

# Call to the function with the variables defined above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Call to the function with the parameters being summation expressions
print "We can even do math inside, too:"
cheese_and_crackers(17 % 13, 7 - 11)

# Adding numbers to the variables from above and passing these expressions as parameters
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 97, amount_of_crackers + 1001) 

# Another way to call the function utilizing user input
print "How many cheeses to you have?"
answer1 = raw_input()

# isdigit() Ensures the input from the user is a number
#print answer1.isdigit()

# Keeps prompting the user for a number and does not move on until user inputs a number
while answer1.isdigit() == False:
   print("That's not an int! Please enter a number. We won't move on until you do!")
   answer1 = raw_input()
   
# Turns the user input from a 'string' to an 'int'
val1 = int(answer1)
   
print "How many crackers to you have?"
answer2 = raw_input()

# Keeps prompting the user for a number and does not move on until user inputs a number
while answer2.isdigit() == False:
   print("That's not an int! Please enter a number. We won't move on until you do!")
   answer2 = raw_input()
   
# Turns the user input from a 'string' to an 'int' 
val2 = int(answer2)

# Calling the function using the user's input
cheese_and_crackers(val1, val2)