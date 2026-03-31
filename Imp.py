# META DATA DRIVEN
tables= ['customer','orders','products','prices']
columns=['id','create_date']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')


# 3 Attempts
# Yes within 3 attempts
# Otherwise your'e are out
attempts = 0
while attempts < 3:
    answer = input("Do you agree ? (Yes/No)")
    if answer=="yes":
        print("Glad we are on same page")
        break
    attempts += 1
else :
    print("thank you")