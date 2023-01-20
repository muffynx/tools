string = "6e617464616e61692e7061406b6b756d61696c2e636f6d"
x = [*string]

for i in range(2,len(x)+len(x),3):
    x.insert(i,' ')
y = ''.join(x)
print(y)



