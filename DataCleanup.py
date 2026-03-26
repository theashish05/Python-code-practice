#Everytime we need to do datacleanup for having perfect data..
# First we need to do the Data clean up then 
# we need to manipulate or transform the data
# 1 - DATA CLEANUP
# 2 - DATA MANIPULATION OR TRANSFORMATION

files = ['reports.csv', ' DATA.csv','final.txt']
for file in files:
    file=file.strip().lower().replace('.txt','.csv')
    print(f" Processing {file}")




for i in range (1,11):
    resut =7 * i
    print(f"7 * {i} = {resut}")

# *
# **
# ***
# ****
for i in range(1,5):
 print("*" * i)

# ****
# ***
# **
# *
for i in range (4,0,-1):
    print("*" * i)
