import xlwt
import os
import random

myExcelFileName = input('Enter the filename:  ')
fileExists = os.path.isfile(myExcelFileName)
#If filename entered by the user is not available then only if condition will be true
if not fileExists:
	#Create a excel workbook
	myWorkBook = xlwt.Workbook()
	mySheet1 = myWorkBook.add_sheet('Sem1-Marks')
	mySheet1.write(0,0,'Maths')
	mySheet1.write(0,1,'Science')
	mySheet1.write(0,2,'Social')
	mySheet2 = myWorkBook.add_sheet('Sem2-Marks')
	mySheet2.write(0,0,'English')
	mySheet2.write(0,1,'Hindi')
	mySheet2.write(0,2,'Sanskrit')
	
	#Outer loop starts from i = 1 and ends at i = (2001-1) = 2000
	for i in range (1,2001):#Outer for loop is for row range(a,n-1)
		#inner loop will start from j = 0 and ends at j = (3-1) = 2
		for j in range(0,3):#Inner for loop is for column
			marks = random.randint(0,100)
			mySheet1.write(i,j,marks)
			
	for i in range (1,2001):
		for j in range(0,3):
			marks = random.randint(0,100)
			mySheet2.write(i,j,marks)			
			
myWorkBook.save(myExcelFileName)



