#initial dict
Dict={5:'welcome',6: 'to',7:'geeks',
    'A':{1:'Geeks',2:'for',3:'geeks'},
    'B':{1:'geeks',2:'life'}}

print('Intitial dictionary:')
print(Dict)

#deletinf a key value
del Dict[6]
print('\n deleting a specific key:')
print(Dict)

#deleting a key form
#nested dictionary 
del Dict['A'][2]
print('\n deleting a key from the nested dictionary')
print(Dict)


#Using Pop methord
#creating a dict
Dict={1:'geeks',"name":'for',3:'geeks'}

#deleting a key 
#using a pop() mehtord

pop_ele= Dict.pop(1)
print('\nDict after deletion:'+str(Dict))
print('value associated to poped key is:' + str(pop_ele))



#using popitem()
#creating  dictionary
Dict={1:'geek','name':'for',3:'geeks'}

#delting an abitary key using popitem() fucntion
pop_ele= Dict.popitem()
print('\n Dictionary after deletion:' + str(Dict))
print('The arbitrary pair returned is:'+ str(pop_ele))

#using clear methord
#creating a dictionary
Dict={1:'geeks','name':'for',3:'geeks'}

#delete entire dictionary
Dict.clear()
print('dict after clear function:')
print(Dict)