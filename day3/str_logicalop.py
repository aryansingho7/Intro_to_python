#Logical operation in strings

str1=''
str2='geeks'

#repr prints string with qoutes
#return str1
print(repr(str1 and str2))

#return str1
print(repr(str2 and str1))

#return str2
print(repr(str1 or str2))

#return str 1
print(repr(str2 or str1))

str1='for'

#return str2
print(repr(str1 and str2))
#return str1
print(repr(str2 and str1))
#return str1
print(repr(str1 or str2))
#return str2
print(repr(str2 or str1))

str1='geek'
# return false
print(repr(not str1))

str1=''

#return TRUE
print(repr(not str1))