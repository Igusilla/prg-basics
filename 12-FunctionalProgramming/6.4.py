# An array contains numbers from 1 to 20. Write a program that calculates and displays their third power. 
# Use the map() and an anonymous function.

array = []
for i in range(1,21):
    array.append(i)
third_pow = list(map(lambda x: x**3, array))
print(third_pow)