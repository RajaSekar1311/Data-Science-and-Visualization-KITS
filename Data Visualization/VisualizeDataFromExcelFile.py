import pandas
import matplotlib.pyplot as myPlot

myFileName = 'F:\KITS-Guntur\Session-2\Session2-KITS-Guntur-DataSet.xls'

#with is a context manager here
with pandas.ExcelFile(myFileName) as myExcelFileReadObject:
	#invoke the read_excel method from pandas library with the fileobject and the name of the sheet in the excel workbook
	myDataFrame1 = pandas.read_excel(myExcelFileReadObject,'Sem1-Marks')
	myDataFrame2 = pandas.read_excel(myExcelFileReadObject,'Sem2-Marks')
	#print(myDataFrame1)
	#print(myDataFrame2)
	myDataFrame1.hist()
	myPlot.show()
	myDataFrame2.hist()
	myPlot.show()
	




