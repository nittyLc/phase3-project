from lib.models import session
from models.book import Book
from models import Base, engine

print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables created successfully!")


books = session.query(Book).all()
for book in books:
    print(book)
