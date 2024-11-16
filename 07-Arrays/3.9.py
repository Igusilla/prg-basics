def compare(arr1,arr2):
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            if arr1[i]==arr2[i]:
                continue
            else:
                print("Comparison: arrays aren't the same")
                return False
        print("Comparison: arrays are the same")
        return True
    else:
        print("Comparison: arrays aren't the same")
        return False

arr1=["water","book","sky"]
arr2=["water","book","sky"]
print('Array1:',arr1)
print('Array2:',arr2)
compare(arr1,arr2)#True
arr1=[True,False]
arr2=[True,False,True]
print('Array1:',arr1)
print('Array2:',arr2)
compare(arr1,arr2)
arr1=[5,3,1]
arr2=[5,3,1]
print('Array1:',arr1)
print('Array2:',arr2)
compare(arr1,arr2)
arr1=[3,2,1]
arr2=[3,1,1]
print('Array1:',arr1)
print('Array2:',arr2)
compare(arr1,arr2)