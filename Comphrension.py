# Data cleanup in comphresion method
domains = ['www.youtube.com',
           'linked.in',
           'QQQWWWEEE', 
           'Ashish@gmail.com']

cleaned = [
    d.lower().replace('www','')
    for d in domains
    if '.' in d
]
print(cleaned)