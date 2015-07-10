# There's a comma at the end of each print line so the line doesn't end and close
# This allows it to expect an input to be able to react to
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

respuesta = "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
print respuesta
	
# Sample practice
weird_answer = raw_input(respuesta)
print weird_answer