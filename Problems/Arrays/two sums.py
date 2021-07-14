arr1= [1,3,5,7]
target1= 8

arr2=[1,8,9,3]
target2= 5

def two_sum(arr, target):
    values= dict()
    for i, elem in enumerate(arr):
        comp=target-elem
        if comp in values:
            return [values[comp],i]
        values[elem]=i
    return[]

list1= two_sum(arr1,target1)
print(list1)

list2= two_sum(arr2, target2)
print(list2)
