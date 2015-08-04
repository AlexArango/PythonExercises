# Imports library like in java
from sys import argv

# Takes in the argument to type into the command line
script, filename = argv

# Asks the user whether he wants to erase the file passed in to the command line
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-c (^c)."
print "If you do want that, hit ENTER."

# Prompts a decision from the user
raw_input("?")

# Opens the file and the 'w' tells it to allow writing into it
print "Opening the file..."
# Second parameter could be either 'w' or 'w+' or 'a+' or 'r+'
target = open(filename, 'a+')

# Reduces the file's memory to 0. AKA erases the contents of the file
print "Truncating the file. Goodbye!"
target.truncate()

# Prompts the user for lines to be written into the file
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Writes what the user wrote into the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Closes the file because, apparently, it is good practice
print "And finally, we close."
target.close()

# Extra practice addition to the exercise