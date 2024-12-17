filled_bottles = [508,500,512,499,492,511,503,476,501,509]
corectly_filled = list(filter(lambda x:x>=490 and x<=510, filled_bottles))

print('Bottle capacity: 500ml')
print('Filling tolerance: 2%')
print('Filled bottles:',filled_bottles)
percentage = (len(filled_bottles)-len(corectly_filled))/len(filled_bottles)*100
print('Incorrectly filled:', percentage,'%')