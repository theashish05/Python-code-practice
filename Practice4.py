print("Hello April ready for the marathon")

names =  ['Ashish','Gagan',None,'Vidya']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")
        