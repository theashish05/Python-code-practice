# Mapping

letters = ['a','b','c']
print(list(map(str.upper,letters)))

number =['1','2','3']
print(list(map(int,number)))

names=['Ashish','Gagan','Vidya']
for n in map(str.strip,names):
    print(n)

# isAlpha
letters=['sql','maths','1212']
print(list(filter(str.isalpha,letters)))

# bool
newlet=['ash',True,False]
print(list(filter(bool,newlet)))
 
