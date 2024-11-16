array = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
for i in range(len(array)):
    for j in range(len(array)):
        if i==j:
            array[i][j]=1
    print(array[i])
