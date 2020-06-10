# x = int(input("Enter a number: "))

#using a try statement
try: # try is first run, 
    x = int(input("Enter a number: "))
except: # this runs when python gets an exception from Try  
    print("that\'s is not a valid number ! ")
# Nb: program proceeds to run even though it gets an exception
print("\nAttempted Input\n")

# if we want the code to keep running till the user inputs a valid input
#  we can use a while loop
print("------------------------")
while True:
    try:
        x= int(input("Enter a number :"))
        break
    except:
        print("that\'s not a valid number !")
    
    finally: # this runs after the break in try as well as after the exception
        print("Attempted Input ! )")
