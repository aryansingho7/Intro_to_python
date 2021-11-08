#python prigram to find factorial of a given number

#methord 1
def factorial(n):

    #single line to find factorial
    return 1 if (n==1 or n==0) else n* factorial(n-1);

#driver code
num=5;
print('factorial of a number:', num , "is")
factorial(num)