'''
import pandas

ids = [1, 2, 3, 4, 5, 6, 7]
place = ['Spain', 'France', 'India', 'Germany', 'Nepal','Bangladesh','Srilanka']


df = pandas.DataFrame(list(zip(ids, place)),      
                  columns=['Ids', 'Place'])
				  
print(df)

y = pandas.get_dummies(df.Place, prefix='Place')
print(y)

'''
import pandas

ids = [11, 22, 33, 44, 55, 66, 77]
countries = ['Spain', 'France', 'Spain', 'Germany', 'France']

df = pandas.DataFrame(list(zip(ids, countries)),      
                  columns=['Ids', 'Countries'])

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
y = LabelBinarizer().fit_transform(df.Countries)
print(y)

x = [[11, "Spain"], [22, "France"], [33, "Spain"], [44, "Germany"], [55, "France"]]
y = OneHotEncoder().fit_transform(x).toarray()
print(y)

