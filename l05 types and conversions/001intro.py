## datatypes discussed so far
#   int
#   float
#   bool
#   string

print(type(True))   #bool
print(type(633))    #int
print(type(633.0))  #float
print(type("633"))  #string

#conversion
count = int(4.0)
print(count)
print(type(count))

#example2  [ string from a number ]
house_number = 13
street_name = "The Cresent"
town_name = "Belmont"
print(type(house_number))

address = str(house_number)+" "+street_name+", "+ town_name
print(address)
print(type(address))

#example 3 [number from a string ]
grams = "35.0"
print(type(grams))
grams = float(grams)
print(type(grams))