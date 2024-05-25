class Author:
    def __init__(self, author_id, name, biography):
    
        self.__author_id = author_id
        self.__name = name
        self.__biography = biography

    def get_author_id(self):
        return self.__author_id

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def __str__(self):
        return f"Author ID: {self.__author_id}, Name: {self.__name}, Biography: {self.__biography}"
