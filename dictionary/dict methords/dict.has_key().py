#example1
#python program to show the working 
#of has_key() methord in the dictionary

#dictionary with three items
Dict1={'a':'geeks','b':'for','c':'geeks'}

#printing the initial dictionary
print('intial dictionary:')
print(Dict1)

#use of has key fucntion in the dictionary
print(Dict1.has_key('a'))
print(Dict1.has_key('for'))

#example2

#python program to show the working of 
#has_key methord in dictionary\

#dictonary with three elements
Dict2={1:'welcome',2:'to',3:'geeks'}

#dictonary to be checked 
print('orignial dictionary:')
print(Dict2)

#use of has key() to check the cetain element
print(Dict2.has_key(3))
print(Dict2.has_key('to'))


#python program to search a ey in the dictionary 
#using operator

dictonary={1:'geeks',2:'for',3:'geeks'}

print('original dictionary:'.format(dictonary))

#return true if present
if 1 in dictonary:
    print(dictonary[1])
    else:
        print('{} is absent'.format(1))

#return false is not present

if 5 in dictonary.key():
    print(dictonary[5])
    else:
        print("{} is absent:.format(5))

