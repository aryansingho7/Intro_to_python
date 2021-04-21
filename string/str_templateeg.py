#py program to demon, thhe working of the string template
from string import Template

#list student stores the name and marks of three students
student=[('Aryan',90),('ryan',80),('Yan',70)]

#create a basic structure to print name and amrks of the student
t= Template('Hey $name, you got $marks marks')

for i in student: 
    print(t.substitute(name=i[0], marks= i[1]))