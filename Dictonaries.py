my_dict={'a':10,'b':20,'c':30}

print(my_dict)
# Ordered
# Keys are unique
# Values allow duplicates

# Not indexed used by key value pair
print(my_dict['b'])
my_dict['c']=40
print(my_dict)

# You are mutable 

user = {'id':1,'age':30,'city': 'Bengaluru'}

print(user['city'])
print(user.get('age'))
print('age'in user)
print( 'id'not in user)

print(user.keys())
print(user.values())
print(user.items())
print(user)
print('-----------------------------------------')


for u in user :
    print(u)

for key,value in user.items():
    print(key,value)


user.update({'age':55,'city':'DVG'})
print(user)