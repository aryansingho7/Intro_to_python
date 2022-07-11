
##Given an array of integers. Find the Inversion Count in the array.

#Simple solution

def inversionCount(arr,n):
  count=0
  
  for i in  range(n):
    for j in range(i+1,n):
      if arr[i]>arr[j]:
        count+=1
  return count

arr = list(map(int,input().split()))
n=len(arr)
inversionCount(arr,n)

##Given an array of integers. Find the Inversion Count in the array.

#merge sort
def merge(arr,left,mid,right):
  i=left
  j=mid
  k=0
  invcount=0
  temp=[0 for x in range(right - left +1)]

  while(i<mid) and (j<=right):
    if arr[i]<=arr[j]:
      temp[k]= arr[i]
      k+=1
      i+=1
    else:
      temp[k]= arr[j]
      invcount += mid -i
      k+=1
      j+=1
  while i < mid:
    temp[k]= arr[i]
    k +=1
    i +=1

  while j<= right:
    temp[k]=arr[j]
    k+=1
    j+=1
  
  k=0
  for i in range(left,right+1):
    arr[i]= temp[k]
    k+=1

  return invcount


def mergesort(arr,left,right):
  invcount=0

  if right>left:
    mid=(right+left) // 2

    invcount= mergesort(arr,left,mid)
    invcount+= mergesort(arr, mid+1, right)
    invcount+= merge(arr,left,mid+1,right)

  return invcount

def inversionCount(arr,n):
  return mergesort(arr,0 , n-1)


arr=[2,3,4,5,6]
n=5
inversionCount(arr,n)