from rest_framework_simplejwt.authentication import JWTAuthentication

"""
    Custom JWT authentication class that allows retrieving the access token
    from either the Authorization header or from cookies.
    
    By default, SimpleJWT only checks the Authorization header. This class
    extends it to also check for an 'access_token' cookie if the header is missing.
    """
class JWTAuthenticationFromCookie(JWTAuthentication):
    """
        Authenticate the user based on JWT token.

        Steps:
        1. Try to get the token from the Authorization header.
        2. If no header is present, attempt to get 'access_token' from cookies.
        3. Validate the token.
        4. Return the associated user and validated token.

        Returns:
            Tuple(user, validated_token) if authentication is successful.
            None if no token is found.
        """
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raw_token = request.COOKIES.get('access_token')
            if raw_token is None:
                return None
        else:
            raw_token = self.get_raw_token(header)

        validated_token = self.get_validated_token(raw_token)
        user = self.get_user(validated_token)
        return (user, validated_token)
