#approach 1
#python program to reverse an array 

#function to reverse an array A[] from start to end
def reverselist(A, start, end):
    while start < end:
        A[start], A[end]= A[end], A[start]
        start= start+1
        end =end-1

#driver function
A=[1,2,3,4,5,6]
print(A)
reverselist(A,0,5)
print("Reversed List is")
print(A)
#time complexity :O(n)

#approach 2: using python list slicing 
def reverselist1(A):
    print(A[::-1])

#driver fucntion to test 
A=[1,2,3,4,5,6]
print(A)
print("reversed List is")
reverselist(A)