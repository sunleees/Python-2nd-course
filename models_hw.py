import uuid


class Book:
    def __init__(self, author: str, title: str):
        self.author = author
        self.title = title
        self.id = str(uuid.uuid4())  # унікальний ідентифікатор


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book_by_id(self, book_id: str):
        self.books = [b for b in self.books if b.id != book_id]
