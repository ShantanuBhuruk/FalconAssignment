from sqlobject import *
from srv import conn
from db.models.BookModel import Book


class Author(SQLObject):
    _connection = conn
    name = StringCol(length=32, notNone=True)
    books = MultipleJoin("Book")

    def get_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "books": [book.name for book in Book.select(Book.q.author == self)]
        }


Author.createTable(ifNotExists=True)
