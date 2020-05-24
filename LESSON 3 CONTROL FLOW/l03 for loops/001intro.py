names = ["washngton mugo","peter mwangi","stephen njuguna","kennedy irungu"]

for name in names:
    print(name.title())


#creating a list using a loop 
cities = ["new york city", "mountain view", "chicago", "los angeles"]
capitalized_cities = [] #initialize an empty loop
for city in cities:
    capitalized_cities.append(city.title())
print("------------------")
print(capitalized_cities)

# modiffying a list 
#   requires use of the function range(start, stop, step)
print("======Range========")
# caling range with 1 argument will make it the stop argument 
# and returns a sequence of numbersfrom 0 to that integer minus 1
print(list(range(4))) 

# caling range with 2 argument will make it the start and stop argument 
print(list(range(2,6)))

# caling range with 3 arguments will make it the start, stop and step
print(list(range(2,9,2)))

#printing just a range will show you a range object
print(range(9))

#view values in a range object 
for number in range(5,15,3):
    print(number)


#lets et the indexes in our cities examples
for index in range (len(cities)):
    cities[index] = cities[index].title() #this will capitalize each element of cities at a time
    print(cities)