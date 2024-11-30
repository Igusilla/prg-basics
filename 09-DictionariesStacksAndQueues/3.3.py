import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   otwarcia=0
   zamknięcia=0
   expresionnn=queue.LifoQueue()
   for i in range(len(expression)):
    if expression[i]=='[' or expression[i]=='(' or expression[i]=='{':
        expresionnn.put(expression[i])
        otwarcia+=1
    elif not expresionnn.empty() and (expression[i]==']' or expression[i]==')' or expression[i]=='}'):
        znak = expresionnn.get()
        zamknięcia+=1
        if znak == '[':
            znak = ']'
        elif znak == '{':
            znak='}'
        elif znak == '(':
            znak=')'
        if znak != expression[i]:
            return False
        elif zamknięcia==otwarcia:
            return True
       
        
    
if brackets_ok(expression1):
   print('Correct')
else:
   print('Incorrect')

if brackets_ok(expression2):
   print('Correct')
else:
   print('Incorrect')

if brackets_ok(expression3):
   print('Correct')
else:
   print('Incorrect')
