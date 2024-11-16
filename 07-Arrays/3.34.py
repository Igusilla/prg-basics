import random
def matrix(n):
    arr = [[random.randint(1,100) for i in range(n)] for i in range(n)]
    return arr
def wypisanie(x):
    for i in matrix(x):
        print(i)
    return ''

print(wypisanie(3))
print(wypisanie(5))
print(wypisanie(8))