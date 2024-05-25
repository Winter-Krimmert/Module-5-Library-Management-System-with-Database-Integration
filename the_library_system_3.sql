-- Create the database
CREATE DATABASE the_library_system_3;

DROP DATABASE the_library_system_3;

-- Use the newly created database
USE the_library_system_3;


-- Create the authors table
CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

-- Create the books table
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(14) UNIQUE NOT NULL,
    publication_date DATE,
    genre_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);
DROP TABLE books;
-- Create the users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(255) UNIQUE NOT NULL
);

-- Create the borrowed_books table
CREATE TABLE borrowed_books (
    borrow_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
ALTER TABLE books ADD COLUMN is_borrowed BOOLEAN DEFAULT FALSE;

-- Create the genres table
CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(255)
);

SELECT * FROM Authors;
SELECT * FROM Genres;
SELECT * FROM Books;
SELECT * FROM Users;
SELECT * FROM Borrowed_Books;