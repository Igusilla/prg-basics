avg_speed = lambda distance, hours, minutes: round(distance/(hours + minutes/60),2)

dis = int(input('Enter distance in km: '))
hours = int(input('Enter number of travel hours: '))
minutes = int(input('Enter number of travel minutes: '))

print('Average speed:', avg_speed(dis, hours, minutes), 'km/h')