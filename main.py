import click
from lib.models.base import Session
from lib.models.book import Book
from lib.models.author import Author
from lib.models.genre import Genre

@click.group()
def cli():
    """Personal Library Manager"""
    pass



@cli.command()
def list_books():
    """List all books"""
    with Session() as session:
        books = session.query(Book).all()
        for book in books:
            print(f"{book.id}: {book.title} (Author ID: {book.author_id}, Genre ID: {book.genre_id})")

@cli.command()
def list_authors():
    """List all authors"""
    with Session() as session:
        authors = session.query(Author).all()
        for author in authors:
            print(f"{author.id}: {author.name}")

@cli.command()
def list_genres():
    """List all genres"""
    with Session() as session:
        genres = session.query(Genre).all()
        for genre in genres:
            print(f"{genre.id}: {genre.name}")

# ---------- Add Commands ----------

@cli.command()
@click.argument("title")
@click.argument("author_id", type=int)
@click.argument("genre_id", type=int)
def add_book(title, author_id, genre_id):
    """Add a new book"""
    with Session() as session:
        book = Book(title=title, author_id=author_id, genre_id=genre_id)
        session.add(book)
        session.commit()
        print(f"Added book: {title}")

@cli.command()
@click.argument("name")
def add_author(name):
    """Add a new author"""
    with Session() as session:
        author = Author(name=name)
        session.add(author)
        session.commit()
        print(f"Added author: {name}")

@cli.command()
@click.argument("name")
def add_genre(name):
    """Add a new genre"""
    with Session() as session:
        genre = Genre(name=name)
        session.add(genre)
        session.commit()
        print(f"Added genre: {name}")

if __name__ == "__main__":
    cli()
