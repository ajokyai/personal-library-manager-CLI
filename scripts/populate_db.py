

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.book import Book
from lib.models.author import Author
from lib.models.genre import Genre

engine = create_engine("sqlite:///library.db")
Session = sessionmaker(bind=engine)
session = Session()

author1 = Author(name="J.K. Rowling")
author2 = Author(name="George Orwell")
session.add_all([author1, author2])


genre1 = Genre(name="Fantasy")
genre2 = Genre(name="Dystopian")
session.add_all([genre1, genre2])

session.commit()


book1 = Book(title="Harry Potter", author_id=author1.id, genre_id=genre1.id)
book2 = Book(title="1984", author_id=author2.id, genre_id=genre2.id)
session.add_all([book1, book2])
session.commit()

print("Database populated successfully!")
