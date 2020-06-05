
#iterate a list alonside with the index
items =['bananas','mattresses','dog kennels','machine','cheeses']

print("-----method 1-----")
for i, item in zip(range(len(items)), items):
    print(i,item)

print("----Method 2 -----")
for  i, item in enumerate(items):
    print(i, item)