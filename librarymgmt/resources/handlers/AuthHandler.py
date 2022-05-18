import falcon
import jwt
import sqlobject.dberrors
from db.models.UserModel import User


class AuthHandler:
    def process_request(self, req, resp):
        if "/login" in req.path:
            return

        if req.get_header("Authorization"):
            auth_header = req.get_header("Authorization").split(" ")
            token = auth_header[1]
            if token:
                if not self._is_token_valid(token):
                    description = "The provided auth token is not valid.Please request a new token and try again."
                    raise falcon.HTTPUnauthorized("Unauthorized", description)

    def _is_token_valid(self, token):
        try:
            payload = jwt.decode(jwt=token, key="secret", algorithms="HS256")
            userid = payload["userid"]
            user = User.get(payload['user_id'])
            print("Authenticated, User : {}".format(user))
            return True
        except (jwt.DecodeError, jwt.ExpiredSignatureError, sqlobject.dberrors.Error):
            return False


