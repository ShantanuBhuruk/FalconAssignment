from db.models.UserModel import User
from sqlobject import *


class UserRepository:
    @staticmethod
    def get_user(username, password):
        return User.select(AND(User.q.username == username, User.q.password == password))