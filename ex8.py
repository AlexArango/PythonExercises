# Serves as a template that takes 4 arguments that are either numbers or strings
formatter = "%r %r %r %r"

# This will print those numbers
print formatter % (1, 2, 3, 4)

# Print the strings
print formatter % ("one", "two", "three", "four")

# Print the Boolean values
print formatter % (True, False, False, True)

# Prints the template itself
print formatter % (formatter, formatter, formatter, formatter)

# Prints strings, but the tricky thing here is why it prints strings with single quotes
# when the formatter has %r, but not when it's %s
print formatter % (
	'I had this thing.',
	'That you could type up right.',
	'But it didnt sing.',
	'So I had to say goodnight.'
)
 