
## Find the union and intersection of two sorted arrays
#union 
#simple approach
def union(a,b):
  a= set(a)
  b=set(b)
  return list(sorted(a.union(b)))
a = str(input())
b= str (input())

union(a,b)

#OR
def union(arr1, arr2, m, n):
  i = 0
  j = 0
  while i < m and j < n:
    if arr1[i] < arr2[j]:
      print(arr1[i], end=" ")
      i += 1
    elif arr2[j] > arr1[i]:
      print(arr2[j], end=" ")
      j += 1
    else:
      print(arr2[j], end=" ")
      i += 1
      j += 1

  while i < m:
    print(arr1[i])
    i += 1

  while j < n:
    print(arr2[j])
    j += 1

arr1=[1,2,3,4,5]
arr2=[3,4,5,6]
m = len(arr1)
n = len(arr2)
union(arr1, arr2, m, n)

#intersection of a sorted array
#merge procedure

def intersection(arr1,arr2,m,n):
  i,j=0,0
  while i<m and j<n:
    if arr1[i]<arr2[j]:
      i+=1
    elif arr1[i]>arr2[j]:
      j+=1
    else:
      print(arr1[i], end=" ")
      i+=1
      j+=1

arr1=[1,2,3,4]
arr2=[3,4,5,6]
m=len(arr1)
n=len(arr2)
intersection(arr1,arr2,m,n)