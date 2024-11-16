arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
for i in range(1,6):
    arr[0][i-1]+=i
    if i != 1:
        arr[i-1][0]+=i
for i in range(1,len(arr)):
    for j in range(1, len(arr[i])):
        arr[i][j]=arr[0][j]*arr[i][0]
for i in range(len(arr)):
    print((arr[i]))