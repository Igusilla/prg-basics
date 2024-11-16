array = [34,7,19,4,21,8]
number=0
evens=0
while number < len(array):
    if array[number]%2==0:
        evens+=1
    number+=1
print(evens)