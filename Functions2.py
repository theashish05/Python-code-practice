name="ashiSh"
print(name.strip().lower())


# DATA CLEANING BY function
def clean_name(name):
    print(name.strip().lower())
clean_name("pPIUAIEN")
clean_name("DigamBAR")
clean_name("")


case_rule="lower"

def clean_name(name):
    cleaned = name.strip()
    if case_rule == "lower":
        cleaned=cleaned.lower()
    print("Cleaned : " ,cleaned)

clean_name("AshiSSh  ")
print("The rule is :" , case_rule)




def total(*args):
    print(sum(args))
    
total(1,2,3)
total(2,4,4)

# Create a user profile
def create_user(**kwargs):
    print(kwargs)
    print(type(kwargs))

create_user(first_name="AShis",
            last_name="acharya",
            age=26)



def clean_name(name):
    if not name:
        return None
    else:
        cleaned =name.strip().lower()
        return cleaned

cln_name = clean_name("gaGan")
print(cln_name)
 