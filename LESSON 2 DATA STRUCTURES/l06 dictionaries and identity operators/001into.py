# A dictionary is a mutable data type that stores mappings of unique keys to values
# stores pairs of elements : keys and values
# eg element names and their corresponding atomic numbers 

elements = {'hydrogen':1, 'helium':2, 'carbon': 6 }
print(elements['carbon'])

# inserting new values into the dictionary
elements['lithium'] = 3
print(elements)
#dictionaries can have key of any immutable types
#checking whether a value is in the dictionary
print('mithril' in elements)
print('hydrogen' in elements)

#get()  -> returns 'None' or a default values of your choice if the key id not found
print(elements.get('helium'))   # returns the value of jey specified
print(elements.get('boron'))

#since errors can crash your program , we can check if a key 

#   < identiity operators   > 
#   returns None with the  'is' operator
print("--------------------")
x = elements.get('dilithium')
is_null  = x is None
print(is_null)

print("--------OR------------")
x = elements.get('delithium')
not_null = x is not None
print(not_null)