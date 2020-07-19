import random
def get_full_name():
	first_name = get_first_name()
	last_name = get_last_name()
	return(first_name+' '+last_name)

def get_first_name():
	first_name = random.choice(['Diyaan','Shubham','Manohar','Abhigyan','Nirmal','Viswanath','Kalyan','Dheeraj','Mahendra','Prakash','Ashok','Arnab','Ajay','Sujay','Nischal','Nihal','Raju','Rahul','Ashok','Shraddha','Anand','Ravi','Vinay','Manoj','Shaswath','Vamsi'])
	return first_name

def get_last_name():
	last_name = random.choice(['Kumar','Sinha','Agarwwal','Sharma','Ranjan','Das','Kishan','Dubey','Dey','Varma','Sarkar','Goswami','Saroj','Reddy','Gupta','Meena'])
	return last_name
	
with open('MyCustomizedNames.txt','w') as fileAppendObj:
	for name in range(1,2001):
		fullName = get_full_name()
		fileAppendObj.write(fullName)
		fileAppendObj.write('\n')
	