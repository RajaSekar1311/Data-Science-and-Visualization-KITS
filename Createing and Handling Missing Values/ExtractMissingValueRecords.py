#Creating a data frame from CSV file
import pandas
#reading the data from a csv file using read_csv() method
MyDataFrame = pandas.read_csv('KITS-MissingValuesDataSet.csv')
print(MyDataFrame)
Total_Rows_Columns = MyDataFrame.shape
#Displaying the shape tuple
print('\nThe dimensions of the data set are: ',Total_Rows_Columns)
#Displaying individual elements in the shape tuple
print('\n\nThe Total number of instances are:',Total_Rows_Columns[0])
print('The Total number of attributes are:',Total_Rows_Columns[1])
#extracting the missing values in the attribute CGPA
CGPAMissingValueRecords = pandas.isnull(MyDataFrame['CGPA'])
Total_Rows_CGPA_Missing = MyDataFrame[CGPAMissingValueRecords].shape
print('\nNumber of records where CGPA is missing: ',Total_Rows_CGPA_Missing[0])
print('The fisrt fifteen instances of the dataset where CGPA values are missing:')
print(MyDataFrame[CGPAMissingValueRecords].head(15))

