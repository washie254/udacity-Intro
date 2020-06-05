# break terminates a loop. 
# continue skips an iteration of a loop 
#this list contains tuples of items and their weight 
manifest = [("bananas", 15),("mattresses",34),("dog kennels",42),("machine",120),("cheeses",5)]

# assume we want to load the items in the list to a ship 
# which has a maximum capacity, i.e when capacity of ship is reached, 
# we'll stop onloadin

weight = 0
items = []
for cargo in manifest:
    print("Current Weight {} ".format(weight))
    if weight >= 100:
        print("Breaking loop now")
        break
    else:
        print(" adding {} ({})".format(cargo[0], cargo[1]))
        items.append(cargo[0])
        weight +=cargo[1]

print(weight)
print(items)

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))