import pandas
import numpy

#defining a dictionary with Lists
MyDictData = {'First Semester Marks':[97, 83, numpy.nan, 95], 
		'Second Semester Marks': [85, 45, 56, numpy.nan], 
		'Third Semester Marks':[numpy.nan, 40, 80, 98]} 

#creating a dataframe from the dictionary
MyDataFrame = pandas.DataFrame(MyDictData, index = ['Rajesh', 'Manish', 'Shankar', 'Vinay'])

print('\nThe DataFrame is:\n\n',MyDataFrame)

#print('\n\nChecking the existence of missing values by invoking isnull():\n\n',MyDataFrame.isnull())


