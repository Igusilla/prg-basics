countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":84500000},
    {"name":"USA", "population":334900000},
    {"name":"Norway", "population":5520000},
    {"name":"England", "population":56500000},
]
print('COUNTRY   POPULATION')
for dictionary in countries:
    for key,item in dictionary.items():
        print(item, end='   ')
    print()