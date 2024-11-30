import queue
notacja = queue.LifoQueue()
while True:
    x = input()
    if x.isdigit():
        notacja.put((x))
    else:
        if x=='=':
            print(notacja.get())
            break
        else:
            b = notacja.get()
            a = notacja.get()
            tymczas = a + x + b
            wynik = eval(tymczas)
            notacja.put(str(wynik))
