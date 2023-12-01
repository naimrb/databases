# Books Model and Repository Classes Design Recipe

Set up a new project called book_store from the starter.\
Use the book_store SQL seed instead of the music_library seed. You can find this in the seeds directory in the starter.\
Follow the design recipe as usual, before starting to test-drive the classes.\
Once you've done the design recipe, start recording yourself.\
Test-drive a Book class that has attributes for each column in the books table, using the example(s) from your design.\
Test-drive a BookRepository class that has a method all that returns a list of Book objects.\
Write a small program in app.py using the class BookRepository to print out the list of books to the terminal.\

## 1. Design and create the Table

```
Table: books

Columns:
id | title | author_name
```

## 2. Create Test SQL seeds


## 3. Define the class names

```python
# Table name: books

# Model class
# (in lib/book.py)
class Book


# Repository class
# (in lib/book_repository.py)
class BookRepository

```

## 4. Implement the Model class

```python
# Table name: books

# Model class
# (in lib/book.py)

class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
```
## 5. Define the Repository Class interface
```python
# Table name: books

# Repository class
# (in lib/book_repository.py)

class BookRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students;

        # Returns an array of Student objects.

        # Gets a single record by its ID
        # One argument: the id (number)

```

## 6. Write Test Examples

```python

# 1
# Get all books
#Book1 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
#Book2 = Book(2, 'Mrs Dalloway', 'Virginia Woolf');

repo = BookRepository()

books = repo.all()

len(books) # =>  2

books[0].id # =>  1
books[0].title # =>  'Nineteen Eighty-Four'
books[0].author_name # =>  'George Orwell'

books[1].id # =>  2
books[1].title # =>  'Mrs Dalloway'
books[1].author_name # =>  'Viriginia Woolf'