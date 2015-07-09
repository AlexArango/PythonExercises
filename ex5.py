name = 'Alex Arango'
age = 21.1 #approximately
height = 69 #inches on a good day
lbs_weight = 160 #stone
stone_weight = lbs_weight * 0.714
eyes = 'brown'
teeth = 'white'
hair = 'brown'

#Let's define what this %d, %s, %r business means
# %d means simple integer
# %s means simple string
# %r means something complex like a float or mixed numbers and words

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %r stone heavy." % stone_weight
print "Actually, that ain't too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the food he eats." % teeth

# I guess this line is tricky or something
print "If I add %r, %r, and %r I get %r." % (
	age, height, weight, age + height + weight)