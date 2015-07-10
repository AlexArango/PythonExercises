# In this lesson, we're learning how to use backslash to write different characters
# For example: /n = new line; \t = tab or indent; \\ = \; and \" = "
# Also, \n and \v basically do the same thing
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# Triple quotes to be able to type lines upon lines on end
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# Printed a list of indented and bullet pointed things

# Prints the strings saved in these variables
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Practice
oracion = "Something with a %s space" 
print oracion % '\n'

# Combines escape sequences such as \n and \t with formates like %s and %d
print '''
%s This is the start or a paragraph and therefore needs to be indented.
%s Now this is a new line and thus needs to be on a new line.
%s Simple, isn't it?
''' % ('\t', "\n", "\v")

# So-called little piece of code that is apparently fun
while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,