# opening a file in python 
# open('path','mode')    # NB: mode is defaulted to read if not specified
# mode r: Read  w: Write 

f = open('my_file.txt','r')
file_data = f.read()  # Read the contents of a file 
print("-----read from file-----")
print(file_data)

#writing into a file 
# nb : w overrites currennt file contents 
# if file doesnt exist, python will create the file automatically
f2 = open('file2.txt','w')
f2.write("Hello world, this is the new context")
f2 = open('file2.txt','r')
file2_data = f2.read()


print("\n-----write into File----")
print(file2_data)

#close the file once done with it to free up system resources
f.close()
f2.close()