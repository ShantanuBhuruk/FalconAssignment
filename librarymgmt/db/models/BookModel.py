from sqlobject import *
from srv import conn

class Book(SQLObject):
    _connection = conn
    name = StringCol(length=32, notNone=True, unique=True)
    rent = IntCol(notNone=True)
    author = ForeignKey('Author', cascade=True)


    def get_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author.name,
            "rent": self.rent
        }


Book.createTable(ifNotExists=True)
