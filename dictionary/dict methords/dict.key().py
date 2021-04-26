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

exit()


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

exit()