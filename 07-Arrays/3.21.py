arr1 = [7,9,14,5,6]
arr2 = [7,9,2,4,5,6,10,51,5324,43]
for item in arr1:
    if item not in arr2:
        print('Arr1 isnt the subset of arr2')
        break
else:
    print('Arr1 is the subset of arr2')
    
