#   Lists can be modified but strings can't -> mutability
#   Mutability is about whether or not we can change an object once it has been created.
months = ['january','february','march','april','may','june','july','august','september','october','november','december']
months[3] = "Friday"
print(months)

my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)

#Order is about whether the position of an element in the object can be used to access the element