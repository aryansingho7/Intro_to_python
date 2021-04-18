#creating tuple with mixed data types
#creating a tuple with mix DT
tuple1=(1,2,'geek',7)
print('tuple with mixed DT:')
print(tuple1)

#creating tuple with nested tuples
tuple1=(0,1,2,3)
tuple2=('geek','for','geeks')
tuple3=(tuple1,tuple2)
print('tuple with nested tuples:')
print(tuple3)

#creating a tuple with repetition
tuple1=('geeks',)*3
print('tuple with repetition:')
print(tuple1)

#creating a tuple eith the use of loop
tuple1=('geeks')
n=5
print('tuple with loop')
for i in range(int(n)):
    tuple1=(tuple1,)
    print(tuple1)