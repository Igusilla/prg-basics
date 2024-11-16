categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
i=0
for item in expenses:
    if item == max(expenses):
        break
    i+=1
print(categories[i])