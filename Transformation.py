lett = ['a','b','c']
print(list(map(str.upper,lett)))

num = ['1','2','3']
print(list(map(int,num)))

names =['ashish','gagan','  kumar']
print(list(map(str.strip,names)))

for n in map(str.strip,names):
    print(n)