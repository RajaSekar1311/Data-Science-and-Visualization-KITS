import csv
import os
import random
import names
delimiter = ','


myCSVFileName = input('Enter a CSV Filename: ')

fileExists = os.path.isfile(myCSVFileName) 
if not fileExists:
	print(myCSVFileName, 'does not exist')
else:
	print(myCSVFileName, 'exist')


#Lines 14 to 20 are for writing a Header 
#lines 23 to end are writing student data in the file
#Open the CSV File in append mode for creating Users details 
#with is a Context Manager
#with open the csv file in append mode perform the steps below
with open(myCSVFileName,'a',newline='') as appendInToCSVFile:
	#Defining a list of elements in the Header
	csvHeaderList = ['REGISTRATION_NUMBER','STUDENT_NAME','STUDENT_GENDER','STUDENT_DEPARTMENT','STUDENT_CGPA','STUDENT_EMAILID','STUDENT_CONTACT_NUMBER']
	MyHeader = csv.DictWriter(appendInToCSVFile,fieldnames=csvHeaderList)
	print(MyHeader)#It is a Dictionary Writer Object
	if not fileExists:
		MyHeader.writeheader()#writes the header in the CSV File
	#Loop starts with ID value as 1 and loop ends when ID > 5000
	#Loop will iterate from 1 to 5000
	
	ID = 1
	while (ID <= 100):
		studentId = ID
		#write() method writes in to a file with an file object
		#write method can write only strings but not integers, floating point etc
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
		studentDepartment = random.choice(['CSE','ECE','EEE','Mechanical','Civil','EIE'])
		appendInToCSVFile.write(studentDepartment)
		appendInToCSVFile.write(delimiter)
		studentCGPA = round(random.uniform(5.00,10.00),2)
		appendInToCSVFile.write(str(studentCGPA))
		appendInToCSVFile.write(delimiter)
		emailTag = random.choice(['@gmail.com','@yahoo.co.in','@rediffmail.com','@hotmail.com'])
		studentEmailId = firstName+lastName+emailTag
		appendInToCSVFile.write(studentEmailId)
		appendInToCSVFile.write(delimiter)
		studentContactNum = random.randint(9986000000,9986999999)
		appendInToCSVFile.write(str(studentContactNum))
		#record is completed, so do not write demiliter i.e., comma
		#instead of comma, introduce a new line '\n'
		appendInToCSVFile.write('\n')
		ID+=1 #ID = ID + 1
