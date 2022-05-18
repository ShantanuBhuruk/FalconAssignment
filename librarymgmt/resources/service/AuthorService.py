import json
import falcon
from db.internals.AuthorRepository import AuthorRepository

auth_repository = AuthorRepository()


class AuthorService:

    def on_get(self, req, resp):
        params = req.params
        if params and params["author_id"]:
            author = auth_repository.get_author(author_id=params["author_id"])
            resp.status = falcon.HTTP_200
            resp.media = {
                "Author": author.get_dict()
            }
        else:
            authors = []
            for author in auth_repository.get_author():
                authors.append(author.get_dict())

            resp.status = falcon.HTTP_200
            resp.media = {
                "Authors": authors
            }

    def on_post(self, req, resp):
        req_data = json.loads(req.stream.read())
        author = auth_repository.add_author(author_data=req_data)
        resp.status = falcon.HTTP_201
        resp.media = author

    def on_put(self, req, resp):
        req_data = json.loads(req.stream.read())
        params = req.params
        if params and params["author_id"]:
            author_id = params["author_id"]
            auth_repository.update_author(author_id=author_id, author_data=req_data)
            resp.media = {'author': auth_repository.get_author(author_id=author_id).get_dict()}
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_400
            resp.media ={
                "msg" : "Please re-verify the request"
            }

    def on_delete(self, req, resp):
        params = req.params
        if params and params["author_id"]:
            author_id = params["author_id"]
            auth_repository.delete_author(author_id=author_id)
            resp.status = falcon.HTTP_200
            resp.media = {
                "msg": "Record deleted...!!!"
            }
        else:
            resp.status = falcon.HTTP_400
            resp.media ={
                "msg" : "Please re-verify the request"
            }