#py program for formatting of string
#default string

string1='{} {} {} '.format('hey', 'there', 'world')
print('print string in the default order:')
print(string1)

#positional formatting
string1='{1} {0} {2} '.format('hey', 'there', 'world')
print(string1)

#keyword formatting
string1='{x} {y} {z} '.format(x='hey', y='there' , z='world')
print('print the string by keyword order:')
print(string1)