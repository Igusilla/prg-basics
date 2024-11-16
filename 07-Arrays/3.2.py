import random
arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
myarr1 = [4,0,3]
myarr2 = [0 for i in range(15)]
myarr3 = [random.randint(1,30) for i in range(10)]
myarr4 = [random.randint(0,1) for i in range(20)]
myarr5 = [[False for i in range(2)] for i in range(5)]
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)
print('My: ')
print(myarr1) # an array with values: 4,0,3
print(myarr2) # 15-element array filled with zeros
print(myarr3) # an array with integer values in the range of <1,30>
print(myarr4) # 20-element array filled with 0 or 1 randomly
print(myarr5) # two dimensional array with five rows and two columns filled with False