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



#code 2
#demosn  the working of the pop()without key

#initialization of dict
test_dict={'nikhil':7,'akshat':1,'akash':2}
#printing the initial dict
print('dict before deletion:' +str(test_dict))

#using pop to return and remove key value pair

pop_ele=test_dict.pop('manjeet',4)

#printing the value asociated to popped key 
print('value aossicated to popped key is: '+ str(pop_ele))

#using pop to return and remove key value pair
#not providing default
pop_ele= test_dict.pop('manjeet')

#printing th evalue associated to popped key 
#key error

print('value associated to popped key is:' + str(pop))

