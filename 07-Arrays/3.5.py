arr = [15, 8, 31, 47, 2, 19]
mean = 0
for number in arr:
    mean += number
mean /= len(arr)
print(arr)
print(round(mean,2))