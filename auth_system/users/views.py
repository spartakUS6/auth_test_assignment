import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password

from users.models import User
from users.jwt_utils import create_jwt
from django.views.decorators.http import require_http_methods


@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    data = json.loads(request.body)

    if data["password"] != data["password_repeat"]:
        return JsonResponse({"detail": "Passwords do not match"}, status=400)

    if User.objects.filter(email=data["email"]).exists():
        return JsonResponse({"detail": "Email already exists"}, status=400)

    user = User.objects.create(
        email=data["email"],
        password_hash=make_password(data["password"]),
        first_name=data["first_name"],
        last_name=data["last_name"],
        patronymic=data.get("patronymic", "")
    )

    return JsonResponse({"id": user.id})


@require_http_methods(["POST"])
def login(request):
    data = request.POST
    email = data.get("email")
    password = data.get("password")

    try:
        user = User.objects.get(email=email, is_active=True)
    except User.DoesNotExist:
        return JsonResponse({"detail": "Invalid credentials"}, status=400)

    if not check_password(password, user.password):
        return JsonResponse({"detail": "Invalid credentials"}, status=400)

    token = create_jwt(user.id)
    return JsonResponse({"token": token})


@require_http_methods(["POST"])
def logout(request):
    return JsonResponse({"detail": "Logged out"})


@require_http_methods(["GET", "PATCH"])
def me(request):
    if not request.user:
        return JsonResponse({"detail": "Unauthorized"}, status=401)

    if request.method == "GET":
        return JsonResponse({
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "middle_name": request.user.middle_name,
        })

    data = request.POST
    request.user.first_name = data.get("first_name", request.user.first_name)
    request.user.last_name = data.get("last_name", request.user.last_name)
    request.user.middle_name = data.get("middle_name", request.user.middle_name)
    request.user.save()

    return JsonResponse({"detail": "Profile updated"})




@csrf_exempt
def update_me(request):
    if not request.user:
        return JsonResponse({"detail": "Unauthorized"}, status=401)

    data = json.loads(request.body)

    for field in ("first_name", "last_name", "patronymic"):
        if field in data:
            setattr(request.user, field, data[field])

    request.user.save()
    return JsonResponse({"detail": "Updated"})


@require_http_methods(["DELETE"])
def soft_delete(request):
    if not request.user:
        return JsonResponse({"detail": "Unauthorized"}, status=401)

    request.user.is_active = False
    request.user.save()
    return JsonResponse({"detail": "Account deleted"})
