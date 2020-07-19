import pandas

myFileName = 'Session2-KITS-Guntur-DataSet.xls'

#with is a context manager here
# group of instructions will be exexuted in a particular context
#In pandas there is a method called as ExcelFile()
#ExcelFile() method opens a excel file
#With opening the file in read mode perform lines 11 to 15
with pandas.ExcelFile(myFileName) as myExcelFileReadObject:
	#invoke the read_excel method from pandas library with the file read object and the name of the sheet in the excel workbook
	myDataFrame1 = pandas.read_excel(myExcelFileReadObject,'Sem1-Marks')
	myDataFrame2 = pandas.read_excel(myExcelFileReadObject,'Sem2-Marks')
	print(myDataFrame1)
	print(myDataFrame2)
	#if more values are there in the dataframe, only the first and last 5 records
	
	

	




