import mysql.connector
from mysql.connector import Error
from Validation import validate_isbn, validate_library_id, validate_date

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'sqlpass#4'
DB_NAME = 'the_library_system_3'

# Function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to add a new book
def db_add_book(title, isbn, publication_date):

    if not (validate_isbn(isbn) and validate_date(publication_date)):
        print("Invalid ISBN or publication date.")
        return
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO books (title, isbn, publication_date) VALUES (%s, %s, %s)"
    values = (title, isbn, publication_date)
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Book added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Function to borrow a book
def db_borrow_book(library_id, isbn):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        print("Connected to MySQL database")

        # Check if the library_id exists in the users table
        user_query = "SELECT * FROM users WHERE library_id = %s"
        cursor.execute(user_query, (library_id,))
        user = cursor.fetchone()

        if user:
            user_id = user[0]  # Extract the user_id from the user tuple
            # Check if the book exists and is available
            book_query = "SELECT * FROM books WHERE isbn = %s AND is_borrowed = FALSE"
            cursor.execute(book_query, (isbn,))
            book = cursor.fetchone()

            if book:
                # Update book status and record borrowing
                update_query = "UPDATE books SET is_borrowed = TRUE WHERE isbn = %s"
                cursor.execute(update_query, (isbn,))
                connection.commit()

                insert_query = "INSERT INTO borrowed_books (book_id, user_id) VALUES (%s, %s)"
                cursor.execute(insert_query, (book[0], user_id))
                connection.commit()

                print("Book borrowed successfully.")
            else:
                print("Book not found or already borrowed.")
        else:
            print("User with the specified library ID not found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'connection' in locals():
            cursor.close()
            connection.close()

# Function to return a book
def db_return_book(book_id):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        update_query = "UPDATE books SET is_borrowed = FALSE WHERE book_id = %s"
        cursor.execute(update_query, (book_id,))
        connection.commit()

        update_query = "UPDATE borrowed_books SET return_date = NOW() WHERE book_id = %s AND return_date IS NULL"
        cursor.execute(update_query, (book_id,))
        connection.commit()
        print("Book returned successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Function to search for a book in the database
def db_search_book(isbn):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM books WHERE isbn = %s"
        cursor.execute(query, (isbn,))
        book = cursor.fetchone()

        if book:
            book_id, title, author_id, isbn, publication_date, is_borrowed, book_type = book
            print(f"Title: {title}, Author ID: {author_id}, ISBN: {isbn}, "
                  f"Publication Date: {publication_date}, Book Type: {book_type}, "
                  f"Status: {'Borrowed' if is_borrowed else 'Available'}")
        else:
            print("Book not found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Function to display all books
def db_display_all_books():
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT title, isbn, publication_date, is_borrowed FROM books"
        cursor.execute(query)
        books = cursor.fetchall()

        if books:
            for book in books:
                title, isbn, publication_date, is_borrowed = book
                availability = "Available" if not is_borrowed else "Borrowed"
                print(f"Title: {title}, ISBN: {isbn}, "
                      f"Publication Date: {publication_date}, "
                      f"Availability: {availability}")
        else:
            print("No books found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def db_add_user(user):
    if not validate_library_id(user.get_library_id()):
        print("Invalid library ID.")
        return
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        values = (user.get_name(), user.get_library_id())
        cursor.execute(query, values)
        connection.commit()
        print("User added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()     

def db_view_user_details():
    user_id = input("Enter user library ID: ")
    if not validate_library_id(user_id):
        print("Invalid library ID format. Please try again.")
        return
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE library_id = %s"
        values = (user_id,)
        cursor.execute(query, values)
        user_data = cursor.fetchone()

        if user_data:
            user_id, name, library_id = user_data
            print(f"User ID: {user_id}, Name: {name}, Library ID: {library_id}")
        else:
            print("User not found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

        
# Function to display all users
def db_display_all_users():
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()

        if users:
            for user in users:
                user_id, name, library_id = user
                print(f"User ID: {user_id}, Name: {name}, Library ID: {library_id}")
        else:
            print("No users available.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        
# Function to add a new author
def db_add_author(name, biography):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        values = (name, biography)
        cursor.execute(query, values)
        connection.commit()
        print("Author added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Function to view author details
def db_view_author_details(author_id):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT name, biography FROM authors WHERE author_id = %s"
        cursor.execute(query, (author_id,))
        author = cursor.fetchone()

        if author:
            name, biography = author
            print(f"Name: {name}, Biography: {biography}")
        else:
            print("Author not found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Function to display all authors
def db_display_all_authors():
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT author_id, name, biography FROM authors"  # Exclude any extra columns
        cursor.execute(query)
        authors = cursor.fetchall()

        return authors
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


# Function to add a new genre
def db_add_genre(name, description, category):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
        values = (name, description, category)
        cursor.execute(query, values)
        connection.commit()
        print("Genre added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Function to view genre details
def db_view_genre_details(genre_id):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM genres WHERE genre_id = %s"
        values = (genre_id,)
        cursor.execute(query, values)
        genre = cursor.fetchone()

        if genre:
            genre_id, name, description, category = genre
            print(f"Name: {name}, Description: {description}, Category: {category}")
        else:
            print("Genre not found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Function to display all genres
def db_display_all_genres():
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT genre_id, name, description, category FROM genres"
        cursor.execute(query)
        genres = cursor.fetchall()

        if genres:
            for genre in genres:
                genre_id, name, description, category = genre
                print(f"Genre ID: {genre_id}, Name: {name}, Description: {description}, Category: {category}")
        else:
            print("No genres available.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


