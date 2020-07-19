import csv
import os
import random
#import names
delimiter = ','

myCSVFileName = input('Enter a CSV Filename: ')
fileExists = os.path.isfile(myCSVFileName)

#Open the CSV File in append mode for creating Users details 
with open(myCSVFileName,'a',newline='') as appendInToCSVFile:
	csvHeader = ['English','Hindi','Sanskrit','Maths','Science','Social']
	MyHeader = csv.DictWriter(appendInToCSVFile,fieldnames=csvHeader)
	if not fileExists:
            MyHeader.writeheader()

	ID = 1
	while (ID <= 100000):
		MarksList = []
		for i in range(0,6):
			marks = random.randint(0,100)
			MarksList.append(marks)
			appendInToCSVFile.write(str(MarksList[i]))
			if(i<5):
				appendInToCSVFile.write(delimiter)
		appendInToCSVFile.write('\n')
		ID+=1