names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
#change the names to usernames
# should be in smal letters separated by an underscore
for name in names:
    name = name.lower().replace(" ", "_")
    usernames.append(name)

print(usernames)


print("------------------------------")
for name in names:
    name = name.lower().replace(" ", "_")

print(names)


#quiz2
print("+++++++++++++++++++++++++++++++")
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(" ","_")
print(usernames)