import os
myFileName = input('Enter a FileName to be searched:')
#isfile() returns True if file exists otherwise False
fileExists = os.path.isfile(myFileName)
print(fileExists)