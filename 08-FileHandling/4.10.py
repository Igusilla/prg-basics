import csv
with open('clothing.csv', 'r') as file:
    content=csv.DictReader(file)
    for row in content:
        if float(row['Price'])<60 and float(row['Stock_Quantity'])<40:
            print(f'{row['Product_ID']},{row['Product_Name']},{row['Category']},{row['Size']},{row['Color']},{row['Price']},{row['Stock_Quantity']}')