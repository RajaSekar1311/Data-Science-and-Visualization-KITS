'''
#creating an empty dataframe
import pandas
MyDataFrame = pandas.DataFrame()
print(MyDataFrame)
print(type(MyDataFrame))
'''
'''
#creating a dataframe from a List
import pandas
MyListData = [1,2,3,4,5]
MyDataFrame = pandas.DataFrame(MyListData)
print(MyDataFrame)
'''
'''
#creating a dataframe from List of Lists
import pandas
MyListData = [['Nischal',7],['Nihal',5],['Nihaan',1],['Diyaan',6]]
MyDataFrame = pandas.DataFrame(MyListData,columns=['Name','Age'])
print(MyDataFrame)
'''
'''
#creating a dataframe from Dictionary of ndarrays or Lists
#All the ndarrays must be of same length. 
#If index is passed, then the length of the index should equal to the length of the arrays.
#If no index is passed, then by default, index will be range(n), where n is the array length.
#Note − Observe the values 0,1,2,3. They are the default index assigned to each using the function range(n).
import pandas
MyDictData = {'Name':['Nishcal', 'Nihal', 'Nihaan', 'Shubham'],'Age':[7,5,1,4]}
print(MyDictData)
print(type(MyDictData))
MyDataFrame = pandas.DataFrame(MyDictData)
print(type(MyDataFrame))
print ("\n",MyDataFrame)
'''
#Creating an Indexed dataframe (Labelled rows)
import pandas
MyDictData = {'Name':['Durgesh','Indrasen', 'Chandan Pandey', 'Premchand'],'CGPA':[9.83,9.79,9.62,7.25]}
#the index parameter assigns an index to each row
MyDataFrame = pandas.DataFrame(MyDictData,index=['Rank1','Rank2','Rank3','Rank4'])
print ("\n",MyDataFrame)
	















