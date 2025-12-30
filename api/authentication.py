from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Get token from cookie
        raw_token = request.COOKIES.get("access_token")
        if raw_token is None:
            return None

        # decode token and return (user, token)
        validated_token = self.get_validated_token(raw_token)
        user = self.get_user(validated_token)
        return (user, validated_token)
