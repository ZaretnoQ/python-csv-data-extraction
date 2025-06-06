import csv

class Book:
    def __init__(self, book, sale):
        self.book = book
        self.sale = sale

with open('Bestseller - Sheet1.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)

    book = Book('name', 0.0)
    next(csv_reader)

    for i in csv_reader:
        sale = float(i[4])

        if sale >= book.sale:
            book = Book(i[0], sale)

    print(f"{book.book} - {book.sale}")