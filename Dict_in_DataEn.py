# TO store the structure of our DATA

# Dicionaries are collection of multipple related information

row ={
    "id": 1001,
    "name":"Ashish",
    "age":26,
    "country":"India",
    "status":"active",
}
print(row)

country_map={
    "IND":"INDIA",
    "GER":"GERMANY",
    "USA":"AMERICA",
}
print(country_map)

print("----------------")

row_str={
    k.lower():v.upper()
    for k,v in row.items()
    if isinstance(v,str)
} 

print(row_str)