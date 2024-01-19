import datetime
from sys import exception
import jwt
from rest_framework import authentication, exceptions
from apps.oauth.models import AuthUser

from core import settings


class AuthBackend(authentication.BaseAuthentication):
    athentication_header_prefix = "Token"

    def authenticate(self, request, token=None, **kwargs):
        auth_header = authentication.get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower != b"token":
            return None

        if len(auth_header) == 1:
            raise exceptions.AuthenticationFailed(
                "Invalid token header. No credentials provided."
            )
        elif len(auth_header) > 2:
            raise exceptions.AuthenticationFailed(
                "Invalid token header. Token string should not contain spaces."
            )

        try:
            token = auth_header[1].decode("utf-8")
        except exception.AuthorizationError:
            raise exceptions.AuthenticationFailed(
                "Invalid token header. Token string containt invalid characters"
            )

        return self.authenticate_credentials(token)
    
    def authenticate_credentials(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.PyJWKError:
             raise exceptions.AuthenticationFailed('Invalid authentication. Could not decode token.')
        token_exp =datetime.fromtimestamp(payload['exp'])
        if token_exp < datetime.utcnow():
            raise exceptions.AuthenticationFailed('Token expired')
        
        try:
            user = AuthUser.objects.get(email=payload['email'])
        except AuthUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, None)
