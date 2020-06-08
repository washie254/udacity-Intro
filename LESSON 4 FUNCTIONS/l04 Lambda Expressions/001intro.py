# comparison btwn a function and a lmbda expression 
# 1. Function 
# def double(x):
#     return x*2

# 2. Lambda Expression ( Equivalent of the above function )
double = lambda x: x*2
# double = lambda num: num*2
# using the lambda expression
print(double(3))

# 3. With Multiple arguments
multi = lambda x,y,z: x*y*z
print(multi(2,3,4))
