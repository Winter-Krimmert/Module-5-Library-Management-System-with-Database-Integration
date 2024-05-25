class Genre:
    def __init__(self, genre_id, name, description, category):
       
        self.__genre_id = genre_id
        self.__name = name
        self.__description = description
        self.__category = category

    def get_genre_id(self):
        return self.__genre_id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_category(self):
        return self.__category

    def __str__(self):
        return f"Name: {self.__name}, Description: {self.__description}, Category: {self.__category}"
