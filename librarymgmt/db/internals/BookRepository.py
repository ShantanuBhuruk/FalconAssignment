import falcon
from sqlobject import *
from db.models.BookModel import Book
from sqlobject.sqlbuilder import *
from db.models.AuthorModel import Author


class BookRepository:
    def get_book(self, book_id=None, name="", author=""):
        if book_id is None:
            return Book.select(AND(LIKE(Book.q.name, "%" + name + "%"), LIKE(Author.q.name, "%" + author + "%")),
                        join=INNERJOINOn(Book, Author, Book.q.author == Author.q.id))
        else:
            try:
                return Book.get(book_id)
            except SQLObjectNotFound:
                raise falcon.HTTPBadRequest(title='Wrong book id',
                                            description='Please provide valid book id to get info')

    def add_book(self, book_data):
        try:
            book = Book(name=book_data["name"], author=book_data["author_id"], rent=book_data["rent"])
            return book.get_dict()
        except Exception:
            raise falcon.HTTPBadRequest(title="Please provide valid data",
                                        description="The data you provided cannot be proccessed! Try again")

    def update_book(self, book_id=None, book_data={}):
        book = self.get_book(book_id=book_id)
        print(book.author.id)
        book_dict = book.get_dict()
        print(book_dict)
        for k, v in book_data.items():
            book_dict[k] = v
        try:
            book.set(name=book_dict["name"], author=Author.get(book.author.id), rent=book_dict['rent'])
        except:
            raise falcon.HTTPBadRequest(title="Wrong info",
                                        description="Well it seems that you've provided wrong author id!")

    def delete_book(self, book_id=None):
        if book_id is not None:
            Book.delete(book_id)
        else:
            raise falcon.HTTPBadRequest(title="Wrong info",
                                        description="Well it seems that you've provided wrong book id!")

