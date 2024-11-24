import csv
print('GRAPHIC DESIGNER')
print('=================')
with open('it_company.csv', 'r') as file:
    company=csv.DictReader(file)
    for row in company:
        if row['Job Title']=='Graphic Designer':
            print(f'{row['Last Name']} {row['First Name']},{row['Email']}')