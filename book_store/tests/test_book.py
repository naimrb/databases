from lib.book import *

book = Book(1, "Title", "Author")
book2 = Book(1, "Title", "Author")

def test_initalising():
    assert isinstance(book, Book)
    assert book.id == 1
    assert book.title == "Title"
    assert book.author == "Author"

def test_equality():
    assert book == book2