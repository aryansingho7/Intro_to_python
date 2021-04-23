#py program to oshow the working of the update() func
#example 1
# following teo dictionary
Dict1={'geeks':1,'for':2}
Dict2={'geek':2}

#printing the original dict
print('original  dictionary:', Dict1)

#updation
Dict1.update(Dict2)
print('dictionary after updation:', Dict1)


#example 2
#updation with iterable
#dictionary with single item
Dict1={'a':'geeks'}

#dictionary before updation
print('original dict:', Dict1)

#updation with iterable\
Dict1.update(b='aryan',c='yan')
print('updated final dict:', Dict1)