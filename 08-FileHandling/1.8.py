def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content=read_from_file('pets.txt')
file_line=file_content.splitlines()
words=0
for item in file_line:
   words+=len(item)
for line in file_line:
   print(line)
print("Words count:",words)