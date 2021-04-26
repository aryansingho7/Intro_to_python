#py program to show the working of item()
#methord in dictionary

#dictionary with three items
Dict1={'a':'geeks','b':4,'c':'geeks'}

print('dictionary items:')

print(Dict1.items())


#example2
#python program to show the working of 
#item methord in dictionary 

#dictionary with 3 items
Dict1:{'a':'geeks','b':4,'c':'geeks'}

print('original dict:')

print(Dict1.items())

items=Dict1.items()
#now printing all items of a dictionary
print(items)

#delet an iteam from dictionary
del[Dict1['c']]
print('dictionary affter deletion:')
print(items)