arr = [
    [52, 11, 57],
    [2, 1, 35],
    [4, 74, 78],
    [0, 88, 95],
    [10, 9, 27]
]
for item in arr:
    print(item)

print('Changed:')
for item in arr:
    item[0], item[-1] = item[-1], item[0]
    print(item)