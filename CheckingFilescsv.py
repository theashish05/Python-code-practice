
# print ("Checking the all file in data whether they are in csv ,pdf or other format")
# files=['data1.csv','report.csv','report2.pdf']

# for file in files:
#     if file == file.endswith('.csv'):
#         print(f"{file} is not a csv")
#         break
# else :
#     print("All files are in csv")



print ("Nested loops")
years =[2026,2027]
months=['Jan','Feb']
days=range(1,29)

for y in years:
    for m in months:
        for day in days:
            print(f'report_{y}_{m}_{day}.csv')