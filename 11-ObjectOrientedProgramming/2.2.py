class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def perimeter(self):
      return self.a * 4

square1 = Square(4)
square2 = Square(6)

area1 = square1.area()
perimeter1 = square1.perimeter()

area2 = square2.area()
perimeter2 = square2.perimeter()

print('Square with side 4:')
print(f'Area is {area1}, Perimeter is {perimeter1}')

print ('Square with side 6:')
print(f'Area is {area2}, Perimeter is {perimeter2}')