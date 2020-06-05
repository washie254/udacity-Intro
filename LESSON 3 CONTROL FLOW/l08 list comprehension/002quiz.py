names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#change names to lower case, just the first name
first_names = [name.split()[0].lower() for name in names]# write your list comprehension here
print(first_names)