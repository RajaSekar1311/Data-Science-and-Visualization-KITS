import pandas

myFileName = 'Session2-KITS-Guntur-DataSet.xls'

with pandas.ExcelFile(myFileName) as myExcelFileReadObject:

	myDataFrame1 = pandas.read_excel(myExcelFileReadObject,'Sem1-Marks')
	myDataFrame2 = pandas.read_excel(myExcelFileReadObject,'Sem2-Marks')

	#print(myDataFrame1.describe())
	#print(myDataFrame2.describe())
	#print(myDataFrame1.head(6))
	#print(myDataFrame2.head(6))
	DF1TotalRowsCols = myDataFrame1.shape
	print(DF1TotalRowsCols)
	print(DF1TotalRowsCols[0])
	print(DF1TotalRowsCols[1])
	
	DF2TotalRowsCols = myDataFrame1.shape
	print(DF2TotalRowsCols)
	print(DF2TotalRowsCols[0])
	print(DF2TotalRowsCols[1])