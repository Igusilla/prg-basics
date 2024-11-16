def number_words(string):
    arr=string.split()
    return len(arr)

def longest_to_shortest(string):
    arr=string.split()
    arr.sort(key=len, reverse=True)
    return arr

def alphabetically_ordered(string):
    arr=string.split()
    return sorted(arr)