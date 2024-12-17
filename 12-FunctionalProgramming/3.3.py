stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
prices = list(map(lambda position: position[0]*position[1], stock))
print('Total value:', sum(prices))