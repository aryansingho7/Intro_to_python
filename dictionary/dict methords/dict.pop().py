#python program to demons working of pop()

#initialization dictionary
test_dict={'aryan':7, 'ryan':1, 'yan':2}

#printing intitial dict
print('the dict before the deletion:' + str(test_dict))

#using the pop to return adn remove key value pair
pop_ele=test_dict.pop('yan')

#printing the valure associated to popped key
print('value assiciated to poped key is:'+str(pop_ele))

#printing dictionary after deletion 
print('dictionary after deletion is:' +str(test_dict))