#example1

#show the working of the setdefault()


#dictionary with the single item
Dict1={'a':'aryan','b':'ryan','c':'yan'}

#using set default function
Third_value=Dict1.setdefault('c')
print('dictionary:',Dict1)
print('Third value:', Third_value)



#example 2
#setdefault() in dictionary

Dict1={'a':'geek','b':'for'}

#using setdefault() when key is not in the dictionary
Third_value=Dict1.setdefault('c')
print('Dictionary:', Dict1)
print('third value:', Third_value)

#setdefault usage when key is not in the dictionary but default value is provided
Forth_value=Dict1.setdefault('d', "geek")
print('dictonary', Dict1)
print('fourth value:', Forth_value)