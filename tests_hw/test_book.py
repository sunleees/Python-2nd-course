from models_hw import Book


class TestBook:
    def test_create_book(self):
        book = Book("Іван Франко", "Захар Беркут")
        assert book.author == "Іван Франко"
        assert book.title == "Захар Беркут"
        assert isinstance(book.id, str)

    def test_unique_ids(self):
        b1 = Book("A", "B")
        b2 = Book("A", "B")
        assert b1.id != b2.id
