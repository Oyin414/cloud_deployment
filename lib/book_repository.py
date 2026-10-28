from lib.book import Book

class BookRepository():
    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM books')

        books = []
        for row in rows:
            item = Book(row['id'],row['title'],row['author'])
            books.append(item)

        return books

    def find(self,id):
        rows = self._connection.execute('SELECT * FROM books WHERE id = %s', [id])

        return Book(rows[0]['id'],rows[0]['title'],rows[0]['author'])

    def create(self,book):
        self._connection.execute('INSERT INTO books (title,author) VALUES (%s,%s)', [book.title,book.author])
        return None