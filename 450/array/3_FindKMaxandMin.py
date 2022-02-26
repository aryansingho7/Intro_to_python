#Find the Kth smallest element in array
def kthsmallest(arr,k):
    arr.sort()
    return arr[k-1]
arr= list(map(int,input().split(' ')))
k= int(input())
kthsmallest((arr,k))

