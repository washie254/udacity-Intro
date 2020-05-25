#iterating through a dict using for loop only gives you the keys
cities = {"Nairobi":23,"Mombasa":14, "Nyeri":45, "Eldoret":40}

print(len(cities))

for city in cities:
    print(city)

# Example two: iterating for both key and value.
# Consider this dictionary that uses names of actors as keys and their characters as values.
cast = {
    "Jerry Seignfield": "Jerry Seignfield",
    "Julia Louis-DREFUS":"Elaine Benes",
    "Jason Alexander":"George Costanza",
    "Michael Richards":"Cosmo Cramer"
}
#Iterate through hthe usual way with for loop
print("-----------------------")
print("------ just key  ------")
for key in cast:
    print(key)

#Iterate both key and value
print("iterate key and values")
print("-----------------------")

for key, value in cast.items():
    print("Actor: {} Role: {}".format(key, value))
