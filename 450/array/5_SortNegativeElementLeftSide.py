# def rearrange(arr, n):
#   j=0

#   for i in range(0,n):
#     if arr[i]<0:
#       temp = arr[i]
#       arr[i]= arr[j]
#       arr[j]= temp
#       j+=1
#   return arr
  
# arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
# n= len(arr)
# rearrange(arr,n)
#move all the negative element to one side of the array 
#quick sort

def rearrange(arr, n):
  j=0

  for i in range(0,n):
    if arr[i]<0:
      temp = arr[i]
      arr[i]= arr[j]
      arr[j]= temp
      j+=1
  return arr
  
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n= len(arr)
rearrange(arr,n)