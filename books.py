class Book:
    def __init__(self, title, author_id, isbn, publication_date, genre_id):
        self.__title = title
        self.__author_id = author_id
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__genre_id = genre_id
        self.__is_borrowed = False

    def get_title(self):
        return self.__title

    def get_author_id(self):
        return self.__author_id

    def get_isbn(self):
        return self.__isbn

    def get_publication_date(self):
        return self.__publication_date
    
    def get_genre_id(self):
        return self.__genre_id

    def is_borrowed(self):
        return self.__is_borrowed

    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, " \
               f"Publication Date: {self.__publication_date}, Borrowed: {'Yes' if self.__is_borrowed else 'No'}"

class FictionBook(Book):
    def __init__(self, title, author, isbn, publication_date):
        super().__init__(title, author, isbn, publication_date)

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, publication_date):
        super().__init__(title, author, isbn, publication_date)
