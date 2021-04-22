#py program to demons. working of the 
#dictionary clear()

text ={1:'geeeks',2:'for'}

text.clear()
print('text:', text)


#python code to demons. diff clear and {}
text1={1:'geeks',2:'for'}
text2=text1
#using clear makes both text1 and text 2 empty 
text1.clear()

print('after removing items using clear()')
print('text1=',text1)
print('text1=',text2)

text1={1:'one',2:'two'}
text2=text1
#this makes only text1 empty
text1={}

print('after removing items by assiging {}')
print('text1',text1)
print('text1',text2)