# we can have a global variable that can be accessed 
# anywhere outside or withing teh functions
ans = 10 #glibal variable 

def show_ans():
    print(ans)

show_ans()  # accessing it from the function
print(ans)  # accessing it outside the function