#addition of elements in a list

#creating a list
list=[]
print('initial list:')
print(list)

#addition of element
list.append(1)
list.append(2)
list.append(4)
print('Updated list:')
print(list)

#adding  elements to list using iterator
for i in range(1,4):
    list.append(i)
    print('List after addition of elemnets from 1-3')
    print(list)
    
#adding tuples to the list
list.append((5,6))
print('list after addition of a tuple:')
print(list)

#addition of list to a list
list2=['for', 'geeks']
list.append(list2)
print('list after additon of a list')
print(list)
    