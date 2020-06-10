""" handling errors specifying exceptions """

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError: # specify that it's a value Error [so that keyboard interupts like cntrl +c still work ]
        print("that\'s not a valid Input ! ")

    except KeyboardInterrupt:
        print("\n No input Taken")
        
    finally:
        print("\n Attempted Input\n")


# NB:
try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))

