
# from unittest import result

from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = [] 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        result = connectToMySQL('books').query_db(query)
        authors = []
        for author in result:
            authors.append(cls(author))
        return authors

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        result = connectToMySQL('books').query_db(query, data)
        return result

    @classmethod
    def get_favs(cls, data):
        query= "SELECT * FROM authors LEFT JOIN favorite_books ON author_id = authors.id LEFT JOIN favorite_books ON book_id = books.id WHERE id = %(id)s"
        results = connectToMySQL('books').query_db(query, data)
        fav_books = []
        for fav_book in results:
            fav_books.append(cls(fav_book))
        return fav_books
