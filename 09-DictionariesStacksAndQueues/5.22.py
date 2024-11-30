import json
product = {}

# read product data from keyboard
product["name"]=input("Name: ")
product["price"]=float(input("Price: "))
payment=input("Paid(Y/N): ")
if payment == 'Y':
    product["paid"]=True
else:
    product["paid"]=False
# save product data to json file
with open('product.json', "w", encoding="utf-8") as file:
    json.dump(product, file)