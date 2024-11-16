arr = [
    [52, 11, 57],
    [2, 1, 35],
    [4, 74, 78],
    [0, 88, 95],
    [10, 9, 27]
]
for item in arr:
    print(item)

print('Swaped:')

arr[0], arr[-1] = arr[-1], arr[0]
for item in arr:
    print(item)
