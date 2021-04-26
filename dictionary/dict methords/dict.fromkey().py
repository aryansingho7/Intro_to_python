#py program to demostrate
# the working of fromkeys()

#initializing a sequence 
seq={'a','b','c','d','e'}

#using from key sequence to dict
#initializing with none
res_dict=dict.fromkeys(seq)

#printing th created dict
print('the newly created dict wiht none values:'+str(res_dict))

#using the fromkeys() to convert sequence to ddict
res_dict=dict.fromkeys(seq,1)

#printing the newly created dict 
print('the newly created dict with 1 as value:' +str(res_dict))


#code 2
#python 3 code to demostrate behaviour
# with mutable objects

#initializing sequence and list
seq={'a','b','c','d','e'}
list1=[2,3,]

#using fromkeys() to convert sequence to dict
#using conventional methord
res_dict=dict.fromkeys(seq,list1)

#printing create dict
print('the newly created dict with lsit value:'+str(res_dict))


#appendig the list
list1.append(4)

#printing the list after appending it
#notice that append take place in all values
print('the dict with list values after appending:'+str(res_dict))

list1=[2,3]
print('\n')



#usinf fromkeys() to convert sequence to dict
#using dict. comprehension
res_dict2={key:list(list1) for key in seq}

#printing the created dict
print('the new;y created dict with list values:'+ str(res_dict2))
#appending to list1
list1.append(4)

#printing dict after appen doesnt take place now
print('the dict with list values after appending (no chnage):'+str(res_dict))