# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total():
   total = len(cinema_seats)*len(cinema_seats[0])
   return total

def seats_available():
   available=0
   for row in cinema_seats:
      for seat in row:
         if seat == 'A':
            available+=1
   return available

def seats_booked():
   booked=0
   for row in cinema_seats:
      for seat in row:
         if seat == 'B':
            booked+=1
   return booked

def seat_status(row, place):
   if cinema_seats[row-1][place-1]=='A':
      return 'Available'
   else:
      return 'Booked'

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total())
print('Seats available:',seats_available())
print('Seats booked:', seats_booked())
print('Seat in row 1, place 1:', seat_status(1,1))
print('Seat in row 5, place 5:', seat_status(5,5))
print('Seat in row 3, place 5:', seat_status(3,5))