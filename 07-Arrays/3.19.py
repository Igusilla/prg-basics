arr = [1.5, 3.2, 4.8, 2.1, 5.6]
number = float(input('Number: '))
amount=0
for item in arr:
    if item>number:
        amount+=1
        
print('Amount of numbers greater than', number, 'in array is', amount)