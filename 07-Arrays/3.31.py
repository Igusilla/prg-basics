arr = [
    [-38, 19],
    [5,40],
    [-7,11],
    [29,16]
   ]
maksimum=0
rowmax=0
colmax=0
minimum=0
rowmin=0
colmin=0
for item in arr:
    for item1 in item:
        if item1>maksimum:
            maksimum=item1
            rowmax=arr.index(item)+1
            colmax=item.index(item1)+1
        if item1<minimum:
            minimum=item1
            rowmin=arr.index(item)+1
            colmin=item.index(item1)+1

print('Minimum:', minimum, 'Row:', rowmin, 'Column:', colmin)
print('Maksimum:', maksimum, 'Row:', rowmax, 'Column:', colmax)