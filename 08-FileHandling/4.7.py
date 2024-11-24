import re
text = input('Text: ')
condition = '[aeiouyAEIOUY]'
vowels=0
for i in range(len(text)):
    if re.match(condition, text[i]):
        vowels+=1
print(vowels)
