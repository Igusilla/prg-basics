def bubblesort(array):
    for j in range(len(array)-1):
        for i in range(len(array)-1):
            if array[i]<array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array

arr = [4,36,12,28,9,44,5]
arr1 = [15, 8, 31, 47, 2, 19]
arr2 = [34,7,19,4,21,8]
print(bubblesort(arr))
print(bubblesort(arr1))
print(bubblesort(arr2))