#Find the Kth smallest element in array
def kthsmallest(arr,k):
    arr.sort()
    return arr[k-1]
arr= list(map(int,input().split(' ')))
k= int(input())
kthsmallest(arr,k)

def kthlargest(arr,k):
    k=len(arr)-k
    def quickselect(l,r):
        pivot, p= arr[r], l
        for i in range(l,r):
            if arr[i] <= pivot:
                arr[p], arr[i]= arr[i], arr[p]
                p += 1
        arr[p], arr[r]= arr[r], arr[p]

        if p>k:
            return quickselect(l,p-1)
        elif p <k:
            return quickselect(p+1,r)
        else:
            return arr[p]

    return quickselect(0, len(arr)-1)

arr =list(map(int,input().split(' ')))
k=int(input())
kthlargest(arr,k)
