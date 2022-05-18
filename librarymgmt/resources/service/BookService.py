import falcon
import json
from db.internals.BookRepository import BookRepository

book_repository = BookRepository()


class BookService:
    def on_get(self, req, resp):
        params = req.params
        if params and params["book_id"]:
            book = book_repository.get_book(book_id=params["book_id"])
            resp.status = falcon.HTTP_200
            resp.media = {
                "Author": book.get_dict()
            }
        else:
            books = []
            for book in book_repository.get_book():
                books.append(book.get_dict())
            resp.status = falcon.HTTP_200
            resp.media = {
                "Authors": books
            }

    def on_post(self, req, resp):
        req_data = json.loads(req.stream.read())
        book = book_repository.add_book(book_data=req_data)
        resp.status = falcon.HTTP_201
        resp.media = book

    def on_put(self, req, resp):
        req_data = json.loads(req.stream.read())
        params = req.params
        if params and params["book_id"]:
            book_id = params["book_id"]
            book_repository.update_book(book_id=book_id, book_data=req_data)
            resp.media = {'author': book_repository.get_book(book_id=book_id).get_dict()}
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_400
            resp.media = {
                "msg": "Please re-verify the request"
            }

    def on_delete(self, req, resp):
        params = req.params
        if params and params["book_id"]:
            book_id = params["book_id"]
            book_repository.delete_book(book_id=book_id)
            resp.status = falcon.HTTP_200
            resp.media = {
                "msg": "Record deleted...!!!"
            }
        else:
            resp.status = falcon.HTTP_400
            resp.media = {
                "msg": "Please re-verify the request"
            }
