import pandas
myCSVFileName = input('Enter a CSV Filename: ')
myDataFrame = pandas.read_csv(myCSVFileName)
print(myDataFrame)
