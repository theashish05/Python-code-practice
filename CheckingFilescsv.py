
print ("Checking the all file in data whether they are in csv ,pdf or other format")
files=['data1.csv','report.csv','report2.pdf']

for file in files:
    if not file.endswith('.csv'):
        print(f"{file} is not a csv")
        break
else :
    print("All files are in csv")