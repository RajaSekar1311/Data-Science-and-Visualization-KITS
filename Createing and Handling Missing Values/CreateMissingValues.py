#Code for creating some missing values using numpy ndarray 
import pandas
import numpy

MyDataFrame = pandas.DataFrame(numpy.random.randn(5,3),
			  index = ['a','c','e','f','h'], 
			  columns = ['One','Two','Three'])

print('\nActual DataFrame:\n',MyDataFrame)


UpdatedDataFrame = MyDataFrame.reindex(['a','b','c','d','e','f','g','h'])
print('\nUpdated DataFrame:\n',UpdatedDataFrame)


'''
UpdatedMyDataFrame = MyDataFrame.dropna(how='all')
print('\n\nUpdated Dataframe after dropping the records with all missing values\n',UpdatedMyDataFrame)
'''


