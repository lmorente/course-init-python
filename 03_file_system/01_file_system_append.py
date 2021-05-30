import pathlib
from io import open

"""
permission: read, append, write 
"""

#open file
file = open("file_text.txt", "a+")
file2 = open(str(pathlib.Path().absolute()) + "\\file_text2.txt", "a+")

#write file
file.write("*****Hello World*****\n This file has been written from python")

#close file
file.close()
