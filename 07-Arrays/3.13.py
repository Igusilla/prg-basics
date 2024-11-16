def occurs(number, array):
    if number in array:
        return True
    else:
        return False

number=int(input('Number: '))
arr = [15, 38, 7, 23, 14]
print(occurs(number, arr))