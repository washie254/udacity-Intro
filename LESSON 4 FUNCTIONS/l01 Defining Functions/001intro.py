# function that calulates the volume of a cylinder

def cylinder_volume(height, radius):
    pi = 3.14159 # Local Variable: can only be used within this function
    volume =  height*pi*radius**2
    return volume

print(cylinder_volume(10,3))

# a function that takes no arguments
def print_greetings():
    print("Hello, World")

print_greetings()

# if an argument is not specified we can put a default value
def cylinder_volume(height, radius=3):
    pi = 3.14159 # Local Variable: can only be used within this function
    volume =  height*pi*radius**2
    return volume

print(cylinder_volume(10,5))
# passing values by names
print(cylinder_volume(height=10,radius=8))