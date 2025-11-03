# 1. Declare and assign the variables here:
space_shuttle = 'Determination'
shuttle_speed = 17500
mars_distance = 225000000
moon_distance = 384400
milesperkm = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(space_shuttle))
print(type(shuttle_speed))
print(type(mars_distance))
print(type(moon_distance))
print(type(milesperkm))

# Code your solution to exercises 3 and 4 here:
miles_to_mars = mars_distance * milesperkm
mars_travel_time = miles_to_mars / shuttle_speed
days_to_mars = mars_travel_time / 24

print(space_shuttle + " will take " + str(days_to_mars) + " days to reach Mars.")

# Code your solution to exercise 5 here
miles_to_moon = moon_distance * milesperkm
moon_travel_time = miles_to_moon / shuttle_speed
days_to_mars = moon_travel_time / 24

print(space_shuttle + " will take " + str(days_to_mars) + " days to reach the Moon.")
# The launchcode solution as shown will error, days_to_mars needs to be converted to a string.