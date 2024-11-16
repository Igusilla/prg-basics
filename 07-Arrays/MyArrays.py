def Second_largest(array):
    array.sort()
    return array[-2]

def diffrence_extremas(array):
    return max(array)-min(array)

def median(array):
    array.sort()
    if len(array)%2==1:
        return array[int(len(array)/2)]
    else:
        return int(((array[int(len(array)/2)] + array[int((len(array)/2)+1)]/2)/2))
    
def extremas(array):
    array.sort()
    return array[0], array[-1]

def arr_str(array):
    array0=[]
    for item in array:
        array0+=str(item)
    string = '-'.join(array0)
    return string
