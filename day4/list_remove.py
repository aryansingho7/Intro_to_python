#using remove methord
#creating a list
list=[1,2,3,4,5,6,7,8,9,10,11,12]
print('initial list:')
print(list)

#remove elemnet using remove methord
list.remove(5)
list.remove(6)
print('Updated list:')
print(list)

#removing using iterator methord
for i in range(1,5):
    list.remove(i)
print('second updated list:')
print(list)


