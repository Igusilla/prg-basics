import csv
with open('books.csv', 'r') as file:
    books = csv.DictReader(file)
    for row in books:
        file_name='books_'+row['Genre']+'.csv'
        with open(file_name, 'a') as filew:
            filew.write(f'{row['Title']},{row['Author']},{row['Genre']},{row['Year']}\n')
