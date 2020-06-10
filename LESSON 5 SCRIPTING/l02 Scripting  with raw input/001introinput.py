# using input() -> takes user input as a string
name = input("Enter Your Name: ")
print("Hello , "+name.title())

# changing to other datatypes"
age = int(input("Age ?: "))
age+=10
print("You'll be {} years old in 10 years".format(age))

#Eval -> evaluates a string as a line of python 
x = eval(input('enter an expresion: '))
print(x)

# you can even include variables 
num = 30
x = eval('num + 40')
print(x)
