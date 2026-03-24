# Scenario: You receive a raw file with messy headers: 
# " First Name ", "Last-Name", "Order_ID#", "Total ($)".

# Task: Write a function to convert these into a 
# clean SQL-friendly format: lowercase, snake_case, and remove special characters.

import re

def clean_headers(headers):
    clean = []
    for h in headers:
        # Lowercase and strip whitespace
        s = h.strip().lower()
        # Replace spaces, hyphens, and special chars with underscores
        s = re.sub(r'[^a-z0-9]', '_', s)
        # Remove duplicate underscores (e.g., "total__" -> "total_")
        s = re.sub(r'_+', '_', s).strip('_')
        clean.append(s)
    return clean

raw_cols = ["  First Name  ", "Last-Name", "Order_ID#", "Total ($)"]
print(clean_headers(raw_cols)) 
# Output: ['first_name', 'last_name', 'order_id', 'total']



score=88.9
if score >= 90 :
    print("Pass")
    if score == 100:
        print ("Rewrite the exam /copy")

elif score >= 75:
    print("V GOOD")
else : 
    print("Fail")

