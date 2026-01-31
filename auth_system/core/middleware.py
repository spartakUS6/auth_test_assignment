from django.http import JsonResponse
from users.models import User
from users.jwt_utils import decode_jwt


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = None

        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            payload = decode_jwt(token)

            if payload:
                try:
                    user = User.objects.get(
                        id=payload["user_id"],
                        is_active=True
                    )
                    request.user = user
                except User.DoesNotExist:
                    return JsonResponse(
                        {"detail": "User not found"},
                        status=401
                    )

        return self.get_response(request)
