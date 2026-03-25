email="2ashishacharya@gmail.com"

email=email.strip()
if email == "":
    print("Email cannot be empty")
elif not('.' in email and '@' in email):
    print("Email should have . and @ in the mail")
elif email.count('@')!= 1:
    print("Email should contain only 1 '@'")
elif not email.endswith(('.com','.org','.net')):
    print("Email should ends with .com ")
elif len(email) > 244:
    print("Email should have not more than 254 characters")
elif not(email[0].isalnum() and email[-1].isalnum):
    print("Email should end and start with alphabets")
else :
    print(" Your email is valid")


valid=True
email=email.strip()
if email == "":
    print("Email cannot be empty")
    valid=False
if not('.' in email and '@' in email):
    print("Email should have . and @ in the mail")
    valid=False
if email.count('@')!= 1:
    print("Email should contain only 1 '@'")
    valid=False
if not email.endswith(('.com','.org','.net')):
    print("Email should ends with .com ")
    valid=False
if len(email) > 244:
    print("Email should have not more than 254 characters")
    valid=False
if not(email[0].isalnum() and email[-1].isalnum):
    print("Email should end and start with alphabets")
    valid=False
else :
    print(" Your email is valid")