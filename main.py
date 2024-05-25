import re
import mysql.connector
from Validation import validate_isbn, validate_library_id, validate_date
from books import Book, FictionBook, NonFictionBook
from users import User
from authors import Author
from genres import Genre
from class_database_library import db_add_book, db_add_author, db_add_genre, db_add_user
from class_database_library import db_display_all_genres, db_display_all_authors, db_display_all_books, db_display_all_users
from class_database_library import db_borrow_book, db_return_book, db_search_book
from class_database_library import db_view_user_details, db_view_author_details, db_view_genre_details


books = []
users = []
authors = []
genres = []

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            genre_operations()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def genre_operations():
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_genre()
        elif choice == '2':
            view_genre_details()
        elif choice == '3':
            display_genres()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_book():
    title = input("Enter book title: ")
    isbn = input("Enter book ISBN (e.g., 978-1234567890): ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    publication_date = input("Enter book publication date (YYYY-MM-DD): ")
    if not validate_date(publication_date):
        print("Invalid date format. Please try again.")
        return
    db_add_book(title, isbn, publication_date)

def borrow_book():
    isbn = input("Enter ISBN of the book to borrow: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    user_id = input("Enter your library ID: ")
    if not validate_library_id(user_id):
        print("Invalid library ID format. Please try again.")
        return

    try:
        print("Attempting to borrow the book...")
        db_borrow_book(user_id, isbn)  # Pass user_id and ISBN to borrow the book
    except Exception as e:
        print(f"An error occurred while borrowing the book: {e}")
    
def return_book():
    isbn = input("Enter ISBN of the book to return: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    user_id = input("Enter your library ID: ")
    if not validate_library_id(user_id):
        print("Invalid library ID format. Please try again.")
        return

    try:
        print("Attempting to return the book...")
        db_return_book(user_id, isbn)  # Pass user_id and ISBN to return the book
    except Exception as e:
        print(f"An error occurred while returning the book: {e}")


    # Search for the book in the database
def search_book():
    isbn = input("Enter ISBN of the book to search: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return

    # Perform book search in the database
    try:
        print("Searching for book details...")
        book_details = db_search_book(isbn)
        if book_details:
            print("Book details found:")
            print(book_details)
        else:
            print("Book not found.")
    except Exception as e:
        print(f"An error occurred while searching for book details: {e}")
    db_search_book(isbn)

def display_books():
    if books:
        print("Books available:")
        for book in books:
            print(f"Title: {book.get_title()}, ISBN: {book.get_isbn()}, Publication Date: {book.get_publication_date()}")
    else:
        print("No books available.")
    db_display_all_books()
    
def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter user library ID (5 digits): ")
    if not validate_library_id(library_id):
        print("Invalid library ID format. Please enter a 5-digit numeric ID.")
        return
    try:
        user = User(name, library_id)
        db_add_user(user)  # Add user to database
        print(f"User '{name}' added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the user: {e}")

def view_user_details():
    user_id = input("Enter user library ID: ")
    if not validate_library_id(user_id):
        print("Invalid library ID format. Please try again.")
        return
    user = next((u for u in users if u.get_library_id() == user_id), None)
    if user:
        print(user)
    else:
        print("User not found.")
    db_view_user_details()

def display_users():
    db_display_all_users()

def add_author():
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    try:
        # Assuming author_id is generated automatically by the database
        author = Author(None, name, biography)  # Pass None for author_id
        authors.append(author)
        print(f"Author '{name}' added successfully.")
        db_add_author(author.get_name(), author.get_biography())
    except Exception as e:
        print(f"An error occurred while adding the author: {e}")

def view_author_details():
    author_id = input("Enter author ID: ")
    db_view_author_details(author_id)

def display_authors():
    authors = db_display_all_authors()
    if authors:
        for author in authors:
            author_id, name, biography = author  # Unpacking the tuple
            print(f"Author ID: {author_id}, Name: {name}, Biography: {biography}")
    else:
        print("No authors available.")
    db_display_all_authors()

def add_genre():
    name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")
    try:
        genre = Genre(None, name, description, category)  # Pass None for genre_id
        print(f"Genre '{name}' added successfully.")
        db_add_genre(genre.get_name(), genre.get_description(), genre.get_category())
    except Exception as e:
        print(f"An error occurred while adding the genre: {e}")

def view_genre_details():
    genre_id = input("Enter genre ID: ")
    db_view_genre_details(genre_id)


def display_genres():
    db_display_all_genres()


if __name__ == "__main__":
    main_menu()
