import pandas
#For Fabricated DataSet
#myDataFrame = pandas.read_csv('F:\KITS-Guntur\Session-3\KITS-Full-DataSet.csv')
#print(myDataFrame.groupby('STUDENT_DEPARTMENT').size())

#For real dataset
myDataFrame = pandas.read_csv('winequality-red.csv',sep=';')
print(myDataFrame.groupby('quality').size())

