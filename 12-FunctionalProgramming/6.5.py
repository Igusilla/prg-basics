# An array contains numbers from 1 to 20. Write a program that displays only numbers divisible by 2 and 3 without remainder.
# Use the filter() and an anonymous function.

array = []
for i in range(1,21):
    array.append(i)
div_by_2_3 = list(filter(lambda x: x%3==0 and x%2==0, array))
print(div_by_2_3)