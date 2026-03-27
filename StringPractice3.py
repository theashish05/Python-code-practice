#for lopps
for i in(1,2,3,4,5):
    print(f"Round of {i}")

print("---------------------")
items =(11,12,13,14,15)
for items in items:
    print(f"Round of {items}")

print("---------------------")

lang="Python"
for lang in lang:
    print(f"Round of {lang}")

print("---------------------")


# even
for items in range (95,105,2):
    print(f"Round of {items}")

print("---------------------")

#odd
for num in range (1,10,2):
    print(f"Round of {num}")



days =['mon','tue','sun','thur']
for day in days:
    weekend=['sat','sun']
    if day in weekend:
        continue
        print(f"weekday {day}")


emails =['ashish@gmail.com',
         'rohi@gmail.com',
         'DROP table Users;']
for email in emails:
    if ';' in email:
        break
    print("Hacker attack SQL script detected")
    print(f"Processing email {email}")
