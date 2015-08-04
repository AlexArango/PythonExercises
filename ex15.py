# Import library for arguments
from sys import argv

# Asks for the file name that it will read from
#script, filename = argv

# Opens said file to read
#txt = open(filename)

# Displays message to user before presenting desired file
#print "Here's your file %r:" % filename
#print txt.read()

# Prompts the user to type the name of the file again
print "Type the filename again:"
file_again = raw_input("> ")

# The user can actually enter any file here
txt_again = open(file_again)

# And the computer will willingly open it, if it exists! Even if it's not the same file!
print txt_again.read()

# Apparently, it is good practice to close files when done with them.
# Seems like memory allocation in C
txt_again.close()
