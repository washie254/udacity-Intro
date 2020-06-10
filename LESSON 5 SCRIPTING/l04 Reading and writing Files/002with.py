# it's easy to forget to close a file 
# with automatically closes the file once done with 
# operating witth a file 
with open('another_file.txt','r') as f:
    file_data = f.read()
    
print(file_data)

##############################################
#   Calling the read Method with an Integer #
print("---------read(x)-----")
"""
If you pass the read method an integer argument, 
it will read up to that number of characters, output all of them, 
and keep the 'window' at that position ready to read on 
"""
with open('camelot.txt') as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

##############################
#   Reading line by line    #
print("\n ------ Read Lines -----")
with open('camelot.txt') as line:
    print(line.readlines())


##########################
#   Looping over Lines  #
print("\n ------ooping over lines ------")
camelot_line = []
with open('camelot.txt') as f:
    for line in f:
        camelot_line.append(line.strip())
print(camelot_line)