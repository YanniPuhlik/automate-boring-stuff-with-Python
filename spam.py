#Comma Code,  Chapter 4
# Value list 'spam'
spam = ['apples', 'bananas', 'tofu', 'cats']
#separating variables with coma sign 
for i in range(len(spam)-2):
    print(str(spam[i]) + ', ', end='')
#puting end before the last item
print(str(spam[-2]) + ' and ' + str(spam[-1]))
