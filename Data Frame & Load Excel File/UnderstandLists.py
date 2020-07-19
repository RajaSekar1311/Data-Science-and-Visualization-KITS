#Creating an empty list
myList = []
print(myList)
print(type(myList))
#Group of similar data type elements
myList1 = [1,2,3,4,5]
print(myList1)
print(type(myList1))
#Group of different data type elements
myList2 = [1,2,3,4.56,'Python']
print(myList2)
print(type(myList2))
for element in myList2:
	print(element)
	print(type(element))
#List is mutable, means the size of the list can be changed in execution time
del(myList2[3])
print(myList2)




'''
myList2 = [1,2,3,4,5]
#Python Style of writing a loop
for element in myList2:
	print(element)
	print(type(element))

#C language
int a[5] = {1,2,3,4,5}
int i;
for(i=0;i<5;i++)
{
   printf("%d",a[i])
}
'''












