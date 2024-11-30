computer_store = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}
total_number=0
for key,value in computer_store.items():
    total_number+=value
    print(f"{key}:{value}")

print('Total number of products:',total_number)