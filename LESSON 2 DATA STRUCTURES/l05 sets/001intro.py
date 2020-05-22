# set   -> A set is a data type for mutable unordered collections of unique elements.
# we can create a set from a list 

countries = ["Ghana", "Kenya","Dubai","India","Kenya","United States","Tanzania","Uganda","Nigeria","Tanzania"]
country_set = set(countries)

print(countries)
print(country_set)
print("The len of list is {} elements, and length of set is {}  elements".format(len(countries),len(country_set)))
print("hence we have removed {} Duplicate entries".format(len(countries)-len(country_set)))

# set supports the 'in ' operator just like list do 
print('Kenya' in country_set)       #True
print('Angola' in country_set)      #False

#Add()  -> adding an element in a set 
country_set.add("Angola")
print(country_set)

#pop() - > removes a random element in the set since it is unordered
print(country_set.pop())    # will display the poped element 
print(country_set)          # will display remaining element s minus the poped one

#union, intersection and difference are operations that can also be done in matthematical sets 
