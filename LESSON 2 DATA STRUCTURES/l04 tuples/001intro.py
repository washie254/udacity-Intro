# Tuple     -> a data type for  immutable ordered sequences of elements
AngkorWat = (13.4125, 103.866667)   # coordtinates 

print(type(AngkorWat))  #   <class 'tuple'>
print("Angkor Wat is at latitude    : {} ".format(AngkorWat[0]))
print("Angkor Wat is at longitude   : {} ".format(AngkorWat[1]))


#NB : Tuples are immuutable, you can't add or remove items, or sort them in place
# can beused to assign variables in a compact way 
# parenthisis are optional when making tuples 
dimensions = 52, 40, 100
length, width, height = dimensions  #   Tuple unparking : assigning variables to contents of a tuple
print("the dimensions are {}x{}x{}".format(length, width, height))