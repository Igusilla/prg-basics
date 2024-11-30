price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
print('PRICE BEFORE DISCOUNT')
total_before_discount=0
for key,value in price_list.items():
    print(f'{key}:{value}')
    total_before_discount+=value
print('Total value of the products before the discount', round(total_before_discount,2))
for key,value in price_list.items():
    price_list[key]=round(value*0.9,2)
total_after_discount=0
for key,value in price_list.items():
    print(f'{key}:{value}')
    total_after_discount+=value
print('Total value of the products after the discount', round(total_after_discount,2))