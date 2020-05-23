# DOS AND DONT'S
# Don't use True or False as conditions
# Bad example
if True:
    print("This indented code will always get run.")

# Another bad example
if is_cold or not is_cold:
    print("This indented code will always get run.")

# Bad example
# This code is valid in Python, but it is not a boolean expression, 
# although it reads like on
if weather == "snow" or "rain":
    print("Wear boots!")

# Bad example
# Don't compare a boolean variable with == True or == False
if is_cold == True:
    print("The weather is cold!")

# Good example
if is_cold:
    print("The weather is cold!")

# objects that are considered False in Python:
# constants defined to be false: None and False
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '"", (), [], {}, set(), range(0)