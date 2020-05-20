# understanding common error mistakes 
#   ZeroDivisionError: division by zero
print(5/0)

#   TypeError: len() takes exactly one argument (0 given) -> if I accidentally do not include the required number of arguments
chars = "supercalifragilisticexpialidocious"
print(len())

#   SyntaxError: unexpected EOF while parsing -> often produced when you have accidentally left out something
greeting = "hello"
print(greeting.upper) # remove the  )