#string template class in py

#simple py template example
from string import Template

#create a template that has placeholder for value of x
t= Template('x is $x')

#subtitute value of xin ablove template
print(t.substitute({'x':1}))