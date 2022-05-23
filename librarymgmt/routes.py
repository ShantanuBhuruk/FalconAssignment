import falcon
from resources.service.login import LoginService
from resources.service.AuthorService import AuthorService
from resources.service.BookService import BookService


def get_app():
    application = falcon.App()
    application.add_route("/login", LoginService())
    application.add_route("/authors", AuthorService())
    application.add_route("/books", BookService())
    return application
