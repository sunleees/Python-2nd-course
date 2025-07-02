import pytest
from models_hw import Book, Library


@pytest.fixture
def book():
    return Book(author="Тарас Шевченко", title="Кобзар")

@pytest.fixture
def library():
    return Library(name="Центральна бібліотека")
