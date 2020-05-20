# a boolean is a datatype that can have a value of True or False
the_sun_is_up = True
the_sun_is_blue = False

print(the_sun_is_blue)

#Produce a boolean result  using comparison operators
x = 42 > 43
print(x)

###  COMPARISON OPERATORS  (Symbol operation)
#   <       less than
#   >       Greater than
#   <=      less than or equal to
#   >=      Greater than or equal to 
#   ==      Equal to 
#   !=      Not equal to 

###   LOGICAL OPERATORS (Keyword operation)
#   and         Evaluates if both sides are True
#   or          Evaluates if at least one side is true 
#   not         Inverse a boolean type

age = 14
is_teen = age > 12 and age <20
not_teen = not(age > 12 and age <20)
print("Is Teen : ", is_teen)
print("Is Not Teen : ", not_teen)  # inverses the statement