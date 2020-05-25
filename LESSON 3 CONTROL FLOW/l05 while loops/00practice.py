#practice factorial with a for loop 
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1
# write your for loop here
for num in range(1, number+1):
    product = product*num

# print the factorial of number
print(product)