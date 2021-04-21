#Escaping $ sign
# $$ used to escape $
template=Template('$$ is the symbol for $name')
string=(template.safe_substitute(name='dollar'))
print(string)