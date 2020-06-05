# Zip returns an itereator that combines mutliple iterables
# into one sequence of tuples 
# each tuple contains the elements in that position 
# from all the iterables 
print("-----Method 1----")
items =['banana','mattresses','dog kennels','machine','cheeses']
weights =[15, 34, 42, 120, 5]

print(list(zip(items,weights)))

# Or
print("----Method 2----")
for cargo in (zip(items,weights)):
    print(cargo[0],cargo[1])    

#or
print("-----Method 3-----")
for item, weight  in zip(items,weights):
    print(item, weight)

#UNXIPPING
print("--------UNZIPPING-------")
manifest = [('banana', 15), ('mattresses', 34), ('dog kennels', 42), ('machine', 120), ('cheeses', 5)]
items, weights = zip(* manifest)
print(items)
print(weights)

"""
Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. 
There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.
"""
print("-----TRANSPOSE DATA----------")
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)


"""
Use enumerate to modify the cast list so that each element contains the name 
followed by the character's corresponding height. 
For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".
"""
print("----Enumuration-----")
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
# write your for loop here
for i, character in enumerate(cast):
    cast[i]= character+" "+str(heights[i])


print(cast)