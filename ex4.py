#Define how many cars we have
cars = 100
#How much space is in each car
space_in_a_car = 4.0
#How many drivers we have today
drivers = 30
#How many passengers are there today
passengers = 90
#How many cars are left over (not enough drivers)
cars_not_driven = cars - drivers
#Cars with drivers
cars_driven = drivers
#The total space we have today in all cars
carpool_capacity = cars_driven * space_in_a_car
#How many passengers will have to be in each car on average to all get transported
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
