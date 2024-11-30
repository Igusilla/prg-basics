import queue

binary=queue.LifoQueue()

number=int(input('Number: '))
while number!=0:
    reszta=number%2
    binary.put(reszta)
    number//=2
print('Binary number:', end=' ')
while not binary.empty():
    print(binary.get(), end='')