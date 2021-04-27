#python code to explin the type() func

#class of type dict
class DictType:
    Dictnumber={1:'aryan',2:'ryan',3:'yan',4:'an'}

#class of list
class ListType:
    ListNumber=[1,2,3,4,5]

#creating objects of each class
d= DictType()
l =ListType()

#will print accordingly whether both the obejcts
#are of same type or not
if type(d)is not type(l):
    print('both class have diffrent object type.')
else:
    print('same object type')


#code 4
#python program to demostrate type(name,bases, dict)

#new class(has no base) class with the 
#dynamic class initialization of type()
new= type('new',(object, ),
    dict(var='geeksforgeeks',b=2009))

    #print type() which reutrns class type()
print(type(new))
print(type(vars))

#base class, incorporated 
#in our new class
class test:
    a= 'geeksforgeeks'
    b= 2009

#dynamically intialize newer class 
#it will derive from the base class test
newer= type('newer', (test, ),
    dict(a='geeks',b=2018))

print(type(newer))
print(vars(newer))