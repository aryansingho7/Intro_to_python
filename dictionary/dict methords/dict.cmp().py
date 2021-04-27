#py program to demostrate working og 
#str() and item()

#initializing dictionary
dic ={'name':'aryan', 'age':19}

#using str() to display dic as string
print('the dict in string:'+ str(dic))

#usingh str() to display dic as list
print('the consituents of dicitoanry as lsit are:')
print(dic.items())


#py program to dmeons working of 
#len() type()

dic ={ 'name':'aryan','age':19,'id':2001}

li = [1,3,5,6]

#using len() to display dic size
print('the size of dic is:', end='')
print(len(dic))

#using len() to display dic size
print('the data type of dic is:', end='')
print(type(dic))

#using type() to display data type
print('the data type of li is:', end="")
print(type(li))

#py code to demons working of clear() and copy()


dic1={'name':'aryan', 'age':20}

dic3={}

#using copy() to make shallow copy of dictioanry
dic3=dic1.copy()

#printing the new directory 
print('new directory dic3:' )
print(dic3.items())

#clearing the dictionary
dic1.clear()

#printing the cleared dictionary
print('the contents of deleted dictioanry is:', end='')
print(dic1.items())