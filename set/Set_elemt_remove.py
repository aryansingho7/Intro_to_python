#python program to dm=emostrate 
#deleation of elements in a set

set1= set([1,2,3,4,5,6,7,8,9,10,11])

#usinf remove() methord
set1.remove(5)
set1.remove(6)
print(set1)

#using discard()
set1.discard(8)
set1.discard(9)
print(set1)

#using the pop() 
set1.pop()
print(set1)

#using clear()
set1.clear()
print(set1)

