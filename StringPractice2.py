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



# Passwords
password = "As33qqqq3gmailm"
email = "user@example.com"

# 1. Must not be empty
if not password:
    print("Password should not be empty")

# 2. Must be at least 8 characters
elif len(password) < 8:
    print("Password must be at least 8 characters")

# 3. Must include at least 1 uppercase
elif not any(char.isupper() for char in password):
    print("Password must include at least 1 uppercase letter")

# 4. Must include at least 1 lowercase
elif not any(char.islower() for char in password):
    print("Password must include at least 1 lowercase letter")

# 5. Must not be same as the email
elif password == email:
    print("Password should not be the same as the email")

# 6. Must not contain any spaces
elif " " in password:
    print("Password must not contain any spaces")

# 7. Must start and end with a letter or digit
elif not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit")

else:
    print("Password saved successfully")
