'''
#for rescaling the data
import pandas, scipy, numpy
#pip install scikit-learn
from sklearn.preprocessing import MinMaxScaler
#code for rescaling the data
myDataFrame=pandas.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv',sep=';')
print(myDataFrame.shape)
MyDataDescription = myDataFrame.describe()
print(MyDataDescription)

array=myDataFrame.values
#Seperating data into input and output components
x=array[:,0:8]
y=array[:,8]
#defining the scaler
scaler=MinMaxScaler(feature_range=(0,1))
print(scaler)
print(type(scaler))

rescaledX=scaler.fit_transform(x)
numpy.set_printoptions(precision=2) #Setting precision for the output
print(rescaledX[0:10,:])
'''
'''
#for standardizing the data
import pandas, scipy, numpy
from sklearn.preprocessing import StandardScaler
df = pandas.read_csv('winequality-red.csv',sep=';')
#df=pandas.read_csv( 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ',sep=';')
array=df.values
#Separating data into input and output components
x=array[:,0:8]  
y=array[:,8]

#code for standardizing the data
scaler=StandardScaler().fit(x)
print(scaler)
print(type(scaler))
rescaledX=scaler.transform(x)
print(rescaledX[0:5,:])
'''
'''
#for normalizing the data
import pandas, scipy, numpy
from sklearn.preprocessing import Normalizer
df = pandas.read_csv('winequality-red.csv',sep=';')
#df=pandas.read_csv( 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ',sep=';')
array=df.values
#Separating data into input and output components
x=array[:,0:8]
y=array[:,8]

#code for normalizing the data
scaler=Normalizer().fit(x)
normalizedX=scaler.transform(x)
print(normalizedX[0:5,:])
'''
'''
#for binarizing the data
import pandas, scipy, numpy
from sklearn.preprocessing import Binarizer

df=pandas.read_csv( 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ',sep=';')
array=df.values
#Separating data into input and output components
x=array[:,0:8]
y=array[:,8]

#code for binarizing the data
binarizer=Binarizer(threshold=0.5).fit(x)
binaryX=binarizer.transform(x)
print(binaryX[0:5,:])
'''
'''
#for mean removal
import pandas, scipy, numpy
from sklearn.preprocessing import scale

df=pandas.read_csv( 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ',sep=';')
array=df.values
#Separating data into input and output components
x=array[:,0:8]
y=array[:,8]

#code for mean removal
data_standardized=scale(df)
print(data_standardized.mean(axis=0))
print(data_standardized.std(axis=0))
'''
'''
#for One Hot Encoding
from sklearn.preprocessing import OneHotEncoder

#code for One Hot Encoding
encoder=OneHotEncoder()
encoder.fit([[0,2,1,2],
[1,3,5,3],
[2,3,2,12],
[1,2,4,3]
])
print(encoder)
encoder_vector = encoder.transform([[2,3,5,3]]).toarray()
print(encoder_vector)
'''

#Label Encoding
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
input_classes = ['suzuki', 'ford', 'suzuki', 'toyota', 'ford', 'bmw']
label_encoder.fit(input_classes)
print("\nClass mapping:  ")
for i, item in enumerate(label_encoder.classes_):
   print(item,'-->', i)

labels = ['toyota', 'ford','bmw','suzuki']
encoded_labels = label_encoder.transform(labels)
print("\nLabels =", labels)
print("Encoded labels =", list(encoded_labels))

encoded_labels = [3, 2, 0, 2, 1]
decoded_labels = label_encoder.inverse_transform(encoded_labels)
print("\nEncoded labels =", encoded_labels)
print("Decoded labels =", list(decoded_labels))
