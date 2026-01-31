from django.http import JsonResponse


def require_permission(permission_code):
    def decorator(view_func):
        def wrapped(request, *args, **kwargs):
            if not request.user:
                return JsonResponse(
                    {"detail": "Unauthorized"},
                    status=401
                )

            if not request.user.has_permission(permission_code):
                return JsonResponse(
                    {"detail": "Forbidden"},
                    status=403
                )

            return view_func(request, *args, **kwargs)
        return wrapped
    return decorator
