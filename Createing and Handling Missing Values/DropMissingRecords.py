#Creating a data frame from CSV file
import pandas
#reading the data from a csv file using read_csv() method
MyDataFrame = pandas.read_csv('KITS-MissingValuesDataSet.csv')

#Displaying the number of records in the dataframe
Total_Rows_Columns = MyDataFrame.shape
print('\nThe Total number of instances are:',Total_Rows_Columns[0])
print('Actual DataFrame\n',MyDataFrame)

#Drop the records if atleast one missing value in any attribute
UpdatedMyDataFrame = MyDataFrame.dropna(axis=0,how='any')
print('Updated DataFrame\n',UpdatedMyDataFrame)

'''
#extracting the missing values in the attribute Department
DeptMissingValueRecords = pandas.isnull(MyDataFrame['DEPARTMENT'])
Total_Rows_Dept_Missing = MyDataFrame[DeptMissingValueRecords].shape
print('\nNumber of records where Department is missing:',Total_Rows_Dept_Missing[0])
'''
'''
#Displaying individual elements in the shape tuple
Total_Rows_Columns = MyDataFrame.shape
print('\nThe Total number of instances are:',Total_Rows_Columns[0])
print('The Total number of attributes are:',Total_Rows_Columns[1])
print('Actual DataFrame\n',MyDataFrame)
'''


'''
UpdatedMyDataFrame = MyDataFrame.dropna(axis=1)
Total_Rows_Columns = UpdatedMyDataFrame.shape
print('\nIn Updated Dataframe the Total number of instances are:',Total_Rows_Columns[0])
print('In Updated Dataframe the Total number of attributes are:',Total_Rows_Columns[1])
print('Updated DataFrame\n',UpdatedMyDataFrame)
'''
'''
#extracting the missing values in the attribute Department
DeptMissingValueRecords = pandas.isnull(MyDataFrame['DEPARTMENT'])
Total_Rows_Dept_Missing = MyDataFrame[DeptMissingValueRecords].shape
print('\nNumber of records where Department is missing:',Total_Rows_Dept_Missing[0])

#extracting the missing values in the attribute CGPA
CGPAMissingValueRecords = pandas.isnull(MyDataFrame['CGPA'])
Total_Rows_CGPA_Missing = MyDataFrame[CGPAMissingValueRecords].shape
print('\nNumber of records where CGPA is missing: ',Total_Rows_CGPA_Missing[0])
'''
'''
#Drop the records where atleast one missing value is present either in Department or CGPA
UpdatedMyDataFrame = MyDataFrame.dropna()
UpdatedTotalRecords = UpdatedMyDataFrame.shape
print('\nTotal records after Dropping the records with missing values:',UpdatedTotalRecords[0])
print('The Total number of attributes are:',UpdatedTotalRecords[1])
'''

'''
print(MyDataFrame)
print(UpdatedMyDataFrame)

#Drop the record if all the values in the record are missing
UpdatedMyDataFrame = MyDataFrame.dropna(how='all')

#Drop the column if atleast one missing value is present
UpdatedMyDataFrame = MyDataFrame.dropna(axis=1)
print(UpdatedMyDataFrame)
'''


