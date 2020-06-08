# read throughht this code snippet 
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()  
# this will give an error since the function is trying to ,
# modify the global variable 

# a better way to write this function would be 
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
print(egg_count)