myfile = open('test.txt')

print(myfile.read())

#seek is used to bring cursor to the top of the file
myfile.seek(0)

#prints file content line by line
print(myfile.readlines())

myfile.seek(0)

print(myfile.readlines())

#close the opened file manually
myfile.close()

#using this modes, no need to close file manually
with open('test.txt', mode='r') as newfile:
    content = newfile.read()
    print(content)

#append mode
with open('test.txt', mode='a') as f:
    f.write('\nTest3')

#read mode
with open('test.txt', mode='r') as newfile:
    content = newfile.read()
    print(content)

#write mode (Overright or create new file)
with open('CreateNewFile.txt', mode='w') as f:
    f.write('Hello! New file is created!')

#read mode
with open('CreateNewFile.txt', mode='r') as content:
    print(content.read())