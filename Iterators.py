# Iterators
letters = ['a','b','c']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)


# Enumerators
for index,value in enumerate (letters):
    print(index,value)

# examples

numbers=[1,2,3]
for l,n in zip (letters,numbers):
    print(l,n)