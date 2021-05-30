from io import open


#open file
file = open("file_text.txt", "r")
text = file.read()
file.close()
print(text)

#read and save list
file = open("file_text.txt", "r")
list_read = file.readlines()
file.close()
print(list_read)

