#py program to demons. workinng of dcit copy

original ={1:'geeks',2:'for'}

#copying using copy( fucntion)
new=original.copy()

#removing all elemnts from the list
#only new list becomes empty as copy()
#does shallow copy

new.clear()

print('new:' ,new)
print('original:' , original)

#copying using =

new = original
#removing all element from the list 
# and printing both
new.clear()

print('new',new)
print('original', original)