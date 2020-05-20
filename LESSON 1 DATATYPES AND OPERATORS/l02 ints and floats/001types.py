# you can check the type of a variable or  number 
# by using type()
print(type(4))
print(type(4.0))

# convert a type to another
print(4+int(4.3))
print(float(78))

x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
print(type(x))
print(type(y))

###
# Because the float, or approximation, for 0.1 is actually slightly more than 0.1,
# when we add several of them together
# we can see the difference between the mathematically correct answer
# and the one that Python creates.
###
print(0.1+0.1+0.1)

print(.1+.1+.1==.3)   #True or False ? .... False
