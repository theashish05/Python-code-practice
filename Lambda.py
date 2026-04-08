multiple = lambda x:x*2
print(multiple(5))

add = lambda x,y,z:x+y+z
print(add(2,8,4))

check = lambda i : i in "Ashish"
print(check('ashi'))


p ='$12.50'
print(float(p.replace('$','')))

# lambda + map
prices=['$1000.25','$9.99','$10.01']
print(list(map(lambda p: float(p.replace('$','')) ,prices)))

