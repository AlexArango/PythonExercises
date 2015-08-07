# Imports 'library' thingy to run file from command line
from sys import argv

script, input_file = argv

# Function that prints the whole file ran with the script
def print_all(f):
	print f.read(), "\n"

# Goes back to the beginning of the file to read it over
def rewind(f):
	f.seek(0)

# Prints a specific line from the file
def print_a_line(line_count, f):
	print line_count, f.readline()

# Sets a variable for the file loaded by the user
current_file = open(input_file)

print "First, let's print the whole file: \n"

# Prints the file
print_all(current_file)

print "Now let's rewind, kind of like a tape. \n"

# Goes back to the top of the file (so it can be read again)
rewind(current_file)

print "Let's print three lines: \n"

# Prints the first line
current_line = 1
print_a_line(current_line, current_file)

# Second line because 1 + 1 = 2
current_line = current_line + 1
print_a_line(current_line, current_file)

# Third line because 2 + 1 = 3
current_line = current_line + 1
print_a_line(current_line, current_file)