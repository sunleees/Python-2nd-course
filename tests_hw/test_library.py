import pytest

from models_hw import Book, Library


class TestLibrary:
    @pytest.fixture
    def book(self):
        return Book("Леся Українка", "Лісова пісня")

    @pytest.fixture
    def library(self):
        return Library("Центральна бібліотека")

    def test_library_starts_empty(self, library):
        assert library.name == "Центральна бібліотека"
        assert library.books == []

    def test_add_book(self, library, book):
        library.add_book(book)
        assert len(library.books) == 1
        assert library.books[0] == book

    def test_remove_book(self, library, book):
        library.add_book(book)
        library.remove_book_by_id(book.id)
        assert len(library.books) == 0

    def test_remove_nonexistent_book(self, library):
        library.remove_book_by_id("fake-id")
        assert library.books == []

    def test_add_multiple_books(self, library):
        b1 = Book("Author1", "Title1")
        b2 = Book("Author2", "Title2")
        library.add_book(b1)
        library.add_book(b2)
        assert len(library.books) == 2
