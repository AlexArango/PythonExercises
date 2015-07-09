cars = 100

#Just what it says
#Something notable is that it seems to be standard to replace space with an underscore 
space_in_a_car = 4

#I think all these variables are pretty self explanatory
drivers = 30
passengers = 90

#Cool little calculation
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

