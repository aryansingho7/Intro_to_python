#py program to demons. th euse of formatting using %

#initialize variable as a string
variable='15'
string='Variable as string=%s' %variable
print(string)

#printing as raw data
print('variable as raw data=%r' %(variable))

#convert variable to interger
variable= int(variable)
print('variable to integer=%d' %(variable))
print(string)
print('variable to float=%f' %(variable))

#printing as anu string or char after a mark
print('variable as printing an special char=%caryan' %variable)
print('variable to hexadecimal=%x' %variable)
print('variable to octal=%o' %variable)