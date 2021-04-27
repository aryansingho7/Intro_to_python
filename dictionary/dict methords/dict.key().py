#py program to show working 
#of key in dictionary

#dict with the 3 keys
Dict={'a':'geeks','b':'for','c':'geeks'}

#printing keys of dict
print(Dict.keys())

#creating empty Dict
empty_Dict1={}

#print keys of empty dictionary
print(empty_Dict1.keys())



# Python program to show updation
# of keys in Dictionary

#dictionary with two keys
Dict1={'a':'geeks','b':'for'}

#printing keys of dictionary
print('key before dictionary updation:')
keys= Dict1.keys()
print(keys)

#adding an element to the dictionary 

Dict1.update({'c':'geeks'})

print('\n After dictionary is updated')
print(keys)



# Python program to demonstrate
# working of keys()

#initialising dictionary
test_dict={'geeks':7,'for':1,'geeks':2}

#accesing 2nfd element using naive methord
#using loop
j=0
for i in test_dict:
    if(j==1):
        print('2nd key using loop:'+1)
        j=j+1


#accesing the 2nd elemnt using keys()
print('2nd key using keys():'+ test_dict.keys()[1])