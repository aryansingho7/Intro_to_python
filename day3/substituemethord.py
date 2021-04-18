#implementation of safe substitute methord
from string import Template

template=Template('$name is the $job of $company')

string=(template.safe_substitute(name='Aryan', job='IFS', company='INDIA'))

print(string)