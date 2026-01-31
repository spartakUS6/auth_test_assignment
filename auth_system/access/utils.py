from django.http import JsonResponse


def permission_required(permission_code: str):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user:
                return JsonResponse(
                    {"detail": "Unauthorized"},
                    status=401
                )

            user_permissions = set(
                request.user.roles
                .values_list("permissions__code", flat=True)
            )

            if permission_code not in user_permissions:
                return JsonResponse(
                    {"detail": "Forbidden"},
                    status=403
                )

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
