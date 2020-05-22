# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai":17.8,"Istanbul":13.3,"Karachi":13.0,"Mumbai":12.5}
print(population)

print("-----------------")
a = [1, 2, 3]
b = a
c = [1, 2, 3]


#Equallity '==' VS Identity 'is'
print(a == b)
print(a is b)
print(a == c)
print(a is c)

#more with dictionaries 
print("==================================")
animals = {'dogs': [20, 10, 15, 8, 32, 15],
           'cats': [3,4,2,8,2,4],
           'rabbits': [2, 3, 3],
           'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(type(animals))
print(animals['dogs'])
print(animals['dogs'][3])
print(animals['fish'])