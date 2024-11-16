arr = [-15, 8, -31, 47, -2, 19]
maximum = arr[0]
minimum = arr[0]
for item in arr:
    if item>maximum:
        maximum=item
    elif item<minimum:
        minimum=item
print(maximum)
print(minimum)