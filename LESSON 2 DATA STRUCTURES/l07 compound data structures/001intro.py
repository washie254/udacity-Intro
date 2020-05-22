#   We can include containers in other containers to create compound data structures. 
#   For example, this dictionary maps keys to values that are also dictionaries!

elements = {
    "hydrogen":{
        "number":1,
        "weight":1.00794,
        "symbol":"H"},
    "helium":{
        "number":2,
        "weight":4.002602,
        "symbol":"He"
    }
}

# Get the Helium Dictionary 
helium = elements["helium"]
#get hydrogen's weight 
hydrogen_weight = elements["hydrogen"]["weight"]

print("Helium Dict: {}".format(helium))
print("Hydrogen weight: {}".format(hydrogen_weight))

# You can also add a new key to the element dictionary.
print('============================')
oxygen = {"number":8, "weight":15.999, "symbol":"O"}
elements["oxygen"]=oxygen

print(elements)

#using the get()
print("+++++++++++++++++++=")
print(elements['helium'])
print(elements.get('boron', "Element not found"))