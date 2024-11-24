file_name=input('File name: ')
try:
    with open(file_name, 'r') as file:
        content=file.read()
        lines=content.splitlines()
    
    print('Number of lines:',len(lines))
    print('Number of words:', len(content.split()))
    print('Number of characters:', len(content))
except:
    print('File doesnt exist')