#py program to find the factorial of a number
def factorial(num):
   fact=1
   for i in range(1, num+1):
       fact=fact*1
       return fact
number=int(input('enter a number:'))
result= factorial(number)
print('the factorial of %d= %d'%(number,result))