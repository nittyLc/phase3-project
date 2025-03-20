import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models import session
from lib.models.book import Book
from lib.models.member import Member
from lib.models.borrow import Borrow

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. View Books")
        print("5. View Members")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            register_member()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            view_books()
        elif choice == '5':
            view_members()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    copies = int(input("Enter copies available: "))
    new_book = Book(title=title, author=author, copies_available=copies)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' added.")

def register_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    new_member = Member(name=name, email=email)
    session.add(new_member)
    session.commit()
    print(f"Member '{name}' registered.")

def borrow_book():
    book_id = int(input("Enter book ID: "))
    member_id = int(input("Enter member ID: "))
    book = session.query(Book).get(book_id)
    if book and book.copies_available > 0:
        book.copies_available -= 1
        borrow = Borrow(book_id=book_id, member_id=member_id)
        session.add(borrow)
        session.commit()
        print(f"Book '{book.title}' borrowed by Member ID {member_id}.")
    else:
        print("Book not available.")

def view_books():
    books = session.query(Book).all()
    for book in books:
        print(book)

def view_members():
    members = session.query(Member).all()
    for member in members:
        print(member)

if __name__ == "__main__":
    main_menu()
