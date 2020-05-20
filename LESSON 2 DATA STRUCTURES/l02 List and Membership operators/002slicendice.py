#Slice and Dice 
list_of_random_things = [1, 3.4, 'a string', True]

#slicing: nb -> the lowerbound is inclusive, but tyhe upper bound is exclusive
print(list_of_random_things[1:3])

#u can start slicing from the beggining by ommiting the first element
print(list_of_random_things[:3])

#...and vice verser
print(list_of_random_things[1:])

#  Similarities with a string
#  _> slicing
greetings = "Hello There"
months = ['january','february','march','april','may','june','july','august','september','october','november','december']

print(greetings[6:9], months[6:9])
#  _> support of membership operators 'in' and 'not in '  
# in        ->  evaluates  if the object on the left side is included n the object on the right 
# not in    ->  evaluates if the object on the left side is not included in the right side
print('her' in greetings, 'her' not in greetings)
print('sunday' in months, 'sunday' not in months )  
