import falcon
import jwt
import json

from db.internals.UserRepository import UserRepository


class LoginService:
    def __init__(self):
        pass

    def login(self, req, resp):
        req_params = json.loads(req.stream.read())
        print("Attempting Login")

        if not req_params or not req_params["Username"] or not req_params["Password"]:
            raise falcon.HTTPBadRequest("Bad Request", "Please enter valid Username and Password")
        else:
            print("authenticating with username: {} and password: {}".format(req_params["Username"], req_params["Password"]))
            self._authenticate(req_params["Username"], req_params["Password"], req, resp)

    def _authenticate(self, username, password, req, resp):
        if not username or not password:
            raise falcon.HTTPBadRequest("Bad Request", "Please enter valid Username and Password")
        else:
            print("Fetching User Form DB")
            users = UserRepository.get_user(username, password)
            print("User Info: {}".format(users))
            if users.count() > 0:
                user = users[0]
                payload = {
                    "userid": user.id
                }
                secret = "secret"
                algo = "HS256"
                token = jwt.encode(payload=payload, key=secret, algorithm=algo)
                resp.media = {
                    "token": token
                }
                resp.status = falcon.HTTP_200
            else:
                raise falcon.HTTPUnauthorized("Unauthorized", "Invalid Credentials")

    def on_post(self, req, resp):
        self.login(req, resp)


def main():
    pass


if __name__ == "__main__": main()
