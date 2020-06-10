#python has numerous libraries 
# https://pymotw.com/3/
import math 
import string
import datetime
import os

print(math.factorial(4))
x = 23.45
print("abs : ", math.fabs(x))

s = " i was amazed by how raven play\'s  his games"
print(string.capwords(s))

t = datetime.datetime.now()
print(t)

path = "C:/"
os.chdir(path)
