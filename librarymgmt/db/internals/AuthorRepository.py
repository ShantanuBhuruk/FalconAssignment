from sqlobject import *
import falcon
from db.models.AuthorModel import Author


class AuthorRepository:
    def get_author(self, author_id=None, name=""):
        if author_id is None:
            return Author.select(LIKE(Author.q.name, "%"+name+"%"))
        else:
            try:
                return Author.get(author_id)
            except SQLObjectNotFound:
                raise falcon.HTTPBadRequest(title='Wrong author id',
                                            description='Please provide valid author id to get info')

    def add_author(self, author_data):
        try:
            author = Author(name=author_data["name"])
            return author.get_dict()
        except Exception:
            raise falcon.HTTPBadRequest(title="Please provide valid data",
                                        description="The data you provided cannot be proccessed! Try again")

    def update_author(self, author_id=None, author_data={}):
        if author_id is not None:
            author = self.get_author(author_id=author_id)
            author_dict = author.get_dict()
            for k, v in author_data.items():
                author_dict[k] = v
            author.set(name=author_dict['name'])
        else:
            raise falcon.HTTPBadRequest(title="Please provide valid data",
                                        description="The data you provided cannot be proccessed! Try again")

    def delete_author(self, author_id=None):
        if author_id is not None:
            Author.delete(author_id)
        else:
            raise falcon.HTTPBadRequest(title="Please provide valid data",
                                        description="The data you provided cannot be proccessed! Try again")

