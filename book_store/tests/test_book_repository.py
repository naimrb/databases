from lib.book import *
from lib.book_repository import *

def test_get_all(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)
    
    books = repo.all()
    
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ] 