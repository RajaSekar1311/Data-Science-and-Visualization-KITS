'''
#From Fabricated DataSet
import pandas
import matplotlib.pyplot as plt
#create the dataframe from CSV file using pandas
myDataFrame=pandas.read_csv('KITS-Guntur-Session5-Student-Marks.csv')
#myDataFrameint(myDataFrame.describe())
#Representation of data as a histogram from all attributes
myDataFrame.hist()
#Representation of data as a histogram from individual attributes
myDataFrame['English'].hist()
#For displaying the plot
#matplotlib.pylot.show()
plt.show()
'''
'''
import pandas
import matplotlib.pyplot as plt
#create the dataframe from CSV file using pandas
myDataFrame=pandas.read_csv('winequality-red.csv',sep=';')
#Representation of data as a histogram
myDataFrame.hist()
plt.show()
#Plotting individual attributes
myDataFrame['quality'].hist()
#For displaying the plot
plt.show()
'''
'''
#sharex and sharey are for x and y co-ordinates
import pandas
import matplotlib.pyplot as plt
#create the dataframe from CSV file using pandas
myDataFrame=pandas.read_csv('winequality-red.csv',sep=';')
#Representation of data as a density plots
myDataFrame.plot(kind='density',subplots=True,sharex=False)
#For displaying the plot
plt.show()
'''
'''
import pandas
import matplotlib.pyplot as plt
#create the dataframe from CSV file using pandas
df=pandas.read_csv('F:\DataScienceFoundations\Data-Visualization\winequality-red.csv',sep=';')
#Representation of data as a Box plots
df.plot(kind='box',subplots=True,sharex=False,sharey=False)
#For displaying the plot
plt.show()
'''
'''
import pandas, numpy
import matplotlib.pyplot as plt
#create the dataframe from CSV file using pandas
myDataFrame=pandas.read_csv('F:\DataScienceFoundations\Data-Visualization\winequality-red.csv',sep=';')
#Representation of data as a Correlation Matrix Plot
correlationsMatrix=myDataFrame.corr()
#creating a figure object
fig=plt.figure()
#Adding sub plots by making use of grid layout 111 
ax=fig.add_subplot(111)
cax=ax.matshow(correlationsMatrix,vmin=-1,vmax=1)
fig.colorbar(cax)
ticks=numpy.arange(0,12,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
#For displaying the plot
plt.show()
'''
'''
import pandas
import seaborn
import matplotlib.pyplot as plt
#create the dataframe from CSV file using pandas
myDataFrame=pandas.read_csv('F:\DataScienceFoundations\Data-Visualization\winequality-red.csv',sep=';')
#Creation of Correlation Martix
correlationsMatrix=myDataFrame.corr()
#print(correlationsMatrix)
#Representation of data as a Correlation Matrix plot
seaborn.heatmap(correlationsMatrix,annot=True)
plt.show()
'''
'''
import matplotlib.pyplot as plt
girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(grades_range, girls_grades, color='r')
ax.scatter(grades_range, boys_grades, color='b')
ax.set_xlabel('Grades Range')
ax.set_ylabel('Grades Scored')
ax.set_title('scatter plot')
plt.show()
'''
'''
import pandas
import matplotlib.pyplot as plt
#create the dataframe from CSV file using pandas
myDataFrame=pandas.read_csv('F:\DataScienceFoundations\Data-Visualization\winequality-red.csv',sep=';')
#Representation of data as a Scatteredplot
pandas.plotting.scatter_matrix(myDataFrame)
plt.show()
'''

