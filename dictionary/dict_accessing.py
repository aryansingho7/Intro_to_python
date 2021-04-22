#python program to demon 
#accessing a elemnt from a dictionary

#creating a dict
Dict={1:'geeks', 'name':'for', 3:'geeks'}

#accessing elemnt using key
print('accessing a elent using key:')
print(Dict['name'])

#accessing element using key
print('accessing an element using key:')
print(Dict[1])


#accessing using get()

Dict={1:'geeks', 'name':'for', 3:'geeks'}

#accesing the ement using get()
print('accessing elemnt using get():')
print(Dict.get(3))


#accessing element of a nested dictionary
Dict ={'Dict1': {1:'geek'}, 'Dict2':{'name':'for'}}

#accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['name'])