arr = [7,9,2,4,5,6]
for item in arr:
    if item%2==0:
        arr.remove(item)
        arr.insert(0, item)
print(arr)
