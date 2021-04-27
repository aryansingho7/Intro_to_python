#pythone simple code to explane the type() func\
print(type([]) is list)

print(type([])is not list)

print(type(()) is tuple)

print(type({}) is dict)

print(type({}) is not list)

#python 3 code to expain the type() fucntion
#class of type dict
# Class of type dict
class DictType:
    Dictnumber={1:'aryan',2:'ryan',3:'yan',4:'an'}
      
    # Will print the object type
    # of existing class
    print(type(Dictnumber))
#will print thr oject type of existing class
print(type(Dictnumber))

#class of type list
class ListType:
    ListNumber=[1,2,3,4,5]

    print(type(ListNumber))

#class type of tuple
class TupleType:
    TupleNumber=('geeks','for','geeks')

    print(type(TupleNumber))


#creating object of each class
d= DictType
l= ListType
t= TupleType
