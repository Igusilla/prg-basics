arr= [15, 8, 31, 47, 2, 19]
mean = 0
number = 0
while number < len(arr):
    mean += arr[number]
    number+=1
mean /= len(arr)
print(arr)
print(round(mean,2))