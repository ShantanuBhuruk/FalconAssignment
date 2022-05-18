from sqlobject import *
from srv import conn


class User(SQLObject):
    _connection = conn
    username = StringCol(length=30, notNone=True, unique=True)
    password = StringCol(length=30, notNone=True)


User.createTable(ifNotExists=True)