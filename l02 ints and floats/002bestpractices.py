#g -> good  #b -> bad
print(8) #g
print (8) #b

print(4+5) #g
print( 4 +5) #b imidiatly after the parenthesis

print(3*7 - 1) # good, adding a space around the lower priority (subtraction)
print(3 * 7 - 1) #b

# avoid long lines of coode.
# limit to 79 - 99 characters per line
# if > 99 consider re writing, simplifying or separating your code into  multiple lines
# from PEP 8 standard Python guide attached below
# https://www.python.org/dev/peps/pep-0008/