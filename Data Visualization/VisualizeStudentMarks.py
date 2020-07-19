import pandas
import matplotlib.pyplot as plt
#create the dataframe from CSV file using pandas
MyDataFrame=pandas.read_csv('ZPHighSchoolGuntur.csv')
print(MyDataFrame.shape)
print(MyDataFrame.describe())
'''
#Representation of data as a histogram
MyDataFrame.hist()
#For displaying the plot
plt.show()
'''
#Representaion of data as desnsity plot
MyDataFrame.plot(kind='density',subplots=False)
#For displaying the plot
plt.show()

'''
#Representation of data as a Box plots
MyDataFrame.plot(kind='box',subplots=True,sharex=False,sharey=False)
#For displaying the plot
plt.show()
'''
'''
import pandas
import seaborn
import matplotlib.pyplot as plt
#create the dataframe from CSV file using pandas
df=pandas.read_csv('StudentMarksDataSet.csv')
#Representation of data as a Correlation Matrix plot
correlationsMatrix=df.corr()
#print(correlationsMatrix)
seaborn.heatmap(correlationsMatrix, annot=True)
plt.show()
'''