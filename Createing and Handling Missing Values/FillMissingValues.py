'''
#Creating a data frame from CSV file
import pandas
import numpy

#reading the data from a csv file using read_csv() method
MyDataFrame = pandas.read_csv('KITS-MissingValuesDataSet.csv')
print(MyDataFrame)



print(UpdatedDataFrame)
'''

'''
#Creating a data frame from CSV file
import pandas
import numpy

#reading the data from a csv file using read_csv() method
MyDataFrame = pandas.read_csv('MissingValues_GCET_Dataset.csv')
print(MyDataFrame)


UpdatedDataFrame=MyDataFrame.interpolate(method ='linear', limit_direction ='forward')
print(UpdatedDataFrame)
'''

import pandas
import numpy
MyDataFrame = pandas.DataFrame(numpy.random.randn(5,3),
			  index = ['a','c','e','f','h'], 
			  columns = ['One','Two','Three'])

MyDataFrame = MyDataFrame.reindex(['a','b','c','d','e','f','g','h'])
print('\nActual DataFrame:\n',MyDataFrame)

UpdatedDataFrame=MyDataFrame.interpolate(method ='linear', limit_direction ='forward')
print(UpdatedDataFrame)



'''


#reading the data from a csv file using read_csv() method
#MyDataFrame = pandas.read_csv('StudentDataWithMissingValues.csv')

#UpdatedDataFrame = MyDataFrame.fillna(0)
#UpdatedDataFrame = MyDataFrame.fillna(method='pad')
#UpdatedDataFrame = MyDataFrame.fillna(method='bfill')
#UpdatedDataFrame = MyDataFrame['DEPARTMENT'].fillna('CSE',inplace = False)
#UpdatedDataFrame = MyDataFrame.replace(numpy.nan, value = -999)
#UpdatedDataFrame=MyDataFrame.interpolate(method ='linear', limit_direction ='forward')
'''