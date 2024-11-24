with open('Integer_powers.txt', 'w') as file:
    for i in range(1,101):
        file.write(f'{i},{i**2},{i**3}\n')
        print(f'{i},{i**2},{i**3}')