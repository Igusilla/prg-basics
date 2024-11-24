import re
with open('files.txt', 'r') as file:
    content=file.read()
    lines=content.split()
condition = '.+\.[a-z]{4}'
for line in lines:
    if re.match(condition, line):
        print(line)