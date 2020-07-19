import csv
import os
import random
import names
import numpy
delimiter = ','

myCSVFileName = input('Enter a CSV Filename: ')

fileExists = os.path.isfile(myCSVFileName)


#Open the CSV File in append mode for creating Users details 
with open(myCSVFileName,'a',newline='') as appendInToCSVFile:
	csvHeader = ['REGISTRATION_NUMBER','NAME','GENDER','DEPARTMENT','CGPA']
	MyHeader = csv.DictWriter(appendInToCSVFile,fieldnames=csvHeader)
	if not fileExists:
            MyHeader.writeheader()

	ID = 2017100001
	while (ID <= 2017101000):
		studentId = ID
		appendInToCSVFile.write(str(studentId))
		appendInToCSVFile.write(delimiter)
		firstName = names.get_first_name()
		lastName = names.get_last_name()
		studentName = firstName+' '+lastName
		appendInToCSVFile.write(studentName)
		appendInToCSVFile.write(delimiter)
		studentGender = random.choice(['Male','Female'])
		appendInToCSVFile.write(studentGender)
		appendInToCSVFile.write(delimiter)
		studentDepartment = random.choice(['CSE',numpy.nan])
		appendInToCSVFile.write(str(studentDepartment))
		appendInToCSVFile.write(delimiter)
		CGPA = round((random.uniform(5.00,10.00)),2)
		studentCGPA = random.choice([CGPA,numpy.nan])
		appendInToCSVFile.write(str(studentCGPA))
		appendInToCSVFile.write('\n')
		ID+=1

