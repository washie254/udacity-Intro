cities= ['new york city',"Mountain View","chicago","los angeles"]
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)

####Using list comprehension
print("-- using list comprehension----")

capitalized_cities = [city.title() for city in cities]
print(capitalized_cities)

#Another Example
print("--Example 2--")
squares = []
for x in range(9):
    squares.append(x**2)
print(squares)

print("--using list comprehension--")
squares =[x**2 for x in range(9)]
print(squares)

print("--- with a condition---")
squares =[x**2 for x in range(9) if x%2==0]
print(squares)

print("--- with a condition with an else---")
squares =[x**2  if x%2==0 else x+3  for x in range(9)]
print(squares)