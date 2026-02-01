import pytest
from lib.models.base import Session
from lib.models.book import Book
from lib.models.author import Author
from lib.models.genre import Genre

def test_add_author():
    with Session() as session:
        author = Author(name="Test Author")
        session.add(author)
        session.commit()
        assert author.id is not None

def test_add_genre():
    with Session() as session:
        genre = Genre(name="Test Genre")
        session.add(genre)
        session.commit()
        assert genre.id is not None

def test_add_book():
    with Session() as session:
        # First, add an author and genre
        author = Author(name="Book Author")
        genre = Genre(name="Book Genre")
        session.add_all([author, genre])
        session.commit()
        
        book = Book(title="Test Book", author_id=author.id, genre_id=genre.id)
        session.add(book)
        session.commit()
        
        assert book.id is not None
