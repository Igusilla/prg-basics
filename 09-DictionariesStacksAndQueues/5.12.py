# Define a function that takes a string as input and
# uses a stack to reverse it. Then, write a program to reverse any text entered from the keyboard.  
import queue
def reverse_string(string):
    stringque = queue.LifoQueue()
    rstring=""
    for i in range(len(string)):
        stringque.put(string[i])
    for i in range(len(string)):
        rstring+=stringque.get()

    return rstring
string = input('String to reverse: ')
print("Reversed string:", reverse_string(string))
