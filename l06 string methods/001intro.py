# methods and functions
# method -> are associated with specific types of objects
# methods are funcrtions that belong to an object
print("washignton mugo".title()) #title will capitalize first letter of each word

full_name = "Peter Mwangi"
print(full_name.islower()) # checks whether tehe characters n a string are lowercase
#nb full_name is the argument to islower()

print("one fish, two fish, three fish, four fish, blue fish".count('fish'))

#format()
num = 23
print("wshington has {} baloons".format(num))

animal = "dog"
act = "bite"
print("does your {} {}".format(animal,act))

maria_string = "Maria loves {} and {} "
print(maria_string.format("maths","statistics"))

print("213.34".islower()) #false

#other fun methods
str = "washington muGo"
print(str.capitalize())  # first character capitalized and the rest lowercased.
print(str.casefold()) #similar to lowercasing but more aggressive because it is intended to remove all case distinctions

#split(sep,maxsplit)
#setp   -> 'separator'. It can be used to identify how the string should be split
#           eg whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)
# the default separator is whitespace
# maxsplit -> maxsplit argument provides the maximum number of splits
#             The argument gives maxsplit + 1 number of elements in the new list

new_str = "the cow jumped over the moon."
print(new_str.split())          # A basic split method
print(new_str.split(' ',3))     # Here the separator is space, and the maxsplit argument is set to 3.
print(new_str.split("."))       # Using '.' or period as a separator.
print(new_str.split(None,3))    # Using no separators but having a maxsplit argument of 3.
