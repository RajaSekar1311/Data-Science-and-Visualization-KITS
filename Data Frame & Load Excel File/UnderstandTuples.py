#Creating an empty tuple
myTuple = ()
print(myTuple)
print(type(myTuple))
#Group of similar data type elements
myTuple1 = (1,2,3,4,5)
print(myTuple1)
print(type(myTuple1))
#Group of different data type elements
myTuple2 = (1,2,3,4.56,'Python')
print(myTuple2)
print(type(myTuple2))
for element in myTuple2:
	print(element)
	print(type(element))
#Tuple is immutable, means the size of the tuple cannot be changed in execution time
del(myTuple2[3])
print(myTuple2)