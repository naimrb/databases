from lib.book import *

class BookRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM books")
        books = []
        
        for row in rows:
            book = Book(row['id'], row['title'], row['author_name'])
            books.append(book)
        
        return books
    
    def find(self, id):
        row = self._connection.execute(f"SELECT * FROM books WHERE id = {id}")
        book = Book(row[0]['id'], row[0]['title'], row[0]['author_name'])

        return book