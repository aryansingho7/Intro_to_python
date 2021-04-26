#define fucntion for maximun, min,sum of a number in a list , removal of duplicate elemnt by using fucntion

#creation of list
number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)

# Calculating the sum of list elements
print("Sum = ", sum(number_list))

# printing the maximum of list
print("Maximumw of list is : ",end="")
print (max( number_list ) )